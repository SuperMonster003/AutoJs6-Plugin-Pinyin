******

### 发行历史

******

# v1.0.0

###### 2026/07/15

* `新增` Pinyin 插件服务, 插件 ID 为 `pinyin`, 引擎为 `pinyin`
* `新增` 支持通过 `org.autojs.plugin.PINYIN` 发现并调用插件
* `新增` 支持 `pinyin.convert(text, options)` 返回二维拼音结果, 并由 AutoJs6 宿主提供 `compact()` 组合方法
* `新增` 支持 `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)` 和 `pinyin.fromPhrase(phrase)`
* `新增` 支持 `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` 拼音风格以及 `NORMAL`/`SURNAME`/`PLACE_NAME` 模式
* `新增` 内置汉字, 词组和分词数据, 支持分词, 多音字, 词组和姓氏拼音处理
* `新增` 插件信息和使用说明的多语言资源: 西班牙语/法语/俄语/阿拉伯语/日语/韩语/英语/简体中文/香港繁体/台湾繁体
* `新增` README 与 CHANGELOG 使用 JSON 源文件和 `.python/generate_markdown.py` 生成多语言 Markdown
