<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>ملحق Pinyin لتحويل النص الصيني الى بينيين</p>

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

### اللغات (Languages)

******

يدعم README.md الحالي اللغات التالية:

- [简体中文 [zh-Hans]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hans.md)
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
- [English [en]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-en.md)
- [Français [fr]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-fr.md)
- [Español [es]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-es.md)
- [日本語 [ja]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ja.md)
- [한국어 [ko]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ko.md)
- [Русский [ru]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ru.md)
- العربية [ar] # الحالية

******

### مقدمة

******

يوفر ملحق AutoJs6 Pinyin تحويل النص الصيني الى بينيين في AutoJs6 باستخدام قواميس مرفقة للحروف والعبارات والتقسيم. يدعم علامات النغمة, النغمات الرقمية, البينيين بلا نغمة, الاحرف الاولى, اول حرف, التقسيم, تعدد النطق, العبارات, ووضع اسم العائلة.

******

### الميزات

******

- يوفر خدمة الملحق `pinyin` مع معرف الملحق `pinyin`.
- يدعم واجهات AutoJs6 مثل `pinyin.convert(text, options)`, `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)`, و `pinyin.fromPhrase(phrase)`.
- يدعم انماط البينيين `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER`, بالاضافة الى الوضع العادي ووضع اسم العائلة.
- يدعم التقسيم المبني على Jieba, تعدد النطق, قواميس العبارات, وتجميع نتائج البينيين.
- تمت ترجمة بيانات الملحق, تعليمات الاستخدام, README, و CHANGELOG الى الاسبانية/الفرنسية/الروسية/العربية/اليابانية/الكورية/الانجليزية/الصينية المبسطة/الصينية التقليدية لهونغ كونغ/الصينية التقليدية لتايوان.

******

### الاستخدام

******

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

تتوفر ايضا طريقة سلسلة مختصرة:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

******

### الخيارات

******

تشمل انماط البينيين الشائعة:

```text
NORMAL, TONE, TONE2, TO3NE,
INITIALS, FIRST_LETTER
```

تشمل الاوضاع:

```text
NORMAL, SURNAME, PLACE_NAME, PLACENAME
```

******

### سجل الاصدارات

******

# v1.0.0

###### 2026/07/15

* `ميزة` تمت اضافة خدمة ملحق Pinyin مع معرف الملحق `pinyin` والمحرك `pinyin`
* `ميزة` تمت اضافة الاكتشاف والاستدعاء من المضيف عبر `org.autojs.plugin.PINYIN`
* `ميزة` تم دعم `pinyin.convert(text, options)` لاعادة نتائج بينيين متداخلة, مع توفير تركيب `compact()` من مضيف AutoJs6
* `ميزة` تم دعم `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)`, و `pinyin.fromPhrase(phrase)`
* `ميزة` تم دعم انماط البينيين `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` واوضاع `NORMAL`/`SURNAME`/`PLACE_NAME`
* `ميزة` تمت اضافة بيانات مرفقة للحروف والعبارات والتقسيم لدعم التقسيم, تعدد النطق, العبارات, ومعالجة بينيين اسم العائلة
* `ميزة` تمت اضافة بيانات الملحق وتعليمات الاستخدام المترجمة للاسبانية, الفرنسية, الروسية, العربية, اليابانية, الكورية, الانجليزية, الصينية المبسطة, الصينية التقليدية لهونغ كونغ, والصينية التقليدية لتايوان
* `ميزة` تمت اضافة مصادر JSON وتوليد `.python/generate_markdown.py` لملفات Markdown متعددة اللغات README و CHANGELOG

##### لمزيد من سجل الاصدارات

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.changelog/CHANGELOG-ar.md)

******

### البناء

******

```powershell
.\gradlew.bat :app:assembleDebug
```

بناء Release:

```powershell
.\gradlew.bat :app:assembleRelease
```

تأتي معاملات البناء من `version.properties`; الحد الادنى الحالي لل SDK هو 24 وال SDK الهدف هو 36.

******

### هيكل الموارد

******

```text
.readme/lang_*.json
.changelog/lang_*.json
.python/generate_markdown.py
app/src/main/res/values-*/strings.xml
app/src/main/res/raw-*/plugin_instruction.md
```

يحتوي `strings.xml` على اوصاف الملحق المترجمة; يحتوي `plugin_instruction.md` على تعليمات الاستخدام التي يعرضها المضيف. يتم توليد README و CHANGELOG من مصادر JSON بواسطة `.python/generate_markdown.py`.

******

### روابط

******

- وثائق AutoJs6 Pinyin: https://docs.autojs6.com/#/pinyin
- مشروع AutoJs6: https://github.com/SuperMonster003/AutoJs6
