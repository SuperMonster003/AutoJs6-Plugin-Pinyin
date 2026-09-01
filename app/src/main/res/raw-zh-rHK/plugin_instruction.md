Pinyin 外掛 (Pinyin Plugin) 為 AutoJs6 提供離線漢語拼音轉換能力. 安裝後, 腳本可透過全局對象 `pinyin` 將中文文本轉換為多種風格的拼音, 支援多音字候選, 詞組詞典, Jieba 分詞與姓氏模式, 適用於排序, 檢索, 首字母索引, 注音標註等自動化場景.

### 快速上手

基礎轉換: `convert` 返回二維候選數組, `simple` 返回緊湊字串:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

多音字: `heteronym` 選項返回全部候選讀音, `compact()` 展開為讀音組合:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

### 拼音風格

`style` 選項控制拼音輸出風格, 以 "中" (zhōng) 為例:

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

支援的選項包括 `style` (拼音風格), `mode` (普通/姓氏/地名模式), `segment` (分詞), `heteronym` (多音字) 與 `group` (詞組合併).

### 快速自檢

安裝並啟用外掛後, 運行以下單行腳本:

```javascript
console.log(pinyin.simple("拼音"));
```

輸出 `pinyin` 即表示外掛已正常工作.

更多用法與選項說明可參閱 [AutoJs6 Pinyin 文檔](https://docs.autojs6.com/#/pinyin) 與 [項目主頁](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin).
