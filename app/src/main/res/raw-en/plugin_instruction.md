The Pinyin Plugin provides AutoJs6 with offline Chinese-to-Pinyin conversion. Once installed, scripts can use the global `pinyin` object to convert Chinese text into Pinyin in multiple styles, with support for heteronym candidates, a phrase dictionary, Jieba word segmentation and a surname mode, making it useful for sorting, searching, initial-letter indexing, phonetic annotation and other automation scenarios.

### Quick start

Basic conversion: `convert` returns a 2D candidate array, `simple` returns a compact string:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

Heteronyms: the `heteronym` option returns all candidate readings and `compact()` expands the combinations:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

### Pinyin styles

The `style` option controls the output style, illustrated with "中" (zhōng):

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

Supported options include `style` (Pinyin style), `mode` (normal/surname/place-name), `segment` (word segmentation), `heteronym` (all candidate readings), `group` (merge by words) and per-call `customDictionary` reading overrides.

### Self check

After installing and enabling the plugin, run this one-liner:

```javascript
console.log(pinyin.simple("拼音"));
```

An output of `pinyin` means the plugin is working properly.

For more usage and option details, refer to the [AutoJs6 Pinyin documentation](https://docs.autojs6.com/#/pinyin) and the [project homepage](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin).
