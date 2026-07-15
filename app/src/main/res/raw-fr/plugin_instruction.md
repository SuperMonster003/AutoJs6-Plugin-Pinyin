Convertit le texte chinois en pinyin:

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

Utilisez `pinyin.simple(text)` pour obtenir une chaine compacte sans tons:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

Les options prises en charge incluent `style`, `mode`, `segment`, `heteronym` et `group`. Les styles courants sont `NORMAL`, `TONE`, `TONE2`, `TO3NE`, `INITIALS` et `FIRST_LETTER`.

Pour plus d'exemples, consultez la section [Pinyin](https://docs.autojs6.com/#/pinyin) de la documentation AutoJs6.
