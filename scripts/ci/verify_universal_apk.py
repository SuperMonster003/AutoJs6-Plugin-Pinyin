#!/usr/bin/env python3
"""Verify the plugin's single pure-JVM APK inventory and required assets."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path


REQUIRED_ASSETS = {
    "assets/dict-chinese-chars.db.gzip",
    "assets/dict-chinese-phrases.db.gzip",
    "assets/dict-chinese-words.db.gzip",
    "assets/prob_emit.txt",
}


class VerificationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def verify(directory: Path, build_type: str = "debug") -> Path:
    require(directory.is_dir(), f"APK output directory is missing: {directory}")
    expected_name = f"app-{build_type}.apk"
    actual = {path.name for path in directory.glob("*.apk") if path.is_file()}
    require(
        actual == {expected_name},
        f"Unexpected APK inventory: expected={[expected_name]}, actual={sorted(actual)}",
    )

    path = directory / expected_name
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
        raise VerificationError(f"Not a valid APK ZIP archive: {path}") from None

    return path


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="directory containing the APK output")
    parser.add_argument(
        "--build-type",
        choices=("debug", "release"),
        default="debug",
        help="APK build type (default: debug)",
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    try:
        path = verify(arguments.directory.resolve(), arguments.build_type)
    except VerificationError as error:
        print(f"APK_ERROR {error}", file=sys.stderr)
        return 1
    print(f"APK_OK file={path.name} pure_jvm=true assets={len(REQUIRED_ASSETS)} bytes={path.stat().st_size}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
