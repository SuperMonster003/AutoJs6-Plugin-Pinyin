Преобразует китайский текст в пиньинь:

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

Используйте `pinyin.simple(text)` для компактной строки без тонов:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

Поддерживаемые параметры включают `style`, `mode`, `segment`, `heteronym` и `group`. Распространенные стили: `NORMAL`, `TONE`, `TONE2`, `TO3NE`, `INITIALS` и `FIRST_LETTER`.

Дополнительные примеры смотрите в разделе [Pinyin](https://docs.autojs6.com/#/pinyin) документации AutoJs6.
