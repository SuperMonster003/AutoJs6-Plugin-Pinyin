<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>Плагин Pinyin для преобразования китайского текста в пиньинь</p>

  <p>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/SuperMonster003/AutoJs6-Plugin-Pinyin?label=Release"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues/SuperMonster003/AutoJs6-Plugin-Pinyin?color=A24232&label=Issues"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/commit/f21dd3191be1cb0c07d5cadf7478c29064e409c1"><img alt="Created" src="https://img.shields.io/date/1783230112?color=2e7d32&label=Created"/></a>
    <br>
    <a href="https://developer.android.com/studio/archive"><img alt="Android Studio" src="https://img.shields.io/badge/Android%20Studio-2023.3+-B64FC8"/></a>
    <a href="https://www.jetbrains.com/idea/download/other.html"><img alt="IntelliJ IDEA" src="https://img.shields.io/badge/IntelliJ%20IDEA-2023.3+-EE4677"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/SuperMonster003/AutoJs6-Plugin-Pinyin?color=534BAE&label=License"/></a>
  </p>
</div>

******

### Языки (Languages)

******

Текущий README.md поддерживает следующие языки:

- [简体中文 [zh-Hans]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hans.md)
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
- [English [en]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-en.md)
- [Français [fr]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-fr.md)
- [Español [es]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-es.md)
- [日本語 [ja]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ja.md)
- [한국어 [ko]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ko.md)
- Русский [ru] # текущий
- [العربية [ar]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ar.md)

******

### Введение

******

Плагин AutoJs6 Pinyin предоставляет AutoJs6 преобразование китайского текста в пиньинь с упакованными словарями символов, фраз и сегментации. Поддерживаются тоновые знаки, числовые тоны, пиньинь без тона, инициали, первые буквы, сегментация, многозвучные символы, фразы и режим фамилий.

******

### Возможности

******

- Предоставляет службу плагина `pinyin` с ID плагина `pinyin`.
- Поддерживает API AutoJs6, такие как `pinyin.convert(text, options)`, `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)` и `pinyin.fromPhrase(phrase)`.
- Поддерживает стили пиньиня `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER`, а также обычный режим и режим фамилий.
- Поддерживает сегментацию на базе Jieba, многозвучные символы, словари фраз и групповые комбинации пиньиня.
- Метаданные плагина, инструкции по использованию, README и CHANGELOG локализованы для испанского/французского/русского/арабского/японского/корейского/английского/упрощенного китайского/традиционного китайского Hong Kong/традиционного китайского Taiwan.

******

### Использование

******

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

Также доступен метод для компактной строки:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

******

### Параметры

******

Распространенные стили пиньиня:

```text
NORMAL, TONE, TONE2, TO3NE,
INITIALS, FIRST_LETTER
```

Режимы:

```text
NORMAL, SURNAME, PLACE_NAME, PLACENAME
```

******

### История Выпусков

******

# v1.0.0

###### 2026/07/15

* `Новое` Добавлена служба плагина Pinyin с ID плагина `pinyin` и движком `pinyin`
* `Новое` Добавлено обнаружение и вызов хостом через `org.autojs.plugin.PINYIN`
* `Новое` Поддержан `pinyin.convert(text, options)` с вложенными результатами пиньиня, а композиция `compact()` предоставляется хостом AutoJs6
* `Новое` Поддержаны `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)` и `pinyin.fromPhrase(phrase)`
* `Новое` Поддержаны стили пиньиня `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` и режимы `NORMAL`/`SURNAME`/`PLACE_NAME`
* `Новое` Добавлены упакованные данные символов, фраз и сегментации для сегментации, многозвучных символов, фраз и обработки фамилий
* `Новое` Добавлены локализованные метаданные плагина и инструкции по использованию для испанского, французского, русского, арабского, японского, корейского, английского, упрощенного китайского, традиционного китайского Hong Kong и традиционного китайского Taiwan
* `Новое` Добавлены JSON исходники и генерация `.python/generate_markdown.py` для многоязычных Markdown файлов README и CHANGELOG

##### Дополнительная история выпусков

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.changelog/CHANGELOG-ru.md)

******

### Сборка

******

```powershell
.\gradlew.bat :app:assembleDebug
```

Release сборка:

```powershell
.\gradlew.bat :app:assembleRelease
```

Параметры сборки берутся из `version.properties`; текущий минимальный SDK равен 24, целевой SDK равен 36.

******

### Структура Ресурсов

******

```text
.readme/lang_*.json
.changelog/lang_*.json
.python/generate_markdown.py
app/src/main/res/values-*/strings.xml
app/src/main/res/raw-*/plugin_instruction.md
```

`strings.xml` содержит локализованные описания плагина; `plugin_instruction.md` содержит инструкции по использованию, отображаемые хостом. README и CHANGELOG создаются из JSON исходников с помощью `.python/generate_markdown.py`.

******

### Ссылки

******

- Документация AutoJs6 Pinyin: https://docs.autojs6.com/#/pinyin
- Проект AutoJs6: https://github.com/SuperMonster003/AutoJs6
