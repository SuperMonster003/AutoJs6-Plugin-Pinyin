******

### Historial De Versiones

******

# v1.0.1

###### 2026/09/13

* `Aviso` Esta versión solo mejora la documentación y las herramientas de apoyo; el comportamiento de conversión a pinyin y todas las API de script permanecen sin cambios
* `Mejora` Se rehízo el README en 10 idiomas: se añadieron secciones de uso, inicio rápido, tablas de referencia de estilos y opciones de pinyin, API de script, comprobación rápida, preguntas frecuentes, permisos y seguridad, comparación de plugins hermanos e interfaz del plugin
* `Mejora` El generador de documentación se actualizó a la implementación unificada compartida entre plugins hermanos: detección de desviaciones con `--check`, validación de claves y formas entre idiomas, rechazo de símbolos de ancho completo y comprobaciones de alineación de versiones
* `Mejora` Las instrucciones del centro de plugins (`plugin_instruction.md`) se incorporaron a la misma cadena de generación JSON multilingüe, eliminando el mantenimiento de fuentes duplicadas
* `Mejora` Se añadió la hoja de ruta ROADMAP.md y se establecieron referencias cruzadas bidireccionales y una comparación con el plugin hermano Pinyin4j
* `Mejora` Unificar el diseño del README y la gestión de versiones de la plataforma Gradle
* `Mejora` La verificación de compilación rechaza dependencias nativas accidentales y genera un informe JSON
* `Mejora` Recursos traducidos coherentes, activación explícita del complemento y validación de los paquetes de publicación

# v1.0.0

###### 2026/07/15

* `Función` Servicio del plugin Pinyin: ID de plugin `pinyin`, descubierto e invocado automáticamente por AutoJs6 mediante `org.autojs.plugin.PINYIN`
* `Función` API de conversión: `pinyin.convert(text, options)` devuelve un arreglo 2D de candidatos con un método de combinación `compact()`, y `pinyin.simple(text)` devuelve una cadena compacta
* `Función` API de consulta de diccionarios: `pinyin.fromCodePoint(codePoint)` consulta el registro de lecturas de un carácter y `pinyin.fromPhrase(phrase)` consulta las lecturas de palabras
* `Función` Seis estilos de pinyin (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) más el modo de apellidos (`SURNAME`)
* `Función` Soporte de polifonía y segmentación: diccionarios de caracteres, palabras y segmentación más un modelo HMM incluidos, con las opciones `segment` / `heteronym` / `group` disponibles según se necesite
* `Función` Recursos multilingües: metadatos del plugin e instrucciones disponibles en 10 idiomas
* `Función` README y CHANGELOG generados como Markdown multilingüe desde fuentes JSON mediante `.python/generate_markdown.py`
