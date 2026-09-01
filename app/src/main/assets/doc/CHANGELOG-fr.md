******

### Historique Des Versions

******

# v1.0.1

###### 2026/09/01

* `Info` Cette version ne fait qu'améliorer la documentation et l'outillage associé; le comportement de conversion pinyin et toutes les API de script restent inchangés
* `Amélioration` Refonte du README en 10 langues: ajout des sections utilisation, démarrage rapide, tableaux de référence des styles et options de pinyin, API de script, vérification rapide, FAQ, permissions et sécurité, comparaison des plugins frères et interface du plugin
* `Amélioration` Générateur de documentation mis à niveau vers l'implémentation unifiée partagée entre plugins frères: détection de dérive `--check`, validation des clés et des formes entre langues, rejet des symboles pleine chasse et contrôles d'alignement des versions
* `Amélioration` Les instructions du centre de plugins (`plugin_instruction.md`) rejoignent la même chaîne de génération JSON multilingue, éliminant la double maintenance des sources
* `Amélioration` Ajout de la feuille de route ROADMAP.md et mise en place de renvois bidirectionnels et d'un comparatif avec le plugin frère Pinyin4j
* `Amélioration` Uniformiser la mise en page du README et la gestion des versions de la plateforme Gradle

# v1.0.0

###### 2026/07/15

* `Nouveauté` Service du plugin Pinyin: ID de plugin `pinyin`, découvert et invoqué automatiquement par AutoJs6 via `org.autojs.plugin.PINYIN`
* `Nouveauté` API de conversion: `pinyin.convert(text, options)` renvoie un tableau 2D de candidats portant une méthode de combinaison `compact()`, et `pinyin.simple(text)` renvoie une chaîne compacte
* `Nouveauté` API de consultation des dictionnaires: `pinyin.fromCodePoint(codePoint)` interroge l'entrée de lecture d'un caractère et `pinyin.fromPhrase(phrase)` interroge les lectures des mots
* `Nouveauté` Six styles de pinyin (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) plus le mode nom de famille (`SURNAME`)
* `Nouveauté` Prise en charge des polyphones et de la segmentation: dictionnaires de caractères, de mots et de segmentation plus un modèle HMM embarqués, avec les options `segment` / `heteronym` / `group` disponibles à la demande
* `Nouveauté` Ressources multilingues: métadonnées du plugin et instructions disponibles en 10 langues
* `Nouveauté` README et CHANGELOG générés en Markdown multilingue depuis les sources JSON via `.python/generate_markdown.py`
