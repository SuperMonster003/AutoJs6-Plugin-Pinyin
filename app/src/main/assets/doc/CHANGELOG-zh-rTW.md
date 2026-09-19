******

### 發行歷史

******

# v1.0.3

###### 2026/09/19

* `修復` AGP 9.1 建置時的 SDK XML v4 解析警告及 JVM 單元測試組裝工作誤觸發 APK 原生程式庫對齊檢查的問題 (共用建置外掛 1.8.3)
* `優化` 將 compileSdk 與 targetSdk 提升到 37 (Android 17), 外掛程式行為不受新目標版本影響

# v1.0.2

###### 2026/09/13

* `修復` 外掛版本日期固定使用英文, 不隨建置機器的語言變化
* `優化` 統一多語言資源, 明確外掛啟用契約並驗證發行產物

# v1.0.1

###### 2026/09/11

* `提示` 本版本僅改進文件與配套工程, 拼音轉換行為與全部腳本 API 保持不變
* `優化` 重構 10 種語言的 README: 新增使用方法, 快速上手, 拼音風格與選項速查表, 腳本 API, 快速自檢, 常見問題, 權限與安全, 姊妹外掛對比及外掛介面等章節
* `優化` 文件產生腳本升級為同族外掛統一實作: 支援 `--check` 漂移偵測, 跨語言鍵位與形狀對齊校驗, 全形符號攔截以及版本對齊校驗
* `優化` 外掛中心使用說明 (`plugin_instruction.md`) 納入同一套多語言 JSON 產生鏈路, 消除雙源維護
* `優化` 新增 ROADMAP.md 開發路線圖, 並與姊妹外掛 Pinyin4j 建立雙向互鏈與選型對比
* `優化` 統一 README 版式與 Gradle 平台版本管理方式
* `優化` 建置階段阻止意外引入原生相依套件, 並輸出 JSON 校驗報告

# v1.0.0

###### 2026/07/15

* `新增` Pinyin 外掛服務: 外掛 ID 為 `pinyin`, 由 AutoJs6 透過 `org.autojs.plugin.PINYIN` 自動發現並呼叫
* `新增` 拼音轉換 API: `pinyin.convert(text, options)` 回傳二維候選陣列並附帶 `compact()` 組合方法, `pinyin.simple(text)` 回傳精簡字串
* `新增` 字典查詢 API: `pinyin.fromCodePoint(codePoint)` 查詢單字讀音記錄, `pinyin.fromPhrase(phrase)` 查詢詞組讀音
* `新增` 六種拼音風格 (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) 與姓氏模式 (`SURNAME`)
* `新增` 多音字與分詞支援: 內建單字, 詞組, 分詞三份字典及 HMM 模型, 可按需啟用 `segment` / `heteronym` / `group` 選項
* `新增` 多語言資源: 外掛資訊與使用說明覆蓋 10 種語言
* `新增` README 與 CHANGELOG 由 JSON 來源檔與 `.python/generate_markdown.py` 產生多語言 Markdown
