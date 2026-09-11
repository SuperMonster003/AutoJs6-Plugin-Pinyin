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

Pinyin 外掛 (Pinyin Plugin) 為 AutoJs6 提供離線漢語拼音轉換能力. 安裝後, 腳本可透過全域物件 `pinyin` 將中文文字轉換為多種風格的拼音, 支援多音字候選, 詞組詞典, Jieba 分詞與姓氏模式, 適用於排序, 檢索, 首字母索引, 注音標註等自動化場景.

外掛是一個獨立安裝的 APK, 執行於自身處理程序, 由 AutoJs6 透過外掛機制自動發現並以 AIDL 通訊. 單字, 詞組與分詞字典全部內建 (安裝套件約 6 MB), 轉換完全在裝置本地完成, 無需網路. 自 AutoJs6 v6.8.0 起, 主程式的 `pinyin` 模組由本外掛提供實作. API 設計對齊 JavaScript 生態廣泛使用的 [pinyin](https://github.com/hotoo/pinyin) 程式庫, 熟悉該程式庫的使用者可直接上手.

本外掛與 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) 互為姊妹外掛: 本外掛字典完備, 支援多音字與分詞, 適合追求讀音準確性的場景; Pinyin4j 基於經典 Java 程式庫 pinyin4j, 體積僅約 0.3 MB, 適合輕量逐字注音. 兩者可同時安裝, 詳見下方 `姊妹外掛對比`.

******

### 功能亮點

******

- 開箱即用: 安裝後由 AutoJs6 自動發現, 無需重啟主程式, 腳本直接使用全域物件 `pinyin`.
- 字典完備: 內建單字, 詞組與分詞三份字典及 HMM 模型, 完全離線, 不發起任何網路請求.
- 多音字支援: `heteronym` 選項回傳每個字的全部候選讀音, 詞組詞典自動選取常用讀音.
- Jieba 分詞: `segment` 選項啟用分詞, 按詞組消歧多音字, 提升整句注音準確率.
- 六種拼音風格: 聲調符號, 數字聲調, 數字緊隨韻母, 無聲調, 聲母, 首字母, 涵蓋排序/檢索/注音等場景.
- 專名模式: `SURNAME` 優先採用姓氏專用讀音; `PLACE_NAME` 先套用有來源可追溯的精選地名語料, 未命中再回退一般轉換.
- 結果可組合: `convert` 回傳的二維候選陣列附帶 `compact()` 方法, 一步展開全部讀音組合.
- 多語言: 外掛資訊, 使用說明, README 與更新日誌覆蓋 10 種語言.

******

### 使用方法

******

1. 將 AutoJs6 升級到內部版本號 3923 (6.7.1 Alpha4) 及以上; 自 v6.8.0 起拼音能力完全由外掛承擔, 建議直接使用最新版本.
2. 從 [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) 頁面下載外掛 APK 安裝到執行 AutoJs6 的裝置上, 或直接在 AutoJs6 的外掛中心線上安裝.
3. 開啟 AutoJs6 的外掛中心, 確認 `Pinyin` 外掛已被識別, 完成授權並處於啟用狀態.
4. 在腳本中直接呼叫 `pinyin` 全域物件, 參考下方 `快速上手` 範例; 也可先執行 `快速自檢` 確認外掛生效.

> 外掛僅提供一個通用安裝套件 (純 JVM 實作, 不區分 CPU 架構), 支援 Android 7.0 (API 24) 及以上的裝置. 外掛無獨立介面, 安裝後不在桌面建立圖示, 由 AutoJs6 統一發現與管理.

******

### 快速上手

******

基礎轉換: `convert` 回傳二維候選陣列, `simple` 回傳精簡字串:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

多音字: `heteronym` 選項回傳全部候選讀音, `compact()` 展開為讀音組合:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

分詞消歧, 姓氏模式與地名模式:

```javascript
console.log(pinyin.simple("音乐重要", false, true));
console.log(pinyin.convert("单田芳", { mode: "SURNAME" }));
console.log(pinyin.convert("六安", { mode: "PLACE_NAME" })); // [["lù"], ["ān"]]
console.log(pinyin.convert("六安", {
  customDictionary: { "六安": [["liú"], ["ān"]] },
})); // [["liú"], ["ān"]]
```

******

### 拼音風格

******

`style` 選項控制拼音輸出風格, 以 "中" (zhōng) 為例:

| 風格 | 輸出 | 說明 |
|---|---|---|
| `TONE` | `zhōng` | 聲調符號標註在韻母上 (預設) |
| `TONE2` | `zhong1` | 聲調以數字 0-4 附加在拼音末尾 |
| `TO3NE` | `zho1ng` | 聲調數字緊跟在韻母之後 |
| `NORMAL` | `zhong` | 不帶聲調 |
| `INITIALS` | `zh` | 僅回傳聲母 (零聲母字回傳空字串) |
| `FIRST_LETTER` | `z` | 僅回傳拼音首字母 |

`style` 取值不區分大小寫, 可傳字串 (如 `"TONE2"`) 或常數 (如 `pinyin.STYLE_TONE2`).

******

### 選項

******

`pinyin.convert(text, options)` 支援以下選項:

| 選項 | 預設值 | 說明 |
|---|---|---|
| `style` | `TONE` | 拼音風格, 見上方 `拼音風格` |
| `mode` | `NORMAL` | 轉換模式: `NORMAL` 一般模式, `SURNAME` 姓氏模式, `PLACE_NAME` 精選地名讀音模式 |
| `segment` | `false` | 啟用 Jieba 分詞, 借助詞組詞典消歧多音字 |
| `heteronym` | `false` | 回傳每個字的全部候選讀音, 而非僅首選讀音 |
| `group` | `false` | 按分詞得到的詞組合併拼音候選 (需搭配 `segment`) |
| `customDictionary` | `{}` | 目前呼叫的漢字讀音覆寫, 格式為 `{ 詞: [[帶調候選], ...] }`; 最長比對優先且不持久化, 需要相容的 AutoJs6 宿主與外掛 |

模式也可傳常數 (如 `pinyin.MODE_PLACE_NAME`). `PLACE_NAME` 對小規模人工複核語料執行最長匹配, 未收錄文字回退 `NORMAL`; 它並非全國標準地名全量庫, 涵蓋範圍與出處參見 [語料及來源](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/dictionaries/place-names.md).

******

### 腳本 API

******

`pinyin` 全域物件提供以下方法 (直接呼叫 `pinyin(text, options)` 等價於 `pinyin.convert`):

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

- `convert` 回傳二維陣列: 每個漢字或詞組字位佔一列, 列內為候選讀音; 未收錄字元與非中文字元原樣佔一列. 回傳陣列附帶 `compact()` 方法, 可展開為全部讀音組合.
- `simple` 回傳精簡字串: 每字取首選讀音直接串接; 第 2 參數為 `true` 時輸出數字聲調 (TONE2 風格), 否則不帶聲調; 第 3 參數為 `true` 時啟用分詞.
- `fromCodePoint` 查詢單字碼位在字典中的原始讀音記錄 (逗號分隔的帶調候選), 未收錄時回傳 `null`.
- `fromPhrase` 查詢詞組詞典, 回傳該詞組每個字位的候選讀音; 未收錄時回傳空陣列.
- 全部方法同步回傳; 首次呼叫需初始化內建字典, 可能稍有延遲.

#### Node.js

在 Node.js 執行環境中, 透過公開 `autojs6:bridge` facade 呼叫相同 provider, 並明確宣告 `pinyin` capability:

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

### 快速自檢

******

安裝並啟用外掛後, 執行以下單行腳本:

```javascript
console.log(pinyin.simple("拼音"));
```

輸出 `pinyin` 即表示外掛已正常運作.

******

### 常見問題

******

#### 如何確認外掛已經生效?

開啟 AutoJs6 的外掛中心, 能看到 `Pinyin` 外掛並處於啟用狀態即表示主程式已識別; 再執行上方 `快速自檢` 腳本, 輸出 `pinyin` 即為生效.

#### 腳本報錯提示缺少外掛或 `pinyin` 無法使用?

請確認 AutoJs6 內部版本號不低於 3923, 且外掛已在外掛中心完成安裝, 授權與啟用. 自 AutoJs6 v6.8.0 起, 主程式不再內建拼音實作, 拼音能力完全由本外掛承擔.

#### 為什麼應用程式清單和桌面上沒有外掛圖示?

這是正常現象. 外掛沒有獨立介面, 也不在桌面建立啟動圖示, 安裝後由 AutoJs6 在背景自動發現和呼叫, 全部互動都在 AutoJs6 內完成.

#### 多音字讀音不符合預期?

預設按單字首選讀音轉換. 建議開啟 `segment` 選項借助詞組詞典與分詞消歧 (如 `pinyin.simple(text, false, true)`); 需要全部候選時使用 `heteronym` 選項. 若常用詞讀音仍不正確, 歡迎透過 [Issues](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues) 回報以完善詞典.

#### 與姊妹外掛 Pinyin4j 如何選擇?

需要多音字, 分詞, 詞組或姓氏讀音時選擇本外掛; 只需輕量逐字注音且在意安裝套件體積時選擇 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j). 兩者互不衝突, 可同時安裝, 詳見下方 `姊妹外掛對比`.

#### 外掛會連網或申請敏感權限嗎?

不會. 全部字典內建於安裝套件, 轉換在裝置本地完成; 外掛資訊清單僅宣告與 AutoJs6 通訊所需的外掛權限, 不申請網路, 儲存空間等任何敏感系統權限.

#### 安裝套件為什麼有約 6 MB?

安裝套件內建單字字典, 詞組字典, 分詞詞庫與 HMM 模型四份資料, 以此換取完全離線與更高的注音準確率. 若更在意體積, 可考慮約 0.3 MB 的姊妹外掛 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j).

#### 為什麼 `customDictionary` 或 Node.js 拼音呼叫遭到拒絕?

這些路由需要相容的 AutoJs6 與 Pinyin 外掛版本. Node.js 呼叫必須宣告 `permissions: ["pinyin"]`. 自訂詞典僅對目前呼叫生效, 且必須符合文件中的項目數, 候選數, 組合數與 64 KiB 限制.

******

### 權限與安全

******

外掛在設計上盡可能收窄資料面與權限面:

- 最小權限: 外掛資訊清單僅宣告 AutoJs6 外掛權限 (`org.autojs.permission.PLUGIN`), 不申請網路, 儲存空間, 相機等任何敏感系統權限.
- 本地轉換: 待轉換文字僅經 Binder 在裝置內傳遞, 字典全部內建, 全程離線, 資料不出裝置.
- 簽章與授權: AutoJs6 會驗證外掛簽章, 外掛需在外掛中心授權並啟用後才能被腳本呼叫; 服務與喚醒入口均受外掛權限保護, 第三方應用程式無法直接呼叫.
- 開源可稽核: 外掛程式碼, 字典打包與文件產生鏈路全部開源.

請僅從官方 [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) 頁面或 AutoJs6 外掛中心取得外掛安裝套件; 來源不明的安裝套件即使名稱與版本號相同, 也可能被竄改.

******

### 姊妹外掛對比

******

AutoJs6 官方提供兩個拼音外掛, 各有側重, 可同時安裝:

| 對比項 | [Pinyin](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) | [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) |
|---|---|---|
| 底層實作 | 內建字典 + Jieba 分詞 | 經典 Java 程式庫 `pinyin4j` |
| 全域物件 | `pinyin` | `pinyin4j` |
| 多音字 | 支援, 可回傳全部候選 | 不支援, 固定取首個讀音 |
| 分詞與詞組 | 支援 (詞組詞典 + Jieba) | 不支援, 逐字轉換 |
| 姓氏模式 | 支援 | 不支援 |
| 輸出形式 | 二維候選陣列 (可 `compact()` 組合) 或精簡字串 | 字串, 可設定分隔符號 |
| 風格與格式 | 6 種拼音風格 | 3 種聲調格式 + 大小寫 + `ü` 表示方式 |
| 安裝套件體積 | 約 6 MB (內建字典) | 約 0.3 MB |
| 適用場景 | 讀音準確性優先: 多音字, 詞組, 人名 | 體積與簡單性優先: 快速逐字注音 |

兩個外掛互不依賴也互不衝突; 同時安裝後, 腳本可按需分別呼叫 `pinyin` 與 `pinyin4j`. Pinyin4j 外掛詳見 [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j).

******

### 外掛介面

******

以下資訊面向 AutoJs6 主程式與外掛開發者, 主程式透過這些識別碼發現外掛並完成能力協商:

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

`PinyinPluginService` 回應 `org.autojs.plugin.PINYIN` action (category `pinyin`), 透過 AIDL 介面 `IPinyinPlugin` 公開 5 個方法; `convert` 與 `fromPhrase` 以 JSON 字串回傳二維陣列, 選項經 `Bundle` 傳遞 (鍵: `mode` / `style` / `segment` / `heteronym` / `group` / `custom_dictionary_json`). 自訂詞典需要 `pinyin.customDictionary.v1` capability. 服務與 `WakeActivity` 均受 `org.autojs.permission.PLUGIN` 權限保護, 第三方應用程式無法直接呼叫.

******

### 開發路線圖

******

外掛的能力規劃與完成情況以可勾選清單維護在 ROADMAP.md 中, 按里程碑組織並附驗收條件, 涵蓋地名模式, 詞典演進, 自訂詞典, 效能最佳化與持續整合等方向. 未勾選條目表示規劃意向而非目前版本能力, 歡迎透過 Issues 參與討論.

- [檢視 ROADMAP.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/ROADMAP.md)

******

### 發行歷史

******

#### v1.0.1

_2026/09/11_

- `提示` 本版本僅改進文件與配套工程, 拼音轉換行為與全部腳本 API 保持不變
- `最佳化` 重構 10 種語言的 README: 新增使用方法, 快速上手, 拼音風格與選項速查表, 腳本 API, 快速自檢, 常見問題, 權限與安全, 姊妹外掛對比及外掛介面等章節
- `最佳化` 文件產生腳本升級為同族外掛統一實作: 支援 `--check` 漂移偵測, 跨語言鍵位與形狀對齊校驗, 全形符號攔截以及版本對齊校驗
- `最佳化` 外掛中心使用說明 (`plugin_instruction.md`) 納入同一套多語言 JSON 產生鏈路, 消除雙源維護
- `最佳化` 新增 ROADMAP.md 開發路線圖, 並與姊妹外掛 Pinyin4j 建立雙向互鏈與選型對比
- `最佳化` 統一 README 版式與 Gradle 平台版本管理方式
- `最佳化` 建置階段阻止意外引入原生相依套件, 並輸出 JSON 校驗報告

#### v1.0.0

_2026/07/15_

- `新增` Pinyin 外掛服務: 外掛 ID 為 `pinyin`, 由 AutoJs6 透過 `org.autojs.plugin.PINYIN` 自動發現並呼叫
- `新增` 拼音轉換 API: `pinyin.convert(text, options)` 回傳二維候選陣列並附帶 `compact()` 組合方法, `pinyin.simple(text)` 回傳精簡字串
- `新增` 字典查詢 API: `pinyin.fromCodePoint(codePoint)` 查詢單字讀音記錄, `pinyin.fromPhrase(phrase)` 查詢詞組讀音
- `新增` 六種拼音風格 (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) 與姓氏模式 (`SURNAME`)
- `新增` 多音字與分詞支援: 內建單字, 詞組, 分詞三份字典及 HMM 模型, 可按需啟用 `segment` / `heteronym` / `group` 選項
- `新增` 多語言資源: 外掛資訊與使用說明覆蓋 10 種語言
- `新增` README 與 CHANGELOG 由 JSON 來源檔與 `.python/generate_markdown.py` 產生多語言 Markdown

##### 更多發行歷史可參閱

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/assets/doc/CHANGELOG-zh-Hant-TW.md)

******

### 建置

******

本節面向希望從原始碼建置外掛的開發者.

建置 debug APK:

```powershell
.\gradlew.bat :app:assembleDebug
```

執行 JVM 單元測試並建置 instrumentation 測試 APK:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

建置 release APK (單一通用套件; 在不入庫的 `sign.properties` 中設定簽章後自動簽章):

```powershell
.\gradlew.bat :app:assembleRelease
```

一鍵建置並驗證已簽署的 universal APK, 產生 `SHA256SUMS.txt` 與以英文 CHANGELOG 為來源的 `RELEASE_NOTES.md`:

```powershell
py scripts\release\prepare_release.py
```

驗證多語言文件來源檔與產生產物是否同步 (持續整合也會執行):

```powershell
py .python\generate_markdown.py --check
```

建置參數集中於 `version.properties`: 最低 SDK 24 (Android 7.0), 目標 SDK 36, 目前版本 1.0.1.

******

### 在地化與文件產生

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

`strings.xml` 提供在地化外掛描述, `plugin_instruction.md` 提供主程式外掛中心展示的使用說明. README, 更新日誌與使用說明均由 JSON 來源產生: 修改 `.readme/` 與 `.changelog/` 下的來源檔後執行 `py .python/generate_markdown.py` 重新產生全部產物, 產生產物不手工編輯; 執行 `py .python/generate_markdown.py --check` 可校驗來源檔與產物是否同步.

******

### 授權

******

專案程式碼使用 [Mozilla Public License 2.0](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE). 內建分詞實作移植自 [jieba-analysis](https://github.com/huaban/jieba-analysis) 專案, API 設計對齊 [pinyin](https://github.com/hotoo/pinyin) 程式庫.

******

### 相關連結

******

- AutoJs6 Pinyin 文件: https://docs.autojs6.com/#/pinyin
- AutoJs6 專案: https://github.com/SuperMonster003/AutoJs6
- 姊妹外掛 Pinyin4j: https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j
- pinyin 程式庫 (API 設計參考): https://github.com/hotoo/pinyin
- jieba-analysis 專案: https://github.com/huaban/jieba-analysis


[16 KB page alignment and build verification](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/16kb.md)
