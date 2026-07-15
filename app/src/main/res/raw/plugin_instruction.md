Convert Chinese text to pinyin:

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

Use `pinyin.simple(text)` for a compact string without tones:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

Supported options include `style`, `mode`, `segment`, `heteronym`, and `group`. Common style names are `NORMAL`, `TONE`, `TONE2`, `TO3NE`, `INITIALS`, and `FIRST_LETTER`.

For more usage examples, refer to the [Pinyin](https://docs.autojs6.com/#/pinyin) section in the AutoJs6 documentation.
