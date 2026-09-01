Pinyin 插件 (Pinyin Plugin) 为 AutoJs6 提供离线汉语拼音转换能力. 安装后, 脚本可通过全局对象 `pinyin` 将中文文本转换为多种风格的拼音, 支持多音字候选, 词组词典, Jieba 分词与姓氏模式, 适用于排序, 检索, 首字母索引, 注音标注等自动化场景.

### 快速上手

基础转换: `convert` 返回二维候选数组, `simple` 返回紧凑字符串:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

多音字: `heteronym` 选项返回全部候选读音, `compact()` 展开为读音组合:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

### 拼音风格

`style` 选项控制拼音输出风格, 以 "中" (zhōng) 为例:

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

支持的选项包括 `style` (拼音风格), `mode` (普通/姓氏/地名模式), `segment` (分词), `heteronym` (多音字), `group` (词组合并) 与仅当前调用生效的 `customDictionary` 读音覆盖.

### 快速自检

安装并启用插件后, 运行以下单行脚本:

```javascript
console.log(pinyin.simple("拼音"));
```

输出 `pinyin` 即表示插件已正常工作.

更多用法与选项说明可参阅 [AutoJs6 Pinyin 文档](https://docs.autojs6.com/#/pinyin) 与 [项目主页](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin).
