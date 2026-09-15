******

### Release history

******

# v1.0.3

###### 2026/09/15

* `Improvement` Raise compileSdk and targetSdk to 37 (Android 17); the plugin's behavior does not depend on the new target

# v1.0.2

###### 2026/09/13

* `Fix` Keep the plugin version date in English regardless of the build machine locale
* `Improvement` Consistent localized resources, explicit plugin activation and validated release preparation

# v1.0.1

###### 2026/09/11

* `Hint` This release only improves documentation and supporting tooling; Pinyin conversion behavior and every script API remain unchanged
* `Improvement` Reworked the README in 10 languages: added sections for usage, quick start, Pinyin style and option reference tables, script API, self check, FAQ, permissions and security, sibling plugin comparison and plugin interface
* `Improvement` Upgraded the docs generator to the unified implementation shared across sibling plugins: `--check` drift detection, cross-language key and shape validation, fullwidth symbol rejection and version alignment checks
* `Improvement` Brought the Plugin Center instructions (`plugin_instruction.md`) into the same multilingual JSON generation pipeline, eliminating double-source maintenance
* `Improvement` Added the ROADMAP.md development roadmap and established bidirectional cross-references and a comparison with the sibling plugin Pinyin4j
* `Improvement` Standardize the README layout and Gradle platform version management
* `Improvement` Build verification rejects accidental native dependencies and produces a JSON report

# v1.0.0

###### 2026/07/15

* `Feature` Pinyin plugin service: plugin ID `pinyin`, automatically discovered and invoked by AutoJs6 via `org.autojs.plugin.PINYIN`
* `Feature` Conversion API: `pinyin.convert(text, options)` returns a 2D candidate array carrying a `compact()` combination method, and `pinyin.simple(text)` returns a compact string
* `Feature` Dictionary lookup API: `pinyin.fromCodePoint(codePoint)` queries the reading record of a single character and `pinyin.fromPhrase(phrase)` queries phrase readings
* `Feature` Six Pinyin styles (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) plus the surname mode (`SURNAME`)
* `Feature` Heteronym and segmentation support: bundled character, phrase and segmentation dictionaries plus an HMM model, with `segment` / `heteronym` / `group` options available on demand
* `Feature` Multilingual resources: plugin info and instructions available in 10 languages
* `Feature` README and CHANGELOG generated as multilingual Markdown from JSON sources via `.python/generate_markdown.py`
