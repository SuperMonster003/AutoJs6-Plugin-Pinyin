<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>用於漢語拼音轉換的 Pinyin 外掛</p>

  <p>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/SuperMonster003/AutoJs6-Plugin-Pinyin?label=Release"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues/SuperMonster003/AutoJs6-Plugin-Pinyin?color=A24232&label=Issues"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/commit/f21dd3191be1cb0c07d5cadf7478c29064e409c1"><img alt="Created" src="https://img.shields.io/date/1783230112?color=2e7d32&label=Created"/></a>
    <br>
    <a href="https://developer.android.com/studio/archive"><img alt="Android Studio" src="https://img.shields.io/badge/Android%20Studio-2023.3+-B64FC8"/></a>
    <a href="https://www.jetbrains.com/idea/download/other.html"><img alt="IntelliJ IDEA" src="https://img.shields.io/badge/IntelliJ%20IDEA-2023.3+-EE4677"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/SuperMonster003/AutoJs6-Plugin-Pinyin?color=534BAE&label=License"/></a>
  </p>
</div>

******

### 語言 (Languages)

******

目前 README.md 支援以下語言:

- [简体中文 [zh-Hans]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hans.md)
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- 繁體中文 (台灣) [zh-Hant-TW] # 目前
- [English [en]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-en.md)
- [Français [fr]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-fr.md)
- [Español [es]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-es.md)
- [日本語 [ja]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ja.md)
- [한국어 [ko]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ko.md)
- [Русский [ru]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ru.md)
- [العربية [ar]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ar.md)

******

### 簡介

******

AutoJs6 Pinyin 外掛為 AutoJs6 提供基於內建漢字, 詞組和分詞字典的漢語拼音轉換能力, 支援聲調符號, 數字聲調, 無聲調, 聲母, 首字母, 分詞, 多音字, 詞組和姓氏模式.

******

### 功能

******

- 提供 `pinyin` 外掛服務, 外掛 ID 為 `pinyin`.
- 支援 AutoJs6 中的 `pinyin.convert(text, options)`, `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)` 和 `pinyin.fromPhrase(phrase)`.
- 支援 `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` 拼音風格, 支援普通模式和姓氏模式.
- 支援基於 Jieba 的分詞, 多音字, 詞組字典和拼音結果組合.
- 外掛資訊, 使用說明, README 與 CHANGELOG 均支援西班牙語/法語/俄語/阿拉伯語/日語/韓語/英語/簡體中文/香港繁體/台灣繁體.

******

### 使用範例

******

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

也可以使用緊湊字串方法:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

******

### 選項

******

常用拼音風格包括:

```text
NORMAL, TONE, TONE2, TO3NE,
INITIALS, FIRST_LETTER
```

模式包括:

```text
NORMAL, SURNAME, PLACE_NAME, PLACENAME
```

******

### 發行歷史

******

# v1.0.0

###### 2026/07/15

* `新增` Pinyin 外掛服務, 外掛 ID 為 `pinyin`, 引擎為 `pinyin`
* `新增` 支援透過 `org.autojs.plugin.PINYIN` 探索並呼叫外掛
* `新增` 支援 `pinyin.convert(text, options)` 回傳二維拼音結果, 並由 AutoJs6 宿主提供 `compact()` 組合方法
* `新增` 支援 `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)` 和 `pinyin.fromPhrase(phrase)`
* `新增` 支援 `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` 拼音風格以及 `NORMAL`/`SURNAME`/`PLACE_NAME` 模式
* `新增` 內建漢字, 詞組和分詞資料, 支援分詞, 多音字, 詞組和姓氏拼音處理
* `新增` 外掛資訊和使用說明的多語言資源: 西班牙語/法語/俄語/阿拉伯語/日語/韓語/英語/簡體中文/香港繁體/台灣繁體
* `新增` README 與 CHANGELOG 使用 JSON 來源檔和 `.python/generate_markdown.py` 生成多語言 Markdown

##### 更多發行歷史可參閱

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.changelog/CHANGELOG-zh-Hant-TW.md)

******

### 建置

******

```powershell
.\gradlew.bat :app:assembleDebug
```

Release 建置:

```powershell
.\gradlew.bat :app:assembleRelease
```

建置參數來自 `version.properties`, 目前最低 SDK 為 24, 目標 SDK 為 36.

******

### 資源結構

******

```text
.readme/lang_*.json
.changelog/lang_*.json
.python/generate_markdown.py
app/src/main/res/values-*/strings.xml
app/src/main/res/raw-*/plugin_instruction.md
```

`strings.xml` 提供外掛描述本地化; `plugin_instruction.md` 提供宿主端顯示的外掛使用說明. README 與 CHANGELOG 由 `.python/generate_markdown.py` 根據 JSON 來源檔生成.

******

### 相關連結

******

- AutoJs6 Pinyin 文件: https://docs.autojs6.com/#/pinyin
- AutoJs6 專案: https://github.com/SuperMonster003/AutoJs6
