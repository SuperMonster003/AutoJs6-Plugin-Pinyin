Convierte texto chino a pinyin:

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

Usa `pinyin.simple(text)` para obtener una cadena compacta sin tonos:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

Las opciones admitidas incluyen `style`, `mode`, `segment`, `heteronym` y `group`. Los estilos comunes son `NORMAL`, `TONE`, `TONE2`, `TO3NE`, `INITIALS` y `FIRST_LETTER`.

Para mas ejemplos de uso, consulta la seccion [Pinyin](https://docs.autojs6.com/#/pinyin) en la documentacion de AutoJs6.
