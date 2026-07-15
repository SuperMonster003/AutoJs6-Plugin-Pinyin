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
