******

### Historial De Versiones

******

# v1.0.0

###### 2026/07/15

* `Nuevo` Se agrego el servicio del complemento Pinyin con ID de complemento `pinyin` y motor `pinyin`
* `Nuevo` Se agrego descubrimiento e invocacion desde el host mediante `org.autojs.plugin.PINYIN`
* `Nuevo` Se admitio `pinyin.convert(text, options)` con resultados de pinyin anidados, y composicion `compact()` proporcionada por el host AutoJs6
* `Nuevo` Se admitio `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)` y `pinyin.fromPhrase(phrase)`
* `Nuevo` Se admitieron los estilos de pinyin `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` y los modos `NORMAL`/`SURNAME`/`PLACE_NAME`
* `Nuevo` Se agregaron datos incluidos de caracteres, frases y segmentacion para segmentacion, heteronimos, frases y manejo de apellidos
* `Nuevo` Se agregaron metadatos del complemento e instrucciones de uso localizadas en espanol, frances, ruso, arabe, japones, coreano, ingles, chino simplificado, chino tradicional de Hong Kong y chino tradicional de Taiwan
* `Nuevo` Se agregaron fuentes JSON y generacion `.python/generate_markdown.py` para archivos Markdown README y CHANGELOG multilingues
