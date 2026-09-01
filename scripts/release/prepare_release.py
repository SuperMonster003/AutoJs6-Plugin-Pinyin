#!/usr/bin/env python3
"""Build and prepare one verified, signed universal Pinyin APK release bundle."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable
from uuid import uuid4


CATEGORY_ORDER = ("hint", "feature", "fix", "improvement", "dependency")
RAW_APK_NAMES = {"app-release.apk", "app-universal-release.apk"}
REQUIRED_ASSETS = {
    "assets/dict-chinese-chars.db.gzip",
    "assets/dict-chinese-phrases.db.gzip",
    "assets/dict-chinese-words.db.gzip",
    "assets/prob_emit.txt",
}


class ReleaseError(Exception):
    pass


@dataclass(frozen=True)
class ReleaseContext:
    root: Path
    project_name: str
    version_name: str
    version_code: int
    changelog: dict[str, Any]
    release_entry: dict[str, Any]


@dataclass(frozen=True)
class ApkManifestVersion:
    version_name: str
    version_code: int


@dataclass(frozen=True)
class PackageRecord:
    source: Path
    filename: str
    crc32: str
    sha256: str
    size: int


ManifestReader = Callable[[Path], ApkManifestVersion]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReleaseError(message)


def load_properties(path: Path) -> dict[str, str]:
    require(path.is_file(), f"Missing properties file: {path}")
    properties: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("#", "!")):
            continue
        key, separator, value = line.partition("=")
        require(bool(separator), f"Invalid properties line in {path}: {raw_line!r}")
        key = key.strip()
        require(bool(key), f"Empty property name in {path}: {raw_line!r}")
        require(key not in properties, f"Duplicate property {key!r} in {path}")
        properties[key] = value.strip()
    return properties


def load_release_context(root: Path) -> ReleaseContext:
    root = root.resolve()
    settings_path = root / "settings.gradle.kts"
    require(settings_path.is_file(), f"Missing Gradle settings: {settings_path}")
    settings = settings_path.read_text(encoding="utf-8")
    project_match = re.search(r'rootProject\.name\s*=\s*"([^"]+)"', settings)
    require(project_match is not None, "Cannot determine rootProject.name from settings.gradle.kts")
    project_name = project_match.group(1)

    properties = load_properties(root / "version.properties")
    version_name = properties.get("VERSION_NAME", "")
    require(bool(version_name), "VERSION_NAME is missing from version.properties")
    version_code_text = properties.get("VERSION_BUILD", "")
    require(version_code_text.isdigit(), "VERSION_BUILD must be a non-negative integer")
    version_code = int(version_code_text)

    changelog_path = root / ".changelog" / "lang_en.json"
    require(changelog_path.is_file(), f"Missing English changelog source: {changelog_path}")
    try:
        changelog = json.loads(changelog_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ReleaseError(f"Invalid English changelog JSON: {error}") from None
    require(isinstance(changelog, dict), "English changelog root must be an object")
    data = changelog.get("$data")
    require(isinstance(data, dict) and data, "English changelog has no release entries")
    version_label = f"v{version_name}"
    newest_label = next(iter(data))
    require(
        newest_label == version_label,
        f"Newest English changelog entry {newest_label!r} does not match {version_label!r}",
    )
    release_entry = data.get(version_label)
    require(isinstance(release_entry, dict), f"Missing English changelog entry for {version_label}")
    require(bool(release_entry.get("released_date")), f"English changelog entry {version_label} has no release date")
    return ReleaseContext(root, project_name, version_name, version_code, changelog, release_entry)


def run_release_build(context: ReleaseContext) -> None:
    signing_properties = context.root / "sign.properties"
    require(
        signing_properties.is_file() and signing_properties.stat().st_size > 0,
        "Missing untracked sign.properties; a release must be built with an explicit signing identity",
    )
    wrapper = context.root / ("gradlew.bat" if os.name == "nt" else "gradlew")
    require(wrapper.is_file(), f"Missing Gradle wrapper: {wrapper}")
    if os.name == "nt":
        command = ["cmd.exe", "/d", "/c", str(wrapper), ":app:assembleRelease", "--stacktrace"]
    else:
        command = [str(wrapper), ":app:assembleRelease", "--stacktrace"]
    print("Running signed release build...")
    try:
        subprocess.run(command, cwd=context.root, check=True)
    except subprocess.CalledProcessError as error:
        raise ReleaseError(f"Gradle release build failed with exit code {error.returncode}") from None


def released_apk_pattern(project_name: str) -> re.Pattern[str]:
    return re.compile(
        rf"^{re.escape(project_name)}-v(?P<version>.+?)-universal-"
        rf"(?P<crc>[0-9a-fA-F]{{8}})\.apk$",
    )


def crc32(path: Path) -> str:
    value = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value = zlib.crc32(block, value)
    return f"{value & 0xFFFFFFFF:08x}"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def discover_apk(input_dir: Path, context: ReleaseContext) -> tuple[Path, list[Path]]:
    input_dir = input_dir.resolve()
    require(input_dir.is_dir(), f"Release APK directory is missing: {input_dir}")
    apk_files = sorted(path for path in input_dir.glob("*.apk") if path.is_file())
    require(bool(apk_files), f"No APK files found in {input_dir}")

    raw_candidates = [path for path in apk_files if path.name in RAW_APK_NAMES]
    if raw_candidates:
        require(
            len(raw_candidates) == 1 and len(apk_files) == 1,
            "Raw release APK inventory mismatch: expected exactly one universal app-release APK, "
            f"actual={[path.name for path in apk_files]}",
        )
        return raw_candidates[0], []

    pattern = released_apk_pattern(context.project_name)
    candidates: list[Path] = []
    foreign_versions: list[Path] = []
    malformed_current: list[str] = []
    current_prefix = f"{context.project_name}-v{context.version_name}-"
    for path in apk_files:
        match = pattern.match(path.name)
        if match is None:
            if path.name.startswith(current_prefix):
                malformed_current.append(path.name)
            else:
                foreign_versions.append(path)
            continue
        if match.group("version") != context.version_name:
            foreign_versions.append(path)
            continue
        candidates.append(path)

    require(not malformed_current, f"Malformed current-version APK names: {sorted(malformed_current)}")
    require(bool(candidates), f"Missing current-version universal APK for v{context.version_name}")
    require(
        len(candidates) == 1,
        f"Duplicate current-version universal APKs detected: {[path.name for path in candidates]}",
    )
    return candidates[0], foreign_versions


def validate_apk_archive(path: Path) -> None:
    try:
        with zipfile.ZipFile(path) as archive:
            corrupt_entry = archive.testzip()
            require(corrupt_entry is None, f"Corrupt ZIP entry in {path.name}: {corrupt_entry}")
            names = set(archive.namelist())
            require("AndroidManifest.xml" in names, f"AndroidManifest.xml is missing from {path.name}")
            require(
                any(name.startswith("classes") and name.endswith(".dex") for name in names),
                f"DEX payload is missing from {path.name}",
            )
            native_libraries = sorted(
                name for name in names if name.startswith("lib/") and name.endswith(".so")
            )
            require(not native_libraries, f"Pure-JVM APK contains native libraries: {native_libraries}")
            missing_assets = sorted(REQUIRED_ASSETS - names)
            require(not missing_assets, f"Required Pinyin assets are missing: {missing_assets}")
    except zipfile.BadZipFile:
        raise ReleaseError(f"Not a valid APK ZIP archive: {path}") from None


def validate_manifest_version(
    path: Path,
    context: ReleaseContext,
    manifest_reader: ManifestReader,
) -> None:
    manifest = manifest_reader(path)
    require(
        manifest.version_name == context.version_name,
        f"APK versionName mismatch: expected={context.version_name}, actual={manifest.version_name}",
    )
    require(
        manifest.version_code == context.version_code,
        f"APK versionCode mismatch: expected={context.version_code}, actual={manifest.version_code}",
    )


def collect_record(
    input_dir: Path,
    context: ReleaseContext,
    manifest_reader: ManifestReader,
) -> tuple[PackageRecord, list[Path]]:
    source, foreign_versions = discover_apk(input_dir, context)
    validate_apk_archive(source)
    validate_manifest_version(source, context, manifest_reader)

    match = released_apk_pattern(context.project_name).match(source.name)
    package_crc = crc32(source)
    if match is not None:
        expected_crc = match.group("crc").lower()
        require(
            package_crc == expected_crc,
            f"CRC32 filename mismatch for {source.name}: expected={expected_crc}, actual={package_crc}",
        )

    filename = f"{context.project_name}-v{context.version_name}-universal-{package_crc}.apk"
    return (
        PackageRecord(
            source=source,
            filename=filename,
            crc32=package_crc,
            sha256=sha256(source),
            size=source.stat().st_size,
        ),
        foreign_versions,
    )


def decode_local_property_path(value: str) -> str:
    return value.replace("\\:", ":").replace("\\\\", "\\")


def android_sdk_roots(root: Path) -> list[Path]:
    candidates: list[Path] = []
    for variable in ("ANDROID_SDK_ROOT", "ANDROID_HOME"):
        value = os.environ.get(variable)
        if value:
            candidates.append(Path(value).expanduser())

    local_properties = root / "local.properties"
    if local_properties.is_file():
        properties = load_properties(local_properties)
        sdk_dir = properties.get("sdk.dir")
        if sdk_dir:
            candidates.append(Path(decode_local_property_path(sdk_dir)).expanduser())

    unique: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved not in seen:
            unique.append(resolved)
            seen.add(resolved)
    return unique


def numeric_version_key(path: Path) -> tuple[int, ...]:
    numbers = tuple(int(part) for part in re.findall(r"\d+", path.parent.name))
    return numbers or (0,)


def find_apksigner(root: Path, explicit: Path | None = None) -> Path:
    if explicit is not None:
        candidate = explicit.expanduser().resolve()
        require(candidate.is_file(), f"apksigner does not exist: {candidate}")
        return candidate

    command = shutil.which("apksigner") or shutil.which("apksigner.bat")
    if command:
        return Path(command).resolve()

    executable = "apksigner.bat" if os.name == "nt" else "apksigner"
    candidates: list[Path] = []
    for sdk_root in android_sdk_roots(root):
        build_tools = sdk_root / "build-tools"
        if build_tools.is_dir():
            candidates.extend(path for path in build_tools.glob(f"*/{executable}") if path.is_file())
    require(bool(candidates), "Cannot locate apksigner; configure local.properties or ANDROID_SDK_ROOT")
    return max(candidates, key=numeric_version_key).resolve()


def find_apkanalyzer(root: Path, explicit: Path | None = None) -> Path:
    if explicit is not None:
        candidate = explicit.expanduser().resolve()
        require(candidate.is_file(), f"apkanalyzer does not exist: {candidate}")
        return candidate

    command = shutil.which("apkanalyzer") or shutil.which("apkanalyzer.bat")
    if command:
        return Path(command).resolve()

    executable = "apkanalyzer.bat" if os.name == "nt" else "apkanalyzer"
    candidates: list[Path] = []
    for sdk_root in android_sdk_roots(root):
        command_line_tools = sdk_root / "cmdline-tools"
        if command_line_tools.is_dir():
            candidates.extend(
                path for path in command_line_tools.glob(f"*/bin/{executable}") if path.is_file()
            )
    require(bool(candidates), "Cannot locate apkanalyzer; configure local.properties or ANDROID_SDK_ROOT")

    def analyzer_key(path: Path) -> tuple[int, tuple[int, ...]]:
        version_directory = path.parent.parent.name
        return (1 if version_directory == "latest" else 0, tuple(int(x) for x in re.findall(r"\d+", version_directory)))

    return max(candidates, key=analyzer_key).resolve()


def tool_command(tool: Path, arguments: list[str]) -> list[str]:
    command = [str(tool), *arguments]
    if os.name == "nt" and tool.suffix.lower() in (".bat", ".cmd"):
        return ["cmd.exe", "/d", "/c", *command]
    return command


def run_tool(tool: Path, arguments: list[str], label: str) -> str:
    result = subprocess.run(
        tool_command(tool, arguments),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = f"{result.stdout}\n{result.stderr}".strip()
    require(result.returncode == 0, f"{label} failed with exit code {result.returncode}: {output}")
    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    require(bool(lines), f"{label} returned no output")
    return lines[-1]


def read_apk_manifest_version(apkanalyzer: Path, apk: Path) -> ApkManifestVersion:
    version_name = run_tool(
        apkanalyzer,
        ["manifest", "version-name", str(apk)],
        f"Reading versionName from {apk.name}",
    )
    version_code_text = run_tool(
        apkanalyzer,
        ["manifest", "version-code", str(apk)],
        f"Reading versionCode from {apk.name}",
    )
    require(version_code_text.isdigit(), f"Invalid APK versionCode from apkanalyzer: {version_code_text!r}")
    return ApkManifestVersion(version_name, int(version_code_text))


def signer_digest_from_output(output: str) -> str:
    pattern = re.compile(
        r"(?:Signer #\d+|V\d+(?:\.\d+)? Signer):? certificate SHA-256 digest:\s*([0-9a-fA-F]+)",
    )
    match = pattern.search(output)
    require(match is not None, "Cannot read signer certificate digest from apksigner output")
    return match.group(1).upper()


def verify_signature(record: PackageRecord, apksigner: Path) -> str:
    arguments = ["verify", "--verbose", "--print-certs", str(record.source)]
    result = subprocess.run(
        tool_command(apksigner, arguments),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    output = f"{result.stdout}\n{result.stderr}"
    require(result.returncode == 0, f"Signature verification failed for {record.source.name}: {output.strip()}")
    try:
        return signer_digest_from_output(output)
    except ReleaseError:
        raise ReleaseError(f"Cannot read signer certificate digest from {record.source.name}") from None


def render_release_notes(
    context: ReleaseContext,
    record: PackageRecord,
    signer_digest: str | None,
) -> str:
    date = str(context.release_entry.get("released_date", "")).replace("/", "-")
    lines = [
        f"# {context.project_name} v{context.version_name}",
        "",
        f"Release date: {date}",
        f"Version code: {context.version_code}",
        "",
        "Generated from the English changelog source at `.changelog/lang_en.json`.",
    ]
    for category in CATEGORY_ORDER:
        entries = context.release_entry.get(category, [])
        if not entries:
            continue
        label = context.changelog.get(f"changelog_label_{category}", category.title())
        lines.extend(("", f"## {label}", ""))
        lines.extend(f"- {entry}" for entry in entries)

    lines.extend(
        (
            "",
            "## Package",
            "",
            "| Variant | File | Size (bytes) | CRC32 | SHA-256 |",
            "|---|---|---:|---|---|",
            f"| `universal` | `{record.filename}` | {record.size} | `{record.crc32}` | `{record.sha256}` |",
            "",
            "## Verification",
            "",
            f"- APK manifest verified as version `{context.version_name}` (code `{context.version_code}`).",
            "- The APK is pure JVM and contains no native libraries.",
            "- Verify the package hash with `SHA256SUMS.txt`.",
        ),
    )
    if signer_digest is not None:
        lines.append(f"- Signer certificate SHA-256: `{signer_digest}`")
    return "\n".join(lines).rstrip() + "\n"


def output_is_safe(output_dir: Path, context: ReleaseContext) -> bool:
    release_root = (context.root / "build" / "release").resolve()
    try:
        output_dir.resolve().relative_to(release_root)
    except ValueError:
        return False
    return output_dir.resolve() != release_root


def create_bundle(
    context: ReleaseContext,
    record: PackageRecord,
    output_dir: Path,
    signer_digest: str | None,
    overwrite: bool = False,
) -> Path:
    output_dir = output_dir.resolve()
    require(
        output_is_safe(output_dir, context),
        f"Release output must be a child of {context.root / 'build' / 'release'}: {output_dir}",
    )
    require(not output_dir.exists() or overwrite, f"Output directory already exists: {output_dir}")

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=f".{output_dir.name}-stage-", dir=output_dir.parent))
    backup: Path | None = None
    committed = False
    try:
        destination = stage / record.filename
        shutil.copy2(record.source, destination)
        require(sha256(destination) == record.sha256, f"SHA-256 changed while copying {record.filename}")

        checksum_text = f"{record.sha256}  {record.filename}\n"
        (stage / "SHA256SUMS.txt").write_text(checksum_text, encoding="utf-8", newline="\n")
        (stage / "RELEASE_NOTES.md").write_text(
            render_release_notes(context, record, signer_digest),
            encoding="utf-8",
            newline="\n",
        )

        if output_dir.exists():
            backup = output_dir.parent / f".{output_dir.name}-backup-{uuid4().hex}"
            output_dir.replace(backup)
        stage.replace(output_dir)
        committed = True
        if backup is not None:
            shutil.rmtree(backup)
        return output_dir
    except Exception:
        if not committed and backup is not None and backup.exists() and not output_dir.exists():
            backup.replace(output_dir)
        raise
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="APK source directory; defaults to Gradle release outputs")
    parser.add_argument(
        "--output",
        type=Path,
        help="bundle directory under build/release; defaults to build/release/v<version>",
    )
    parser.add_argument("--skip-build", action="store_true", help="use existing APKs without running assembleRelease")
    parser.add_argument("--apksigner", type=Path, help="explicit path to apksigner or apksigner.bat")
    parser.add_argument("--apkanalyzer", type=Path, help="explicit path to apkanalyzer or apkanalyzer.bat")
    parser.add_argument("--overwrite", action="store_true", help="atomically replace an existing bundle")
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    root = Path(__file__).resolve().parents[2]
    try:
        context = load_release_context(root)
        if not arguments.skip_build:
            run_release_build(context)

        input_dir = (arguments.input or root / "app" / "build" / "outputs" / "apk" / "release").resolve()
        output_dir = (arguments.output or root / "build" / "release" / f"v{context.version_name}").resolve()
        apkanalyzer = find_apkanalyzer(root, arguments.apkanalyzer)
        record, foreign_versions = collect_record(
            input_dir,
            context,
            manifest_reader=lambda apk: read_apk_manifest_version(apkanalyzer, apk),
        )
        for path in foreign_versions:
            print(f"Ignoring foreign-version APK: {path.name}")

        apksigner = find_apksigner(root, arguments.apksigner)
        signer_digest = verify_signature(record, apksigner)
        print(f"SIGNER_OK sha256={signer_digest}")

        bundle = create_bundle(context, record, output_dir, signer_digest, arguments.overwrite)
        print(
            f"PACKAGE_OK variant=universal file={record.filename} bytes={record.size} "
            f"crc32={record.crc32} sha256={record.sha256}",
        )
        print(f"RELEASE_OK version={context.version_name} packages=1 output={bundle}")
        return 0
    except (ReleaseError, OSError) as error:
        print(f"RELEASE_ERROR {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
