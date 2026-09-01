Le plugin Pinyin (Pinyin Plugin) apporte à AutoJs6 la conversion hors ligne du chinois en pinyin. Une fois installé, les scripts peuvent convertir du texte chinois en pinyin dans plusieurs styles via l'objet global `pinyin`, avec prise en charge des candidats pour les caractères polyphones, d'un dictionnaire de mots, de la segmentation Jieba et d'un mode nom de famille, ce qui couvre le tri, la recherche, l'indexation par première lettre, l'annotation phonétique et d'autres scénarios d'automatisation.

### Démarrage Rapide

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

### Styles De Pinyin

L'option `style` contrôle le style de sortie, illustré avec "中" (zhōng):

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

Les options prises en charge comprennent `style` (style de pinyin), `mode` (normal/nom de famille/toponyme), `segment` (segmentation en mots), `heteronym` (toutes les lectures candidates), `group` (regroupement par mots) et les lectures `customDictionary` limitées à l'appel courant.

### Vérification Rapide

Après avoir installé et activé le plugin, lancez cette ligne unique:

```javascript
console.log(pinyin.simple("拼音"));
```

Une sortie `pinyin` signifie que le plugin fonctionne correctement.

Pour plus de détails sur l'utilisation et les options, consultez la [documentation AutoJs6 Pinyin](https://docs.autojs6.com/#/pinyin) et la [page du projet](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin).
