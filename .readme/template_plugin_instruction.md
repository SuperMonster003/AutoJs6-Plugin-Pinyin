{{ p_introduction_what }}

### {{ h3_quick_start }}

{{ p_quick_start_basic }}:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

{{ p_quick_start_heteronym }}:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

### {{ h3_styles }}

{{ p_styles_intro }}:

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

{{ p_instruction_options }}

### {{ h3_self_check }}

{{ p_self_check_intro }}:

```javascript
console.log(pinyin.simple("拼音"));
```

{{ p_self_check_result }}

{{ p_instruction_docs }}
