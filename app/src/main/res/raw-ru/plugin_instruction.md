Плагин Pinyin (Pinyin Plugin) добавляет в AutoJs6 автономное преобразование китайского текста в пиньинь. После установки скрипты через глобальный объект `pinyin` преобразуют китайский текст в пиньинь в нескольких стилях, с поддержкой кандидатов для иероглифов с несколькими чтениями, словаря словосочетаний, сегментации Jieba и режима фамилий, что полезно для сортировки, поиска, индексации по первым буквам, фонетической разметки и других сценариев автоматизации.

### Быстрый Старт

Базовое преобразование: `convert` возвращает двумерный массив кандидатов, `simple` возвращает компактную строку:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

Несколько чтений: параметр `heteronym` возвращает все варианты, а `compact()` разворачивает их комбинации:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

### Стили Пиньиня

Параметр `style` управляет стилем вывода пиньиня; пример для "中" (zhōng):

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

Поддерживаемые параметры: `style` (стиль пиньиня), `mode` (обычный/фамилии/топонимы), `segment` (сегментация), `heteronym` (все варианты чтения), `group` (объединение по словам) и действующие только для текущего вызова чтения `customDictionary`.

### Самопроверка

После установки и включения плагина выполните следующий однострочный скрипт:

```javascript
console.log(pinyin.simple("拼音"));
```

Вывод `pinyin` означает, что плагин работает нормально.

Подробности использования и параметров смотрите в [документации AutoJs6 Pinyin](https://docs.autojs6.com/#/pinyin) и на [странице проекта](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin).
