حول النص الصيني الى بينيين:

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

استخدم `pinyin.simple(text)` للحصول على سلسلة مختصرة بلا نغمات:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

تشمل الخيارات المدعومة `style`, `mode`, `segment`, `heteronym`, و `group`. تشمل الانماط الشائعة `NORMAL`, `TONE`, `TONE2`, `TO3NE`, `INITIALS`, و `FIRST_LETTER`.

لمزيد من امثلة الاستخدام, راجع قسم [Pinyin](https://docs.autojs6.com/#/pinyin) في وثائق AutoJs6.
