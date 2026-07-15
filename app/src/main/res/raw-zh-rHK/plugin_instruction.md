將中文文本轉換為拼音:

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

可使用 `pinyin.simple(text)` 獲取不帶聲調的緊湊字串:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

支援的選項包括 `style`, `mode`, `segment`, `heteronym` 和 `group`. 常用風格名包括 `NORMAL`, `TONE`, `TONE2`, `TO3NE`, `INITIALS` 和 `FIRST_LETTER`.

更多用法可參考 AutoJs6 文檔的 [Pinyin](https://docs.autojs6.com/#/pinyin) 章節.
