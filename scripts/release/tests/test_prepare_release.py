from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.release.prepare_release import (
    ApkManifestVersion,
    ReleaseError,
    collect_record,
    create_bundle,
    crc32,
    load_release_context,
    sha256,
    signer_digest_from_output,
)


class PrepareReleaseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        (self.root / ".changelog").mkdir()
        (self.root / "settings.gradle.kts").write_text(
            'rootProject.name = "autojs6-plugin-pinyin"\n',
            encoding="utf-8",
        )
        (self.root / "version.properties").write_text(
            "VERSION_NAME=1.2.3\nVERSION_BUILD=27\n",
            encoding="utf-8",
        )
        changelog = {
            "changelog_label_hint": "Hint",
            "changelog_label_feature": "Feature",
            "changelog_label_fix": "Fix",
            "changelog_label_improvement": "Improvement",
            "changelog_label_dependency": "Dependency",
            "$data": {
                "v1.2.3": {
                    "released_date": "2026/09/01",
                    "improvement": ["Verified release tooling."],
                },
            },
        }
        (self.root / ".changelog" / "lang_en.json").write_text(
            json.dumps(changelog),
            encoding="utf-8",
        )
        self.input_dir = self.root / "input"
        self.input_dir.mkdir()
        self.context = load_release_context(self.root)
        self.manifest_reader = lambda _: ApkManifestVersion("1.2.3", 27)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def create_fake_apk(
        self,
        path: Path,
        marker: str = "fixture",
        include_native_library: bool = False,
        omit_asset: str | None = None,
    ) -> None:
        assets = {
            "assets/dict-chinese-chars.db.gzip",
            "assets/dict-chinese-phrases.db.gzip",
            "assets/dict-chinese-words.db.gzip",
            "assets/prob_emit.txt",
        }
        with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("AndroidManifest.xml", f"manifest-{marker}")
            archive.writestr("classes.dex", f"dex-{marker}")
            for asset in sorted(assets - {omit_asset}):
                archive.writestr(asset, f"asset-{asset}-{marker}")
            if include_native_library:
                archive.writestr("lib/x86_64/libunexpected.so", "native")

    def create_released_apk(self, marker: str = "current") -> Path:
        temporary = self.input_dir / f"{marker}.tmp"
        self.create_fake_apk(temporary, marker)
        final = self.input_dir / f"autojs6-plugin-pinyin-v1.2.3-universal-{crc32(temporary)}.apk"
        temporary.rename(final)
        return final

    def test_complete_bundle_has_exact_checksum_and_english_notes(self) -> None:
        self.create_fake_apk(self.input_dir / "app-release.apk")
        record, foreign = collect_record(self.input_dir, self.context, self.manifest_reader)

        self.assertEqual([], foreign)
        self.assertEqual("autojs6-plugin-pinyin-v1.2.3-universal", record.filename.rsplit("-", 1)[0])
        output = create_bundle(
            self.context,
            record,
            self.root / "build" / "release" / "v1.2.3",
            signer_digest="A" * 64,
        )
        self.assertEqual(
            {record.filename, "SHA256SUMS.txt", "RELEASE_NOTES.md"},
            {path.name for path in output.iterdir()},
        )
        self.assertEqual(
            f"{sha256(output / record.filename)}  {record.filename}",
            (output / "SHA256SUMS.txt").read_text(encoding="utf-8").strip(),
        )
        notes = (output / "RELEASE_NOTES.md").read_text(encoding="utf-8")
        self.assertIn("Verified release tooling.", notes)
        self.assertIn("Version code: 27", notes)
        self.assertIn("Signer certificate SHA-256", notes)
        self.assertIn("`universal`", notes)

    def test_missing_or_mixed_raw_inventory_is_rejected(self) -> None:
        with self.assertRaisesRegex(ReleaseError, "No APK files"):
            collect_record(self.input_dir, self.context, self.manifest_reader)

        self.create_fake_apk(self.input_dir / "app-release.apk", "one")
        self.create_fake_apk(self.input_dir / "unexpected.apk", "two")
        with self.assertRaisesRegex(ReleaseError, "inventory mismatch"):
            collect_record(self.input_dir, self.context, self.manifest_reader)

    def test_duplicate_current_version_packages_are_rejected(self) -> None:
        self.create_released_apk("first")
        self.create_released_apk("second")
        with self.assertRaisesRegex(ReleaseError, "Duplicate current-version"):
            collect_record(self.input_dir, self.context, self.manifest_reader)

    def test_native_library_and_missing_dictionary_asset_are_rejected(self) -> None:
        native = self.input_dir / "app-release.apk"
        self.create_fake_apk(native, include_native_library=True)
        with self.assertRaisesRegex(ReleaseError, "native libraries"):
            collect_record(self.input_dir, self.context, self.manifest_reader)

        native.unlink()
        self.create_fake_apk(native, omit_asset="assets/prob_emit.txt")
        with self.assertRaisesRegex(ReleaseError, "assets/prob_emit.txt"):
            collect_record(self.input_dir, self.context, self.manifest_reader)

    def test_crc_filename_mismatch_is_rejected(self) -> None:
        released = self.create_released_apk()
        with released.open("ab") as stream:
            stream.write(b"changed-after-naming")
        with self.assertRaisesRegex(ReleaseError, "CRC32 filename mismatch"):
            collect_record(self.input_dir, self.context, self.manifest_reader)

    def test_other_versions_are_excluded_from_current_bundle(self) -> None:
        current = self.create_released_apk()
        foreign_temporary = self.input_dir / "foreign.tmp"
        self.create_fake_apk(foreign_temporary, "old-version")
        foreign = self.input_dir / (
            f"autojs6-plugin-pinyin-v1.2.2-universal-{crc32(foreign_temporary)}.apk"
        )
        foreign_temporary.rename(foreign)

        record, foreign_versions = collect_record(self.input_dir, self.context, self.manifest_reader)
        self.assertEqual(current, record.source)
        self.assertEqual([foreign], foreign_versions)

    def test_manifest_version_name_and_code_are_both_enforced(self) -> None:
        self.create_fake_apk(self.input_dir / "app-release.apk")
        with self.assertRaisesRegex(ReleaseError, "versionName mismatch"):
            collect_record(
                self.input_dir,
                self.context,
                lambda _: ApkManifestVersion("1.2.2", 27),
            )
        with self.assertRaisesRegex(ReleaseError, "versionCode mismatch"):
            collect_record(
                self.input_dir,
                self.context,
                lambda _: ApkManifestVersion("1.2.3", 26),
            )

    def test_overwrite_is_atomic_and_restricted_to_build_release(self) -> None:
        self.create_fake_apk(self.input_dir / "app-release.apk")
        record, _ = collect_record(self.input_dir, self.context, self.manifest_reader)
        output = self.root / "build" / "release" / "v1.2.3"
        create_bundle(self.context, record, output, signer_digest=None)
        (output / "stale.txt").write_text("stale", encoding="utf-8")

        create_bundle(self.context, record, output, signer_digest=None, overwrite=True)
        self.assertFalse((output / "stale.txt").exists())
        self.assertTrue((output / record.filename).is_file())

        with self.assertRaisesRegex(ReleaseError, "must be a child"):
            create_bundle(self.context, record, self.root / "outside", signer_digest=None)

    def test_apksigner_digest_parser_supports_legacy_and_scheme_labels(self) -> None:
        digest = "31a681fcfffb3e428420cae280ded89292b12a3b0f59e19b7a73e32a8ae4c213"
        self.assertEqual(
            digest.upper(),
            signer_digest_from_output(f"Signer #1 certificate SHA-256 digest: {digest}"),
        )
        self.assertEqual(
            digest.upper(),
            signer_digest_from_output(f"V2 Signer: certificate SHA-256 digest: {digest}"),
        )


if __name__ == "__main__":
    unittest.main()
