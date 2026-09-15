<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>Extension Pinyin pour la conversion phonetique du chinois</p>

  <p>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/SuperMonster003/AutoJs6-Plugin-Pinyin?label=Release"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues/SuperMonster003/AutoJs6-Plugin-Pinyin?color=A24232&label=Issues"/></a>
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

Le plugin Pinyin (Pinyin Plugin) apporte à AutoJs6 la conversion hors ligne du chinois en pinyin. Une fois installé, les scripts peuvent convertir du texte chinois en pinyin dans plusieurs styles via l'objet global `pinyin`, avec prise en charge des candidats pour les caractères polyphones, d'un dictionnaire de mots, de la segmentation Jieba et d'un mode nom de famille, ce qui couvre le tri, la recherche, l'indexation par première lettre, l'annotation phonétique et d'autres scénarios d'automatisation.

Le plugin est un APK installé séparément qui s'exécute dans son propre processus; AutoJs6 le découvre automatiquement grâce au mécanisme de plugins et communique avec lui via AIDL. Les dictionnaires de caractères, de mots et de segmentation sont tous embarqués (l'APK pèse environ 6 MB), la conversion se déroule donc entièrement sur l'appareil, sans réseau. Depuis AutoJs6 v6.8.0, le module `pinyin` de l'hôte s'appuie sur ce plugin. La conception de l'API suit la bibliothèque JavaScript [pinyin](https://github.com/hotoo/pinyin) largement utilisée, et ses utilisateurs s'y retrouveront immédiatement.

Ce plugin et [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) sont des plugins frères: celui-ci embarque des dictionnaires complets avec polyphones et segmentation pour les scénarios où la justesse des lectures prime; Pinyin4j repose sur la bibliothèque Java classique pinyin4j et ne pèse qu'environ 0.3 MB pour une transcription légère caractère par caractère. Les deux peuvent être installés ensemble; voir `Comparaison Des Plugins Frères` ci-dessous.

******

### Points Forts

******

- Prêt à l'emploi: découvert automatiquement par AutoJs6 après l'installation, sans redémarrage de l'hôte; les scripts utilisent directement l'objet global `pinyin`.
- Dictionnaires complets: dictionnaires de caractères, de mots et de segmentation plus un modèle HMM embarqués, entièrement hors ligne, sans aucune requête réseau.
- Prise en charge des polyphones: l'option `heteronym` renvoie toutes les lectures candidates de chaque caractère, et le dictionnaire de mots choisit automatiquement les lectures usuelles.
- Segmentation Jieba: l'option `segment` active la segmentation en mots pour désambiguïser les polyphones par mots et améliorer la justesse sur des phrases entières.
- Six styles de pinyin: marques de ton, tons numériques, chiffre après la finale, sans ton, initiales et premières lettres, couvrant le tri, la recherche et l'annotation.
- Modes pour les noms propres: `SURNAME` privilégie les lectures des noms de famille, tandis que `PLACE_NAME` applique d'abord un corpus choisi de toponymes aux sources traçables, puis revient à la conversion normale.
- Résultats composables: le tableau 2D de candidats renvoyé par `convert` porte une méthode `compact()` qui déploie toutes les combinaisons de lectures en une étape.
- Multilingue: métadonnées du plugin, instructions, README et journal des modifications disponibles en 10 langues.

******

### Utilisation

******

1. Mettez AutoJs6 à niveau vers le build interne 3923 (6.7.1 Alpha4) ou supérieur; depuis la v6.8.0, la conversion pinyin est entièrement déléguée aux plugins, la version la plus récente est donc recommandée.
2. Téléchargez l'APK du plugin depuis la page [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) et installez-le sur l'appareil exécutant AutoJs6, ou installez-le en ligne directement depuis le centre de plugins d'AutoJs6.
3. Ouvrez le centre de plugins d'AutoJs6 et vérifiez que le plugin `Pinyin` est reconnu, autorisé et activé.
4. Appelez l'objet global `pinyin` dans vos scripts comme montré dans `Démarrage Rapide` ci-dessous; vous pouvez aussi lancer d'abord la `Vérification Rapide` pour confirmer que le plugin fonctionne.

> Le plugin est publié en un seul APK universel (implémentation purement JVM, sans variantes d'architecture CPU) et prend en charge les appareils sous Android 7.0 (API 24) et supérieur. Il n'a pas d'interface autonome et ne crée pas d'icône de lanceur; AutoJs6 le découvre et le gère de manière unifiée.

******

### Démarrage Rapide

******

Conversion de base: `convert` renvoie un tableau 2D de candidats, `simple` renvoie une chaîne compacte:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

Polyphones: l'option `heteronym` renvoie toutes les lectures candidates et `compact()` déploie les combinaisons:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

Désambiguïsation par segmentation, mode nom de famille et mode toponyme:

```javascript
console.log(pinyin.simple("音乐重要", false, true));
console.log(pinyin.convert("单田芳", { mode: "SURNAME" }));
console.log(pinyin.convert("六安", { mode: "PLACE_NAME" })); // [["lù"], ["ān"]]
console.log(pinyin.convert("六安", {
  customDictionary: { "六安": [["liú"], ["ān"]] },
})); // [["liú"], ["ān"]]
```

******

### Styles De Pinyin

******

L'option `style` contrôle le style de sortie, illustré avec "中" (zhōng):

| Style | Sortie | Description |
|---|---|---|
| `TONE` | `zhōng` | Marques de ton placées sur la finale (par défaut) |
| `TONE2` | `zhong1` | Chiffre de ton 0-4 ajouté en fin de syllabe |
| `TO3NE` | `zho1ng` | Chiffre de ton placé juste après la finale |
| `NORMAL` | `zhong` | Sans tons |
| `INITIALS` | `zh` | Initiale seule (chaîne vide pour les syllabes sans initiale) |
| `FIRST_LETTER` | `z` | Première lettre de la syllabe seulement |

La valeur de `style` est insensible à la casse et accepte une chaîne (comme `"TONE2"`) ou une constante (comme `pinyin.STYLE_TONE2`).

******

### Options

******

`pinyin.convert(text, options)` prend en charge les options suivantes:

| Option | Par défaut | Description |
|---|---|---|
| `style` | `TONE` | Style de pinyin, voir `Styles De Pinyin` ci-dessus |
| `mode` | `NORMAL` | Mode de conversion: `NORMAL` pour le texte ordinaire, `SURNAME` pour les noms de famille, `PLACE_NAME` pour des lectures choisies de toponymes |
| `segment` | `false` | Active la segmentation Jieba et exploite le dictionnaire de mots pour désambiguïser les polyphones |
| `heteronym` | `false` | Renvoie toutes les lectures candidates de chaque caractère au lieu de la seule première |
| `group` | `false` | Regroupe les candidats pinyin par mots segmentés (à utiliser avec `segment`) |
| `customDictionary` | `{}` | Lectures Han de remplacement pour cet appel au format `{ expression: [[candidats avec tons], ...] }`; la correspondance la plus longue prévaut, rien n'est conservé et un hôte AutoJs6 ainsi qu'un plugin compatibles sont requis |

Les modes acceptent aussi des constantes (comme `pinyin.MODE_PLACE_NAME`). `PLACE_NAME` cherche la correspondance la plus longue dans un petit corpus vérifié manuellement; le texte absent revient à `NORMAL`. Il ne s'agit pas d'un répertoire national exhaustif; consultez le [corpus et ses sources](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/dictionaries/place-names.md).

******

### API De Script

******

L'objet global `pinyin` fournit les méthodes suivantes (appeler directement `pinyin(text, options)` équivaut à `pinyin.convert`):

```text
pinyin(text, options?)                   -> string[][]
pinyin.convert(text, options?)           -> string[][]
pinyin.simple(text, numeric?, segment?)  -> string
pinyin.compare(textA, textB)             -> number
pinyin.compact(matrix)                   -> string[][]
pinyin.fromCodePoint(codePoint)          -> string | null
pinyin.fromPhrase(phrase)                -> string[][]
pinyin.STYLE_* / pinyin.MODE_*           -> constants
```

- `convert` renvoie un tableau 2D: chaque caractère chinois ou position de caractère d'un mot occupe une ligne contenant ses lectures candidates; les caractères non couverts et non chinois gardent une ligne telle quelle. Le tableau renvoyé porte une méthode `compact()` qui déploie toutes les combinaisons de lectures.
- `simple` renvoie une chaîne compacte: la première lecture de chaque caractère est concaténée; passez `true` en 2e argument pour des tons numériques (style TONE2, sans tons sinon) et `true` en 3e argument pour activer la segmentation.
- `fromCodePoint` consulte l'entrée brute du dictionnaire pour un point de code (candidats avec tons séparés par des virgules) et renvoie `null` s'il n'est pas couvert.
- `fromPhrase` consulte le dictionnaire de mots et renvoie les lectures candidates de chaque position de caractère du mot; un tableau vide est renvoyé s'il n'est pas couvert.
- Toutes les méthodes répondent de manière synchrone; le tout premier appel initialise les dictionnaires embarqués et peut prendre un peu plus de temps.

#### Node.js

Dans l'environnement Node.js, appelez le même fournisseur via la façade publique `autojs6:bridge` et déclarez explicitement la capacité `pinyin`:

```javascript
const { callAutoJs } = require("autojs6:bridge");

(async () => {
  const result = await callAutoJs(
    "pinyin",
    "convert",
    ["中心", { style: "TONE2" }],
    { permissions: ["pinyin"] },
  );
  console.log(result); // [["zhong1"], ["xin1"]]
})();
```

******

### Vérification Rapide

******

Après avoir installé et activé le plugin, lancez cette ligne unique:

```javascript
console.log(pinyin.simple("拼音"));
```

Une sortie `pinyin` signifie que le plugin fonctionne correctement.

******

### FAQ

******

#### Comment vérifier que le plugin est actif?

Ouvrez le centre de plugins d'AutoJs6: voir le plugin `Pinyin` listé et activé signifie que l'hôte l'a reconnu. Lancez ensuite le script de `Vérification Rapide` ci-dessus; une sortie `pinyin` confirme qu'il fonctionne.

#### Un script signale un plugin manquant ou `pinyin` indisponible?

Vérifiez que le build interne d'AutoJs6 est au moins 3923 et que le plugin a été installé, autorisé et activé dans le centre de plugins. Depuis AutoJs6 v6.8.0, l'hôte n'embarque plus d'implémentation pinyin, toute la conversion est donc déléguée à ce plugin.

#### Pourquoi n'y a-t-il pas d'icône dans la liste des applications ou sur l'écran d'accueil?

C'est normal. Le plugin n'a pas d'interface autonome et ne crée pas d'icône de lanceur; après installation, AutoJs6 le découvre et l'appelle en arrière-plan, et toute interaction se fait dans AutoJs6.

#### Un caractère polyphone n'est pas converti comme prévu?

Par défaut, la première lecture de chaque caractère isolé est utilisée. Activez l'option `segment` pour désambiguïser via le dictionnaire de mots et la segmentation (par exemple `pinyin.simple(text, false, true)`), ou utilisez l'option `heteronym` pour obtenir tous les candidats. Si un mot courant reste mal lu, signalez-le via [Issues](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues) afin d'améliorer les dictionnaires.

#### Comment choisir entre ce plugin et son frère Pinyin4j?

Choisissez ce plugin pour les polyphones, la segmentation, les mots ou les lectures de noms de famille; choisissez [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) pour une transcription légère caractère par caractère quand la taille de l'APK compte. Ils ne se gênent pas et peuvent être installés ensemble; voir `Comparaison Des Plugins Frères` ci-dessous.

#### Le plugin accède-t-il au réseau ou demande-t-il des permissions sensibles?

Non. Tous les dictionnaires sont embarqués dans l'APK et la conversion se fait sur l'appareil; le manifeste ne déclare que la permission de plugin nécessaire pour communiquer avec AutoJs6, sans permission réseau, stockage ni autre permission système sensible.

#### Pourquoi l'APK pèse-t-il environ 6 MB?

L'APK embarque quatre jeux de données: un dictionnaire de caractères, un dictionnaire de mots, un lexique de segmentation et un modèle HMM, échangeant de la taille contre un fonctionnement entièrement hors ligne et une meilleure justesse. Si la taille prime pour vous, envisagez le plugin frère [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) d'environ 0.3 MB.

#### Pourquoi `customDictionary` ou un appel Pinyin depuis Node.js est-il refusé?

Ces chemins exigent des versions compatibles d'AutoJs6 et du plugin Pinyin. Les appels Node.js doivent déclarer `permissions: ["pinyin"]`. Le dictionnaire personnalisé ne vaut que pour un appel et doit respecter les limites documentées d'entrées, de candidats, de combinaisons et de 64 KiB.

******

### Permissions Et Sécurité

******

Le plugin est conçu pour réduire au minimum sa surface de données comme sa surface de permissions:

- Permissions minimales: le manifeste ne déclare que la permission de plugin AutoJs6 (`org.autojs.permission.PLUGIN`), sans permission réseau, stockage, caméra ni autre permission système sensible.
- Conversion locale: le texte à convertir ne circule que via Binder à l'intérieur de l'appareil, les dictionnaires sont entièrement embarqués, tout reste hors ligne et aucune donnée ne quitte l'appareil.
- Signature et autorisation: AutoJs6 vérifie la signature du plugin, et le plugin doit être autorisé et activé dans le centre de plugins avant que les scripts puissent l'appeler; le service et le point d'éveil sont protégés par la permission de plugin, les applications tierces ne peuvent donc pas les appeler directement.
- Ouvert et auditable: le code du plugin, l'empaquetage des dictionnaires et la chaîne de génération de documentation sont entièrement open source.

N'installez le plugin que depuis la page officielle [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) ou le centre de plugins d'AutoJs6; un APK d'origine inconnue peut être altéré même si son nom et sa version semblent identiques.

******

### Comparaison Des Plugins Frères

******

AutoJs6 propose deux plugins pinyin officiels aux priorités différentes, installables côte à côte:

| Critère | [Pinyin](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) | [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) |
|---|---|---|
| Implémentation sous-jacente | Dictionnaires embarqués + segmentation Jieba | Bibliothèque Java classique `pinyin4j` |
| Objet global | `pinyin` | `pinyin4j` |
| Polyphones | Pris en charge, tous les candidats disponibles | Non pris en charge, première lecture seulement |
| Segmentation et mots | Prise en charge (dictionnaire de mots + Jieba) | Non prise en charge, conversion caractère par caractère |
| Mode nom de famille | Pris en charge | Non pris en charge |
| Forme de sortie | Tableau 2D de candidats (composable via `compact()`) ou chaîne compacte | Chaîne avec séparateur configurable |
| Styles et formats | 6 styles de pinyin | 3 formats de ton + casse + représentation du `ü` |
| Taille de l'APK | Environ 6 MB (dictionnaires embarqués) | Environ 0.3 MB |
| Idéal pour | Justesse d'abord: polyphones, mots, noms de personnes | Taille et simplicité d'abord: transcription rapide caractère par caractère |

Les deux plugins ne dépendent pas l'un de l'autre et ne se gênent pas; une fois les deux installés, les scripts appellent `pinyin` et `pinyin4j` selon le besoin. Voir [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) pour les détails.

******

### Interface Du Plugin

******

Les informations suivantes s'adressent aux développeurs de l'hôte AutoJs6 et de plugins; l'hôte utilise ces identifiants pour découvrir le plugin et négocier les capacités:

```text
application id: io.github.supermonster003.autojs6.plugin.pinyin
plugin id: pinyin
engine: pinyin
variant: default
discovery action: org.autojs.plugin.PINYIN
discovery category: pinyin
wake action: org.autojs.plugin.action.WAKE
binder interface: IPinyinPlugin
binder methods: getInfo / convert / simple / fromCodePoint / fromPhrase
minimum host build: 3923
native library: none (pure JVM, all ABIs)
```

`PinyinPluginService` répond à l'action `org.autojs.plugin.PINYIN` (catégorie `pinyin`) et expose 5 méthodes via l'interface AIDL `IPinyinPlugin`; `convert` et `fromPhrase` renvoient des tableaux 2D sous forme de chaînes JSON, et les options transitent dans un `Bundle` (clés: `mode` / `style` / `segment` / `heteronym` / `group` / `custom_dictionary_json`). Les dictionnaires personnalisés exigent la capacité `pinyin.customDictionary.v1`. Le service et `WakeActivity` sont protégés par la permission `org.autojs.permission.PLUGIN`, les applications tierces ne peuvent donc pas les appeler directement.

******

### Feuille De Route

******

Les capacités prévues du plugin et leur avancement sont maintenus sous forme de liste cochable dans ROADMAP.md, organisée par jalons avec critères d'acceptation, couvrant le mode toponymes, l'évolution des dictionnaires, les dictionnaires personnalisés, les performances et l'intégration continue. Les éléments non cochés expriment une intention et non des capacités actuelles; les discussions via Issues sont bienvenues.

- [Voir ROADMAP.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/ROADMAP.md)

******

### Historique Des Versions

******

#### v1.0.3

_2026/09/15_

- `Amélioration` compileSdk et targetSdk passent à 37 (Android 17) ; le comportement du plugin ne dépend pas de la nouvelle cible

#### v1.0.2

_2026/09/13_

- `Correctif` Conserver la date de version du plugin en anglais quelle que soit la langue de la machine de compilation
- `Amélioration` Ressources traduites cohérentes, activation explicite du plugin et validation des paquets de publication

#### v1.0.1

_2026/09/11_

- `Note` Cette version ne fait qu'améliorer la documentation et l'outillage associé; le comportement de conversion pinyin et toutes les API de script restent inchangés
- `Amélioration` Refonte du README en 10 langues: ajout des sections utilisation, démarrage rapide, tableaux de référence des styles et options de pinyin, API de script, vérification rapide, FAQ, permissions et sécurité, comparaison des plugins frères et interface du plugin
- `Amélioration` Générateur de documentation mis à niveau vers l'implémentation unifiée partagée entre plugins frères: détection de dérive `--check`, validation des clés et des formes entre langues, rejet des symboles pleine chasse et contrôles d'alignement des versions
- `Amélioration` Les instructions du centre de plugins (`plugin_instruction.md`) rejoignent la même chaîne de génération JSON multilingue, éliminant la double maintenance des sources
- `Amélioration` Ajout de la feuille de route ROADMAP.md et mise en place de renvois bidirectionnels et d'un comparatif avec le plugin frère Pinyin4j
- `Amélioration` Uniformiser la mise en page du README et la gestion des versions de la plateforme Gradle
- `Amélioration` La vérification de compilation rejette les dépendances natives involontaires et produit un rapport JSON

##### Pour plus d'historique des versions

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/assets/doc/CHANGELOG-fr.md)

******

### Compilation

******

Cette section s'adresse aux développeurs souhaitant compiler le plugin depuis les sources.

Compiler un APK debug:

```powershell
.\gradlew.bat :app:assembleDebug
```

Exécuter les tests unitaires JVM et compiler l'APK de test instrumentation:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

Compiler un APK release (un seul paquet universel; la signature est automatique une fois le fichier non suivi `sign.properties` configuré):

```powershell
.\gradlew.bat :app:assembleRelease
```

Compiler et vérifier en une commande l'APK universel signé, puis générer `SHA256SUMS.txt` et `RELEASE_NOTES.md` depuis le CHANGELOG anglais:

```powershell
py scripts\release\prepare_release.py
```

Vérifier que les sources de la documentation multilingue et les fichiers générés sont synchronisés (également vérifié par l'intégration continue):

```powershell
py .python\generate_markdown.py --check
```

Les paramètres de compilation sont centralisés dans `version.properties`: SDK minimal 24 (Android 7.0), SDK cible 37, version actuelle 1.0.3.

******

### Localisation Et Génération De Docs

******

```text
.readme/common.json
.readme/lang_*.json
.readme/template_readme.md
.readme/template_plugin_instruction.md
.changelog/lang_*.json
.changelog/template_changelog.md
.python/generate_markdown.py
app/src/main/assets/doc/CHANGELOG-*.md
app/src/main/res/values-*/strings.xml
app/src/main/res/raw-*/plugin_instruction.md
```

`strings.xml` contient la description localisée du plugin, et `plugin_instruction.md` contient les instructions affichées dans le centre de plugins de l'hôte. README, journal des modifications et instructions sont tous générés depuis des sources JSON: modifiez les sources sous `.readme/` et `.changelog/`, puis exécutez `py .python/generate_markdown.py` pour régénérer chaque artefact; les artefacts générés ne sont jamais édités à la main. Exécutez `py .python/generate_markdown.py --check` pour vérifier que sources et artefacts sont synchronisés.

******

### Licence

******

Le code du projet est sous licence [Mozilla Public License 2.0](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE). L'implémentation de segmentation embarquée est portée du projet [jieba-analysis](https://github.com/huaban/jieba-analysis), et la conception de l'API suit la bibliothèque [pinyin](https://github.com/hotoo/pinyin).

******

### Liens

******

- Documentation AutoJs6 Pinyin: https://docs.autojs6.com/#/pinyin
- Projet AutoJs6: https://github.com/SuperMonster003/AutoJs6
- Plugin frère Pinyin4j: https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j
- Bibliothèque pinyin (référence de conception d'API): https://github.com/hotoo/pinyin
- Projet jieba-analysis: https://github.com/huaban/jieba-analysis


[16 KB page alignment and build verification](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/16kb.md)
