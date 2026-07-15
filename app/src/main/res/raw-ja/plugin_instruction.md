中国語テキストをピンインに変換します:

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

`pinyin.simple(text)` で声調なしの連結文字列を取得できます:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

対応オプションは `style`, `mode`, `segment`, `heteronym`, `group` です. よく使うスタイル名は `NORMAL`, `TONE`, `TONE2`, `TO3NE`, `INITIALS`, `FIRST_LETTER` です.

その他の使用例は AutoJs6 ドキュメントの [Pinyin](https://docs.autojs6.com/#/pinyin) セクションを参照してください.
