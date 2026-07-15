# v1.0.0

###### 2026/07/15

* `Feature` Added the Pinyin plugin service with plugin ID `pinyin` and engine `pinyin`
* `Feature` Added host discovery and invocation through `org.autojs.plugin.PINYIN`
* `Feature` Supported `pinyin.convert(text, options)` returning nested pinyin results, with `compact()` composition provided by the AutoJs6 host
* `Feature` Supported `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)`, and `pinyin.fromPhrase(phrase)`
* `Feature` Supported `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` pinyin styles and `NORMAL`/`SURNAME`/`PLACE_NAME` modes
* `Feature` Added packaged character, phrase, and segmentation data for segmentation, heteronyms, phrases, and surname pinyin handling
* `Feature` Added localized plugin metadata and usage instructions for Spanish, French, Russian, Arabic, Japanese, Korean, English, Simplified Chinese, Hong Kong Traditional Chinese, and Taiwan Traditional Chinese
* `Feature` Added JSON sources and `.python/generate_markdown.py` generation for multilingual README and CHANGELOG Markdown files
