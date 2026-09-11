<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>Pinyin plugin for Chinese pronunciation conversion</p>

  <p>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/SuperMonster003/AutoJs6-Plugin-Pinyin?label=Release"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues/SuperMonster003/AutoJs6-Plugin-Pinyin?color=A24232&label=Issues"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/SuperMonster003/AutoJs6-Plugin-Pinyin?color=534BAE&label=License"/></a>
  </p>
</div>

******

### Languages

******

The README.md file is currently available in the following languages:

- [简体中文 [zh-Hans]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hans.md)
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
- English [en] # current
- [Français [fr]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-fr.md)
- [Español [es]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-es.md)
- [日本語 [ja]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ja.md)
- [한국어 [ko]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ko.md)
- [Русский [ru]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ru.md)
- [العربية [ar]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ar.md)

******

### Introduction

******

The Pinyin Plugin provides AutoJs6 with offline Chinese-to-Pinyin conversion. Once installed, scripts can use the global `pinyin` object to convert Chinese text into Pinyin in multiple styles, with support for heteronym candidates, a phrase dictionary, Jieba word segmentation and a surname mode, making it useful for sorting, searching, initial-letter indexing, phonetic annotation and other automation scenarios.

The plugin ships as a standalone APK running in its own process; AutoJs6 discovers it automatically through the plugin mechanism and communicates with it via AIDL. The character, phrase and segmentation dictionaries are all bundled (the APK is about 6 MB), so conversion happens entirely on-device with no network access. Since AutoJs6 v6.8.0, the host `pinyin` module is backed by this plugin. The API design follows the widely used JavaScript [pinyin](https://github.com/hotoo/pinyin) library, so users familiar with it can get started right away.

This plugin and [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) are sibling plugins: this one ships full dictionaries with heteronym and segmentation support for accuracy-first scenarios, while Pinyin4j wraps the classic Java library pinyin4j in a package of only about 0.3 MB for lightweight per-character conversion. Both can be installed side by side; see `Sibling plugin comparison` below.

******

### Features

******

- Works out of the box: discovered by AutoJs6 automatically after installation, no host restart required, scripts use the global `pinyin` object directly.
- Complete dictionaries: bundled character, phrase and segmentation dictionaries plus an HMM model, fully offline with no network requests.
- Heteronym support: the `heteronym` option returns every candidate pronunciation of each character, while the phrase dictionary picks common readings automatically.
- Jieba segmentation: the `segment` option enables word segmentation to disambiguate heteronyms by phrase, improving whole-sentence accuracy.
- Six Pinyin styles: tone marks, tone numbers, tone numbers after finals, plain, initials and first letters, covering sorting, searching and annotation scenarios.
- Dedicated name modes: `SURNAME` prefers surname-specific readings, while `PLACE_NAME` applies a curated, source-traceable place-name corpus before falling back to normal conversion.
- Composable results: the 2D candidate array returned by `convert` carries a `compact()` method that expands all pronunciation combinations in one step.
- Multilingual: plugin info, instructions, README and changelog are available in 10 languages.

******

### Usage

******

1. Upgrade AutoJs6 to internal build 3923 (6.7.1 Alpha4) or later; since v6.8.0 Pinyin conversion is fully delegated to plugins, so the latest version is recommended.
2. Download the plugin APK from the [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) page and install it on the device running AutoJs6, or install it online right inside the AutoJs6 Plugin Center.
3. Open the AutoJs6 Plugin Center and make sure the `Pinyin` plugin is recognized, authorized and enabled.
4. Call the global `pinyin` object in your scripts as shown in `Quick start` below; you may also run the `Self check` first to confirm the plugin works.

> The plugin ships as a single universal APK (pure JVM implementation, no CPU architecture variants) and supports devices running Android 7.0 (API 24) or later. It has no standalone UI and creates no launcher icon; AutoJs6 discovers and manages it automatically.

******

### Quick start

******

Basic conversion: `convert` returns a 2D candidate array, `simple` returns a compact string:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

Heteronyms: the `heteronym` option returns all candidate readings and `compact()` expands the combinations:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

Segmentation-based disambiguation, surname mode and place-name mode:

```javascript
console.log(pinyin.simple("音乐重要", false, true));
console.log(pinyin.convert("单田芳", { mode: "SURNAME" }));
console.log(pinyin.convert("六安", { mode: "PLACE_NAME" })); // [["lù"], ["ān"]]
console.log(pinyin.convert("六安", {
  customDictionary: { "六安": [["liú"], ["ān"]] },
})); // [["liú"], ["ān"]]
```

******

### Pinyin styles

******

The `style` option controls the output style, illustrated with "中" (zhōng):

| Style | Output | Description |
|---|---|---|
| `TONE` | `zhōng` | Tone marks placed on finals (default) |
| `TONE2` | `zhong1` | Tone digit 0-4 appended to the syllable |
| `TO3NE` | `zho1ng` | Tone digit placed right after the final |
| `NORMAL` | `zhong` | No tones |
| `INITIALS` | `zh` | Initial consonant only (empty string for zero-initial syllables) |
| `FIRST_LETTER` | `z` | First letter of the syllable only |

The `style` value is case-insensitive and accepts either a string (such as `"TONE2"`) or a constant (such as `pinyin.STYLE_TONE2`).

******

### Options

******

`pinyin.convert(text, options)` supports the following options:

| Option | Default | Description |
|---|---|---|
| `style` | `TONE` | Pinyin style, see `Pinyin styles` above |
| `mode` | `NORMAL` | Conversion mode: `NORMAL` for regular text, `SURNAME` for surname readings, `PLACE_NAME` for curated place-name readings |
| `segment` | `false` | Enable Jieba segmentation and use the phrase dictionary to disambiguate heteronyms |
| `heteronym` | `false` | Return all candidate pronunciations of each character instead of the first one only |
| `group` | `false` | Merge Pinyin candidates by segmented words (use together with `segment`) |
| `customDictionary` | `{}` | Per-call Han reading overrides as `{ phrase: [[tone-marked candidates], ...] }`; longest matches win, the data is not persisted, and a compatible AutoJs6 host and plugin are required |

Modes also accept constants (such as `pinyin.MODE_PLACE_NAME`). `PLACE_NAME` uses longest matching against a small, manually reviewed corpus; text not covered by it falls back to `NORMAL`. This is not a complete national gazetteer; see the [corpus and sources](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/dictionaries/place-names.md).

******

### Script API

******

The global `pinyin` object provides the following methods (calling `pinyin(text, options)` directly is equivalent to `pinyin.convert`):

```text
pinyin(text, options?)                   -> string[][]
pinyin.convert(text, options?)           -> string[][]
pinyin.simple(text, numeric?, segment?)  -> string
pinyin.compare(textA, textB)             -> number
pinyin.compact(matrix)                   -> string[][]
pinyin.fromCodePoint(codePoint)          -> string | null
pinyin.fromPhrase(phrase)                -> string[][]
pinyin.STYLE_* / pinyin.MODE_*           -> constants
```

- `convert` returns a 2D array: each Chinese character or phrase slot occupies one row holding its candidate readings; unknown and non-Chinese characters keep one row as-is. The returned array carries a `compact()` method that expands all pronunciation combinations.
- `simple` returns a compact string: the first reading of each character is concatenated; pass `true` as the 2nd argument for numeric tones (TONE2 style, plain otherwise) and `true` as the 3rd argument to enable segmentation.
- `fromCodePoint` looks up the raw dictionary record of a single code point (comma-separated tone-marked candidates) and returns `null` when it is not covered.
- `fromPhrase` looks up the phrase dictionary and returns the candidate readings of each character slot of the phrase; an empty array is returned when it is not covered.
- All methods return synchronously; the very first call initializes the bundled dictionaries and may take slightly longer.

#### Node.js

In the Node.js runtime, call the same provider through the public `autojs6:bridge` facade and explicitly declare the `pinyin` capability:

```javascript
const { callAutoJs } = require("autojs6:bridge");

(async () => {
  const result = await callAutoJs(
    "pinyin",
    "convert",
    ["中心", { style: "TONE2" }],
    { permissions: ["pinyin"] },
  );
  console.log(result); // [["zhong1"], ["xin1"]]
})();
```

******

### Self check

******

After installing and enabling the plugin, run this one-liner:

```javascript
console.log(pinyin.simple("拼音"));
```

An output of `pinyin` means the plugin is working properly.

******

### FAQ

******

#### How do I confirm the plugin is active?

Open the AutoJs6 Plugin Center: seeing the `Pinyin` plugin listed and enabled means the host has recognized it. Then run the `Self check` script above; an output of `pinyin` confirms it works.

#### My script reports a missing plugin or `pinyin` being unavailable?

Make sure the AutoJs6 internal build is at least 3923 and the plugin has been installed, authorized and enabled in the Plugin Center. Since AutoJs6 v6.8.0 the host no longer bundles a Pinyin implementation, so all Pinyin conversion is delegated to this plugin.

#### Why is there no icon in the app list or on the home screen?

This is expected. The plugin has no standalone UI and creates no launcher icon; after installation AutoJs6 discovers and invokes it in the background, and all interaction happens inside AutoJs6.

#### A heteronym is not converted the way I expect?

By default the first reading of each single character is used. Enable the `segment` option to disambiguate via the phrase dictionary and segmentation (for example `pinyin.simple(text, false, true)`), or use the `heteronym` option to get all candidates. If a common word still reads wrong, please report it via [Issues](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues) so the dictionaries can be improved.

#### How do I choose between this plugin and its sibling Pinyin4j?

Choose this plugin when you need heteronyms, segmentation, phrases or surname readings; choose [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) when you only need lightweight per-character conversion and care about APK size. They do not conflict and can be installed together; see `Sibling plugin comparison` below.

#### Does the plugin access the network or request sensitive permissions?

No. All dictionaries are bundled inside the APK and conversion happens on-device; the manifest only declares the plugin permission required to communicate with AutoJs6, without any network, storage or other sensitive system permissions.

#### Why is the APK about 6 MB?

The APK bundles four data sets: a character dictionary, a phrase dictionary, a segmentation lexicon and an HMM model, trading size for full offline operation and higher accuracy. If size matters more to you, consider the sibling plugin [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) at about 0.3 MB.

#### Why is `customDictionary` or a Node.js Pinyin call rejected?

These routes require compatible AutoJs6 and Pinyin plugin builds. Node.js calls must declare `permissions: ["pinyin"]`. A custom dictionary is scoped to one call and must remain within the documented entry, candidate, combination and 64 KiB limits.

******

### Permissions and security

******

The plugin is designed to keep both its data surface and permission surface minimal:

- Minimal permissions: the manifest only declares the AutoJs6 plugin permission (`org.autojs.permission.PLUGIN`), with no network, storage, camera or other sensitive system permissions.
- On-device conversion: text travels only across Binder within the device, dictionaries are fully bundled, everything stays offline and no data leaves the device.
- Signature and authorization: AutoJs6 verifies the plugin signature, and the plugin must be authorized and enabled in the Plugin Center before scripts can call it; the service and wake entry are protected by the plugin permission, so third-party apps cannot invoke them directly.
- Open source and auditable: the plugin code, dictionary packaging and documentation pipeline are fully open source.

Only obtain the plugin APK from the official [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) page or the AutoJs6 Plugin Center; an APK from an unknown source may be tampered with even if its name and version look identical.

******

### Sibling plugin comparison

******

AutoJs6 offers two official Pinyin plugins with different focuses, and they can be installed side by side:

| Aspect | [Pinyin](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) | [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) |
|---|---|---|
| Underlying implementation | Bundled dictionaries + Jieba segmentation | Classic Java library `pinyin4j` |
| Global object | `pinyin` | `pinyin4j` |
| Heteronyms | Supported, all candidates available | Not supported, first reading only |
| Segmentation and phrases | Supported (phrase dictionary + Jieba) | Not supported, per-character conversion |
| Surname mode | Supported | Not supported |
| Output form | 2D candidate array (composable via `compact()`) or compact string | String with a configurable separator |
| Styles and formats | 6 Pinyin styles | 3 tone formats + letter case + `ü` representation |
| APK size | About 6 MB (bundled dictionaries) | About 0.3 MB |
| Best for | Accuracy first: heteronyms, phrases, person names | Size and simplicity first: quick per-character conversion |

The two plugins neither depend on nor conflict with each other; once both are installed, scripts can call `pinyin` and `pinyin4j` as needed. See [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) for details.

******

### Plugin interface

******

The following information targets AutoJs6 host and plugin developers; the host uses these identifiers to discover the plugin and negotiate capabilities:

```text
application id: io.github.supermonster003.autojs6.plugin.pinyin
plugin id: pinyin
engine: pinyin
variant: default
discovery action: org.autojs.plugin.PINYIN
discovery category: pinyin
wake action: org.autojs.plugin.action.WAKE
binder interface: IPinyinPlugin
binder methods: getInfo / convert / simple / fromCodePoint / fromPhrase
minimum host build: 3923
native library: none (pure JVM, all ABIs)
```

`PinyinPluginService` responds to the `org.autojs.plugin.PINYIN` action (category `pinyin`) and exposes 5 methods through the AIDL interface `IPinyinPlugin`; `convert` and `fromPhrase` return 2D arrays as JSON strings, and options travel in a `Bundle` (keys: `mode` / `style` / `segment` / `heteronym` / `group` / `custom_dictionary_json`). Custom dictionaries require the `pinyin.customDictionary.v1` capability. Both the service and `WakeActivity` are protected by the `org.autojs.permission.PLUGIN` permission, so third-party apps cannot invoke them directly.

******

### Roadmap

******

The plugin capability plan and its progress are maintained as a checkable list in ROADMAP.md, organized by milestones with acceptance criteria, covering place-name mode, dictionary evolution, custom dictionaries, performance and continuous integration. Unchecked items express intent rather than current capabilities; feel free to join the discussion via Issues.

- [View ROADMAP.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/ROADMAP.md)

******

### Release history

******

#### v1.0.1

_2026/09/11_

- `Hint` This release only improves documentation and supporting tooling; Pinyin conversion behavior and every script API remain unchanged
- `Improved` Reworked the README in 10 languages: added sections for usage, quick start, Pinyin style and option reference tables, script API, self check, FAQ, permissions and security, sibling plugin comparison and plugin interface
- `Improved` Upgraded the docs generator to the unified implementation shared across sibling plugins: `--check` drift detection, cross-language key and shape validation, fullwidth symbol rejection and version alignment checks
- `Improved` Brought the Plugin Center instructions (`plugin_instruction.md`) into the same multilingual JSON generation pipeline, eliminating double-source maintenance
- `Improved` Added the ROADMAP.md development roadmap and established bidirectional cross-references and a comparison with the sibling plugin Pinyin4j
- `Improved` Standardize the README layout and Gradle platform version management
- `Improved` Build verification rejects accidental native dependencies and produces a JSON report

#### v1.0.0

_2026/07/15_

- `Added` Pinyin plugin service: plugin ID `pinyin`, automatically discovered and invoked by AutoJs6 via `org.autojs.plugin.PINYIN`
- `Added` Conversion API: `pinyin.convert(text, options)` returns a 2D candidate array carrying a `compact()` combination method, and `pinyin.simple(text)` returns a compact string
- `Added` Dictionary lookup API: `pinyin.fromCodePoint(codePoint)` queries the reading record of a single character and `pinyin.fromPhrase(phrase)` queries phrase readings
- `Added` Six Pinyin styles (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) plus the surname mode (`SURNAME`)
- `Added` Heteronym and segmentation support: bundled character, phrase and segmentation dictionaries plus an HMM model, with `segment` / `heteronym` / `group` options available on demand
- `Added` Multilingual resources: plugin info and instructions available in 10 languages
- `Added` README and CHANGELOG generated as multilingual Markdown from JSON sources via `.python/generate_markdown.py`

##### For more release history, refer to

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/assets/doc/CHANGELOG-en.md)

******

### Build

******

This section targets developers who want to build the plugin from source.

Build a debug APK:

```powershell
.\gradlew.bat :app:assembleDebug
```

Run JVM unit tests and build the instrumentation test APK:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

Build a release APK (a single universal package; signing happens automatically once the untracked `sign.properties` is configured):

```powershell
.\gradlew.bat :app:assembleRelease
```

Build and verify the signed universal APK in one command, then generate `SHA256SUMS.txt` and `RELEASE_NOTES.md` from the English CHANGELOG:

```powershell
py scripts\release\prepare_release.py
```

Verify that the multilingual documentation sources and generated artifacts are in sync (also enforced by CI):

```powershell
py .python\generate_markdown.py --check
```

Build parameters are centralized in `version.properties`: minimum SDK 24 (Android 7.0), target SDK 36, current version 1.0.1.

******

### Localization and docs generation

******

```text
.readme/common.json
.readme/lang_*.json
.readme/template_readme.md
.readme/template_plugin_instruction.md
.changelog/lang_*.json
.changelog/template_changelog.md
.python/generate_markdown.py
app/src/main/assets/doc/CHANGELOG-*.md
app/src/main/res/values-*/strings.xml
app/src/main/res/raw-*/plugin_instruction.md
```

`strings.xml` provides the localized plugin description, and `plugin_instruction.md` provides the usage instructions shown in the host Plugin Center. The README, changelog and instructions are all generated from JSON sources: after editing the sources under `.readme/` and `.changelog/`, run `py .python/generate_markdown.py` to regenerate every artifact (never edit generated files by hand); run `py .python/generate_markdown.py --check` to verify that sources and artifacts are in sync.

******

### License

******

The project code is licensed under [Mozilla Public License 2.0](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE). The bundled segmentation implementation is ported from the [jieba-analysis](https://github.com/huaban/jieba-analysis) project, and the API design follows the [pinyin](https://github.com/hotoo/pinyin) library.

******

### Related links

******

- AutoJs6 Pinyin documentation: https://docs.autojs6.com/#/pinyin
- AutoJs6 project: https://github.com/SuperMonster003/AutoJs6
- Sibling plugin Pinyin4j: https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j
- pinyin library (API design reference): https://github.com/hotoo/pinyin
- jieba-analysis project: https://github.com/huaban/jieba-analysis


[16 KB page alignment and build verification](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/16kb.md)
