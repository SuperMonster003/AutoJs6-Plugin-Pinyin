Pinyin プラグイン (Pinyin Plugin) は AutoJs6 にオフラインの中国語ピンイン変換機能を提供します. インストール後, スクリプトはグローバルオブジェクト `pinyin` を通じて中国語テキストをさまざまなスタイルのピンインへ変換でき, 多音字の候補, フレーズ辞書, Jieba 単語分割, 姓氏モードをサポートし, ソート, 検索, 頭文字インデックス, 発音注記などの自動化シナリオに適しています.

### クイックスタート

基本の変換: `convert` は 2 次元候補配列を, `simple` はコンパクトな文字列を返します:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

多音字: `heteronym` オプションは全読み候補を返し, `compact()` は読みの組み合わせに展開します:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

### ピンインスタイル

`style` オプションはピンインの出力スタイルを制御します. 以下では "中" (zhōng) を例にします:

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

サポートされるオプションには `style` (ピンインスタイル), `mode` (通常/姓氏/地名モード), `segment` (単語分割), `heteronym` (多音字), `group` (フレーズ結合), 現在の呼び出しだけに適用する `customDictionary` があります.

### セルフチェック

プラグインをインストールして有効化した後, 次の 1 行スクリプトを実行します:

```javascript
console.log(pinyin.simple("拼音"));
```

`pinyin` と出力されればプラグインは正常に動作しています.

より詳しい使い方とオプションの説明は [AutoJs6 Pinyin ドキュメント](https://docs.autojs6.com/#/pinyin) と [プロジェクトホームページ](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) を参照してください.
