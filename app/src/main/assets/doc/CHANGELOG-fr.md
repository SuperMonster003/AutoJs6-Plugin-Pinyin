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
