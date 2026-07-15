<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>Extension Pinyin pour la conversion phonétique du chinois</p>

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

### Langues (Languages)

******

Le README.md actuel prend en charge les langues suivantes:

- [简体中文 [zh-Hans]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hans.md)
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
- [English [en]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-en.md)
- Français [fr] # actuel
- [Español [es]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-es.md)
- [日本語 [ja]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ja.md)
- [한국어 [ko]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ko.md)
- [Русский [ru]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ru.md)
- [العربية [ar]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ar.md)

******

### Introduction

******

L'extension AutoJs6 Pinyin fournit a AutoJs6 une conversion en pinyin chinois avec des dictionnaires integres de caracteres, de phrases et de segmentation. Elle prend en charge les marques de ton, les tons numeriques, le pinyin sans ton, les initiales, les premieres lettres, la segmentation, les heteronymes, les phrases et le mode nom de famille.

******

### Fonctionnalites

******

- Fournit le service d'extension `pinyin`, avec l'ID d'extension `pinyin`.
- Prend en charge les API AutoJs6 telles que `pinyin.convert(text, options)`, `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)` et `pinyin.fromPhrase(phrase)`.
- Prend en charge les styles pinyin `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER`, ainsi que les modes normal et nom de famille.
- Prend en charge la segmentation basee sur Jieba, les heteronymes, les dictionnaires de phrases et les combinaisons de resultats pinyin.
- Les metadonnees de l'extension, les instructions d'utilisation, le README et le CHANGELOG sont localises en espagnol/francais/russe/arabe/japonais/coreen/anglais/chinois simplifie/chinois traditionnel de Hong Kong/chinois traditionnel de Taiwan.

******

### Utilisation

******

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

Une methode de chaine compacte est egalement disponible:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

******

### Options

******

Les styles pinyin courants incluent:

```text
NORMAL, TONE, TONE2, TO3NE,
INITIALS, FIRST_LETTER
```

Les modes incluent:

```text
NORMAL, SURNAME, PLACE_NAME, PLACENAME
```

******

### Historique Des Versions

******

# v1.0.0

###### 2026/07/15

* `Fonctionnalite` Ajout du service d'extension Pinyin avec l'ID d'extension `pinyin` et le moteur `pinyin`
* `Fonctionnalite` Ajout de la decouverte et de l'appel par l'hote via `org.autojs.plugin.PINYIN`
* `Fonctionnalite` Prise en charge de `pinyin.convert(text, options)` avec resultats pinyin imbriques, et composition `compact()` fournie par l'hote AutoJs6
* `Fonctionnalite` Prise en charge de `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)` et `pinyin.fromPhrase(phrase)`
* `Fonctionnalite` Prise en charge des styles pinyin `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` et des modes `NORMAL`/`SURNAME`/`PLACE_NAME`
* `Fonctionnalite` Ajout de donnees integrees de caracteres, phrases et segmentation pour la segmentation, les heteronymes, les phrases et les noms de famille
* `Fonctionnalite` Ajout de metadonnees de l'extension et d'instructions d'utilisation localisees en espagnol, francais, russe, arabe, japonais, coreen, anglais, chinois simplifie, chinois traditionnel de Hong Kong et chinois traditionnel de Taiwan
* `Fonctionnalite` Ajout de sources JSON et de la generation `.python/generate_markdown.py` pour les fichiers Markdown README et CHANGELOG multilingues

##### Pour plus d'historique des versions

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.changelog/CHANGELOG-fr.md)

******

### Compilation

******

```powershell
.\gradlew.bat :app:assembleDebug
```

Compilation Release:

```powershell
.\gradlew.bat :app:assembleRelease
```

Les parametres de compilation proviennent de `version.properties`; le SDK minimum actuel est 24 et le SDK cible est 36.

******

### Structure Des Ressources

******

```text
.readme/lang_*.json
.changelog/lang_*.json
.python/generate_markdown.py
app/src/main/res/values-*/strings.xml
app/src/main/res/raw-*/plugin_instruction.md
```

`strings.xml` contient les descriptions localisees de l'extension; `plugin_instruction.md` contient les instructions d'utilisation affichees par l'hote. Les fichiers README et CHANGELOG sont generes depuis les sources JSON par `.python/generate_markdown.py`.

******

### Liens

******

- Documentation AutoJs6 Pinyin: https://docs.autojs6.com/#/pinyin
- Projet AutoJs6: https://github.com/SuperMonster003/AutoJs6
