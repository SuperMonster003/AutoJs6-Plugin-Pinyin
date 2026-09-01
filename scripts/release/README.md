# Release tooling

`prepare_release.py` builds and prepares the single signed universal Pinyin APK as a verified release bundle.

## Normal release

Configure the untracked `sign.properties`, make sure the Android SDK provides `apkanalyzer` and `apksigner`, then run:

```text
py scripts/release/prepare_release.py
```

The command performs these steps:

1. Runs `:app:assembleRelease`.
2. Requires exactly one universal APK and rejects mixed or duplicate current-version packages.
3. Verifies the APK ZIP, required dictionaries, pure-JVM/no-native-library invariant, and manifest version name/code.
4. Verifies the APK signature and records the signer certificate SHA-256 digest.
5. Adds the version, `universal` variant and computed CRC32 to the output file name.
6. Copies the package atomically to `build/release/v<version>`.
7. Generates `SHA256SUMS.txt` and an English `RELEASE_NOTES.md` from `.changelog/lang_en.json`.

The command refuses unsigned or corrupt APKs, version drift, filename/content CRC mismatches, missing dictionaries, native libraries, malformed package names, and unsafe output paths.

To validate an existing signed APK without rebuilding, use `--skip-build --input <directory>`. APKs from other versions are excluded and reported. Use `--overwrite` to atomically replace an existing bundle under `build/release`.

## Tests

```text
py -m unittest discover -s scripts/release/tests -p "test_*.py"
```

The standard-library fixture suite covers the complete package path, missing/mixed/duplicate package rejection, native-library and asset rejection, CRC mismatch, version isolation, APK manifest version checks, atomic overwrite boundaries, checksums, and release-note generation.
