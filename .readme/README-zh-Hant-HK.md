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
- 繁體中文 (香港) [zh-Hant-HK] # 目前
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
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

Pinyin 外掛 (Pinyin Plugin) 為 AutoJs6 提供離線漢語拼音轉換能力. 安裝後, 腳本可透過全局對象 `pinyin` 將中文文本轉換為多種風格的拼音, 支援多音字候選, 詞組詞典, Jieba 分詞與姓氏模式, 適用於排序, 檢索, 首字母索引, 注音標註等自動化場景.

外掛是一個獨立安裝的 APK, 運行於自身進程, 由 AutoJs6 透過外掛機制自動發現並以 AIDL 通信. 單字, 詞組與分詞字典全部內置 (安裝包約 6 MB), 轉換完全在設備本地完成, 無需網絡. 自 AutoJs6 v6.8.0 起, 宿主的 `pinyin` 模塊由本外掛提供實現. API 設計對齊 JavaScript 生態廣泛使用的 [pinyin](https://github.com/hotoo/pinyin) 庫, 熟悉該庫的用戶可直接上手.

本外掛與 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) 互為姊妹外掛: 本外掛字典完備, 支援多音字與分詞, 適合追求讀音準確性的場景; Pinyin4j 基於經典 Java 庫 pinyin4j, 體積僅約 0.3 MB, 適合輕量逐字注音. 兩者可同時安裝, 詳見下方 `姊妹外掛對比`.

******

### 功能亮點

******

- 開箱即用: 安裝後由 AutoJs6 自動發現, 無需重啟宿主, 腳本直接使用全局對象 `pinyin`.
- 字典完備: 內置單字, 詞組與分詞三份字典及 HMM 模型, 完全離線, 不發起任何網絡請求.
- 多音字支援: `heteronym` 選項返回每個字的全部候選讀音, 詞組詞典自動選取常用讀音.
- Jieba 分詞: `segment` 選項啟用分詞, 按詞組消歧多音字, 提升整句注音準確率.
- 六種拼音風格: 聲調符號, 數字聲調, 數字緊隨韻母, 無聲調, 聲母, 首字母, 覆蓋排序/檢索/注音等場景.
- 專名模式: `SURNAME` 優先採用姓氏專用讀音; `PLACE_NAME` 先套用有來源可追溯的精選地名語料, 未命中再回退普通轉換.
- 結果可組合: `convert` 返回的二維候選數組附帶 `compact()` 方法, 一步展開全部讀音組合.
- 多語言: 外掛資訊, 使用說明, README 與更新日誌覆蓋 10 種語言.

******

### 使用方法

******

1. 將 AutoJs6 升級到內部版本號 3923 (6.7.1 Alpha4) 及以上; 自 v6.8.0 起拼音能力完全由外掛承擔, 推薦直接使用最新版本.
2. 從 [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) 頁面下載外掛 APK 安裝到運行 AutoJs6 的設備上, 或直接在 AutoJs6 的外掛中心在線安裝.
3. 打開 AutoJs6 的外掛中心, 確認 `Pinyin` 外掛已被識別, 完成授權並處於啟用狀態.
4. 在腳本中直接調用 `pinyin` 全局對象, 參考下方 `快速上手` 示例; 也可先運行 `快速自檢` 確認外掛生效.

> 外掛僅提供一個通用安裝包 (純 JVM 實現, 不區分 CPU 架構), 支援 Android 7.0 (API 24) 及以上的設備. 外掛無獨立界面, 安裝後不在桌面創建圖標, 由 AutoJs6 統一發現與管理.

******

### 快速上手

******

基礎轉換: `convert` 返回二維候選數組, `simple` 返回緊湊字串:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

多音字: `heteronym` 選項返回全部候選讀音, `compact()` 展開為讀音組合:

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
| `INITIALS` | `zh` | 僅返回聲母 (零聲母字返回空字串) |
| `FIRST_LETTER` | `z` | 僅返回拼音首字母 |

`style` 取值不區分大小寫, 可傳字串 (如 `"TONE2"`) 或常量 (如 `pinyin.STYLE_TONE2`).

******

### 選項

******

`pinyin.convert(text, options)` 支援以下選項:

| 選項 | 預設值 | 說明 |
|---|---|---|
| `style` | `TONE` | 拼音風格, 見上方 `拼音風格` |
| `mode` | `NORMAL` | 轉換模式: `NORMAL` 普通模式, `SURNAME` 姓氏模式, `PLACE_NAME` 精選地名讀音模式 |
| `segment` | `false` | 啟用 Jieba 分詞, 借助詞組詞典消歧多音字 |
| `heteronym` | `false` | 返回每個字的全部候選讀音, 而非僅首選讀音 |
| `group` | `false` | 按分詞得到的詞組合併拼音候選 (需配合 `segment`) |
| `customDictionary` | `{}` | 當前調用的漢字讀音覆蓋, 格式為 `{ 詞: [[帶調候選], ...] }`; 最長匹配優先且不持久化, 需兼容的 AutoJs6 宿主與外掛 |

模式也可傳常量 (如 `pinyin.MODE_PLACE_NAME`). `PLACE_NAME` 對小規模人工複核語料執行最長匹配, 未收錄文字回退 `NORMAL`; 它並非全國標準地名全量庫, 覆蓋範圍與出處參見 [語料及來源](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/dictionaries/place-names.md).

******

### 腳本 API

******

`pinyin` 全局對象提供以下方法 (直接調用 `pinyin(text, options)` 等價於 `pinyin.convert`):

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

- `convert` 返回二維數組: 每個漢字或詞組字位佔一行, 行內為候選讀音; 未收錄字元與非中文字元原樣佔一行. 返回數組附帶 `compact()` 方法, 可展開為全部讀音組合.
- `simple` 返回緊湊字串: 每字取首選讀音直接拼接; 第 2 參數為 `true` 時輸出數字聲調 (TONE2 風格), 否則不帶聲調; 第 3 參數為 `true` 時啟用分詞.
- `fromCodePoint` 查詢單字碼點在字典中的原始讀音記錄 (逗號分隔的帶調候選), 未收錄時返回 `null`.
- `fromPhrase` 查詢詞組詞典, 返回該詞組每個字位的候選讀音; 未收錄時返回空數組.
- 全部方法同步返回; 首次調用需初始化內置字典, 可能稍有延遲.

#### Node.js

在 Node.js 運行時中, 透過公開 `autojs6:bridge` facade 調用同一 provider, 並明確聲明 `pinyin` capability:

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

安裝並啟用外掛後, 運行以下單行腳本:

```javascript
console.log(pinyin.simple("拼音"));
```

輸出 `pinyin` 即表示外掛已正常工作.

******

### 常見問題

******

#### 如何確認外掛已經生效?

打開 AutoJs6 的外掛中心, 能看到 `Pinyin` 外掛並處於啟用狀態即表示宿主已識別; 再運行上方 `快速自檢` 腳本, 輸出 `pinyin` 即為生效.

#### 腳本報錯提示缺少外掛或 `pinyin` 不可用?

請確認 AutoJs6 內部版本號不低於 3923, 且外掛已在外掛中心完成安裝, 授權與啟用. 自 AutoJs6 v6.8.0 起, 宿主不再內置拼音實現, 拼音能力完全由本外掛承擔.

#### 為什麼應用列表和桌面上沒有外掛圖標?

這是正常現象. 外掛沒有獨立界面, 也不在桌面創建啟動圖標, 安裝後由 AutoJs6 在後台自動發現和調用, 全部交互都在 AutoJs6 內完成.

#### 多音字讀音不符合預期?

預設按單字首選讀音轉換. 建議開啟 `segment` 選項借助詞組詞典與分詞消歧 (如 `pinyin.simple(text, false, true)`); 需要全部候選時使用 `heteronym` 選項. 若常用詞讀音仍不正確, 歡迎透過 [Issues](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues) 回報以完善詞典.

#### 與姊妹外掛 Pinyin4j 如何選擇?

需要多音字, 分詞, 詞組或姓氏讀音時選擇本外掛; 只需輕量逐字注音且在意安裝包體積時選擇 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j). 兩者互不衝突, 可同時安裝, 詳見下方 `姊妹外掛對比`.

#### 外掛會聯網或申請敏感權限嗎?

不會. 全部字典內置於安裝包, 轉換在設備本地完成; 外掛清單僅聲明與 AutoJs6 通信所需的外掛權限, 不申請網絡, 存儲等任何敏感系統權限.

#### 安裝包為什麼有約 6 MB?

安裝包內置單字字典, 詞組字典, 分詞詞庫與 HMM 模型四份數據, 以此換取完全離線與更高的注音準確率. 若更在意體積, 可考慮約 0.3 MB 的姊妹外掛 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j).

#### 為甚麼 `customDictionary` 或 Node.js 拼音調用被拒絕?

這些路由要求兼容的 AutoJs6 與 Pinyin 外掛版本. Node.js 調用必須聲明 `permissions: ["pinyin"]`. 自訂詞典僅對當前調用生效, 且必須符合文檔中的條目數, 候選數, 組合數與 64 KiB 限制.

******

### 權限與安全

******

外掛在設計上盡可能收窄數據面與權限面:

- 最小權限: 外掛清單僅聲明 AutoJs6 外掛權限 (`org.autojs.permission.PLUGIN`), 不申請網絡, 存儲, 相機等任何敏感系統權限.
- 本地轉換: 待轉換文本僅經 Binder 在設備內傳遞, 字典全部內置, 全程離線, 數據不出設備.
- 簽名與授權: AutoJs6 會校驗外掛簽名, 外掛需在外掛中心授權並啟用後才能被腳本調用; 服務與喚醒入口均受外掛權限保護, 第三方應用無法直接調用.
- 開源可審計: 外掛代碼, 字典打包與文檔生成鏈路全部開源.

請僅從官方 [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) 頁面或 AutoJs6 外掛中心獲取外掛安裝包; 來源不明的安裝包即使名稱與版本號相同, 也可能被篡改.

******

### 姊妹外掛對比

******

AutoJs6 官方提供兩個拼音外掛, 各有側重, 可同時安裝:

| 對比項 | [Pinyin](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) | [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) |
|---|---|---|
| 底層實現 | 內置字典 + Jieba 分詞 | 經典 Java 庫 `pinyin4j` |
| 全局對象 | `pinyin` | `pinyin4j` |
| 多音字 | 支援, 可返回全部候選 | 不支援, 固定取首個讀音 |
| 分詞與詞組 | 支援 (詞組詞典 + Jieba) | 不支援, 逐字轉換 |
| 姓氏模式 | 支援 | 不支援 |
| 輸出形式 | 二維候選數組 (可 `compact()` 組合) 或緊湊字串 | 字串, 可配置分隔符 |
| 風格與格式 | 6 種拼音風格 | 3 種聲調格式 + 大小寫 + `ü` 表示方式 |
| 安裝包體積 | 約 6 MB (內置字典) | 約 0.3 MB |
| 適用場景 | 讀音準確性優先: 多音字, 詞組, 人名 | 體積與簡單性優先: 快速逐字注音 |

兩個外掛互不依賴也互不衝突; 同時安裝後, 腳本可按需分別調用 `pinyin` 與 `pinyin4j`. Pinyin4j 外掛詳見 [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j).

******

### 外掛接口

******

以下資訊面向 AutoJs6 宿主與外掛開發者, 宿主透過這些標識發現外掛並完成能力協商:

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

`PinyinPluginService` 響應 `org.autojs.plugin.PINYIN` action (category `pinyin`), 透過 AIDL 接口 `IPinyinPlugin` 暴露 5 個方法; `convert` 與 `fromPhrase` 以 JSON 字串返回二維數組, 選項經 `Bundle` 傳遞 (鍵: `mode` / `style` / `segment` / `heteronym` / `group` / `custom_dictionary_json`). 自訂詞典要求 `pinyin.customDictionary.v1` capability. 服務與 `WakeActivity` 均受 `org.autojs.permission.PLUGIN` 權限保護, 第三方應用無法直接調用.

******

### 開發路線圖

******

外掛的能力規劃與完成情況以可勾選清單維護在 ROADMAP.md 中, 按里程碑組織並附驗收條件, 涵蓋地名模式, 詞典演進, 自定義詞典, 效能優化與持續集成等方向. 未勾選條目表示規劃意向而非目前版本能力, 歡迎透過 Issues 參與討論.

- [查看 ROADMAP.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/ROADMAP.md)

******

### 發行歷史

******

#### v1.0.3

_2026/09/15_

- `優化` 將 compileSdk 與 targetSdk 提升到 37 (Android 17), 插件行為不受新目標版本影響

#### v1.0.2

_2026/09/13_

- `修復` 外掛版本日期固定使用英文, 不隨建置機器的語言變化
- `優化` 統一多語言資源, 明確插件啟用契約並驗證發佈產物

#### v1.0.1

_2026/09/11_

- `提示` 本版本僅改進文檔與配套工程, 拼音轉換行為與全部腳本 API 保持不變
- `優化` 重構 10 種語言的 README: 新增使用方法, 快速上手, 拼音風格與選項速查表, 腳本 API, 快速自檢, 常見問題, 權限與安全, 姊妹外掛對比及外掛接口等章節
- `優化` 文檔生成腳本升級為同族外掛統一實現: 支援 `--check` 漂移檢測, 跨語言鍵位與形狀對齊校驗, 全形符號攔截以及版本對齊校驗
- `優化` 外掛中心使用說明 (`plugin_instruction.md`) 納入同一套多語言 JSON 生成鏈路, 消除雙源維護
- `優化` 新增 ROADMAP.md 開發路線圖, 並與姊妹外掛 Pinyin4j 建立雙向互鏈與選型對比
- `優化` 統一 README 版式與 Gradle 平台版本管理方式
- `優化` 建置階段阻止意外引入原生相依套件, 並輸出 JSON 校驗報告

##### 更多發行歷史可參閱

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/assets/doc/CHANGELOG-zh-Hant-HK.md)

******

### 構建

******

本節面向希望從源碼構建外掛的開發者.

構建 debug APK:

```powershell
.\gradlew.bat :app:assembleDebug
```

運行 JVM 單元測試並構建 instrumentation 測試 APK:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

構建 release APK (單一通用包; 在不入庫的 `sign.properties` 中配置簽名後自動簽名):

```powershell
.\gradlew.bat :app:assembleRelease
```

一鍵構建並校驗已簽名的 universal APK, 生成 `SHA256SUMS.txt` 與基於英文 CHANGELOG 的 `RELEASE_NOTES.md`:

```powershell
py scripts\release\prepare_release.py
```

校驗多語言文件源與生成產物是否同步 (持續整合亦會執行):

```powershell
py .python\generate_markdown.py --check
```

構建參數集中於 `version.properties`: 最低 SDK 24 (Android 7.0), 目標 SDK 37, 目前版本 1.0.3.

******

### 本地化與文檔生成

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

`strings.xml` 提供本地化外掛描述, `plugin_instruction.md` 提供宿主外掛中心展示的使用說明. README, 更新日誌與使用說明均由 JSON 源生成: 修改 `.readme/` 與 `.changelog/` 下的源文件後運行 `py .python/generate_markdown.py` 重新生成全部產物, 生成產物不手工編輯; 運行 `py .python/generate_markdown.py --check` 可校驗源文件與產物是否同步.

******

### 許可

******

項目代碼使用 [Mozilla Public License 2.0](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE). 內置分詞實現移植自 [jieba-analysis](https://github.com/huaban/jieba-analysis) 項目, API 設計對齊 [pinyin](https://github.com/hotoo/pinyin) 庫.

******

### 相關連結

******

- AutoJs6 Pinyin 文檔: https://docs.autojs6.com/#/pinyin
- AutoJs6 項目: https://github.com/SuperMonster003/AutoJs6
- 姊妹外掛 Pinyin4j: https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j
- pinyin 庫 (API 設計參考): https://github.com/hotoo/pinyin
- jieba-analysis 項目: https://github.com/huaban/jieba-analysis


[16 KB page alignment and build verification](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/16kb.md)
