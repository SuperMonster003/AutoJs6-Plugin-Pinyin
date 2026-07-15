将中文文本转换为拼音:

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

可使用 `pinyin.simple(text)` 获取不带声调的紧凑字符串:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

支持的选项包括 `style`, `mode`, `segment`, `heteronym` 和 `group`. 常用风格名包括 `NORMAL`, `TONE`, `TONE2`, `TO3NE`, `INITIALS` 和 `FIRST_LETTER`.

更多用法可参考 AutoJs6 文档的 [Pinyin](https://docs.autojs6.com/#/pinyin) 章节.
