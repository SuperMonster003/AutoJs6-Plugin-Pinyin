******

### リリース履歴

******

# v1.0.0

###### 2026/07/15

* `新機能` プラグイン ID `pinyin`, エンジン `pinyin` の Pinyin プラグインサービスを追加
* `新機能` `org.autojs.plugin.PINYIN` によるホスト側の検出と呼び出しを追加
* `新機能` `pinyin.convert(text, options)` が入れ子のピンイン結果を返す機能に対応し, `compact()` 合成は AutoJs6 ホストが提供
* `新機能` `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)`, `pinyin.fromPhrase(phrase)` に対応
* `新機能` `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` のピンインスタイルと `NORMAL`/`SURNAME`/`PLACE_NAME` モードに対応
* `新機能` 文字, フレーズ, 分かち書きデータを同梱し, 分かち書き, 多音字, フレーズ, 姓のピンイン処理に対応
* `新機能` スペイン語, フランス語, ロシア語, アラビア語, 日本語, 韓国語, 英語, 簡体字中国語, 香港繁体字, 台湾繁体字のプラグイン情報と使用説明を追加
* `新機能` 多言語 README と CHANGELOG Markdown 用の JSON ソースと `.python/generate_markdown.py` 生成を追加
