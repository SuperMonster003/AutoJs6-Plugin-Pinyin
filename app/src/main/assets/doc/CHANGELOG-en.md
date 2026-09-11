******

### Release history

******

# v1.0.1

###### 2026/09/11

* `Hint` This release only improves documentation and supporting tooling; Pinyin conversion behavior and every script API remain unchanged
* `Improved` Reworked the README in 10 languages: added sections for usage, quick start, Pinyin style and option reference tables, script API, self check, FAQ, permissions and security, sibling plugin comparison and plugin interface
* `Improved` Upgraded the docs generator to the unified implementation shared across sibling plugins: `--check` drift detection, cross-language key and shape validation, fullwidth symbol rejection and version alignment checks
* `Improved` Brought the Plugin Center instructions (`plugin_instruction.md`) into the same multilingual JSON generation pipeline, eliminating double-source maintenance
* `Improved` Added the ROADMAP.md development roadmap and established bidirectional cross-references and a comparison with the sibling plugin Pinyin4j
* `Improved` Standardize the README layout and Gradle platform version management
* `Improved` Build verification rejects accidental native dependencies and produces a JSON report

# v1.0.0

###### 2026/07/15

* `Added` Pinyin plugin service: plugin ID `pinyin`, automatically discovered and invoked by AutoJs6 via `org.autojs.plugin.PINYIN`
* `Added` Conversion API: `pinyin.convert(text, options)` returns a 2D candidate array carrying a `compact()` combination method, and `pinyin.simple(text)` returns a compact string
* `Added` Dictionary lookup API: `pinyin.fromCodePoint(codePoint)` queries the reading record of a single character and `pinyin.fromPhrase(phrase)` queries phrase readings
* `Added` Six Pinyin styles (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) plus the surname mode (`SURNAME`)
* `Added` Heteronym and segmentation support: bundled character, phrase and segmentation dictionaries plus an HMM model, with `segment` / `heteronym` / `group` options available on demand
* `Added` Multilingual resources: plugin info and instructions available in 10 languages
* `Added` README and CHANGELOG generated as multilingual Markdown from JSON sources via `.python/generate_markdown.py`
