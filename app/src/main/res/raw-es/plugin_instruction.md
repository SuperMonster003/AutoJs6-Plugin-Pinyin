El plugin Pinyin (Pinyin Plugin) aporta a AutoJs6 la conversión sin conexión de chino a pinyin. Una vez instalado, los scripts pueden convertir texto chino a pinyin en varios estilos mediante el objeto global `pinyin`, con soporte para candidatos de caracteres polifónicos, un diccionario de palabras, la segmentación Jieba y un modo de apellidos, útil para ordenar, buscar, indexar por primera letra, anotar fonéticamente y otros escenarios de automatización.

### Inicio Rápido

Conversión básica: `convert` devuelve un arreglo 2D de candidatos, `simple` devuelve una cadena compacta:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

Caracteres polifónicos: la opción `heteronym` devuelve todas las lecturas candidatas y `compact()` despliega las combinaciones:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

### Estilos De Pinyin

La opción `style` controla el estilo de salida, ilustrado con "中" (zhōng):

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

Las opciones admitidas incluyen `style` (estilo de pinyin), `mode` (normal/apellidos/topónimos), `segment` (segmentación de palabras), `heteronym` (todas las lecturas candidatas), `group` (agrupación por palabras) y las lecturas `customDictionary` válidas solo para la llamada actual.

### Comprobación Rápida

Tras instalar y habilitar el plugin, ejecute esta única línea:

```javascript
console.log(pinyin.simple("拼音"));
```

Una salida `pinyin` significa que el plugin funciona correctamente.

Para más detalles de uso y opciones, consulte la [documentación de AutoJs6 Pinyin](https://docs.autojs6.com/#/pinyin) y la [página del proyecto](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin).
