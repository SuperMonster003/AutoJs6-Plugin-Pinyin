<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>Complemento Pinyin para la conversion fonetica del chino</p>

  <p>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/SuperMonster003/AutoJs6-Plugin-Pinyin?label=Release"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues/SuperMonster003/AutoJs6-Plugin-Pinyin?color=A24232&label=Issues"/></a>
    <a href="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/SuperMonster003/AutoJs6-Plugin-Pinyin?color=534BAE&label=License"/></a>
  </p>
</div>

******

### Idiomas (Languages)

******

El README.md actual admite los siguientes idiomas:

- [简体中文 [zh-Hans]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hans.md)
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
- [English [en]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-en.md)
- [Français [fr]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-fr.md)
- Español [es] # actual
- [日本語 [ja]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ja.md)
- [한국어 [ko]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ko.md)
- [Русский [ru]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ru.md)
- [العربية [ar]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ar.md)

******

### Introducción

******

El plugin Pinyin (Pinyin Plugin) aporta a AutoJs6 la conversión sin conexión de chino a pinyin. Una vez instalado, los scripts pueden convertir texto chino a pinyin en varios estilos mediante el objeto global `pinyin`, con soporte para candidatos de caracteres polifónicos, un diccionario de palabras, la segmentación Jieba y un modo de apellidos, útil para ordenar, buscar, indexar por primera letra, anotar fonéticamente y otros escenarios de automatización.

El plugin es un APK de instalación independiente que se ejecuta en su propio proceso; AutoJs6 lo descubre automáticamente mediante el mecanismo de plugins y se comunica con él por AIDL. Los diccionarios de caracteres, palabras y segmentación van todos incluidos (el APK ocupa unos 6 MB), por lo que la conversión ocurre por completo en el dispositivo, sin red. Desde AutoJs6 v6.8.0, el módulo `pinyin` del host se apoya en este plugin. El diseño de la API sigue la biblioteca JavaScript [pinyin](https://github.com/hotoo/pinyin) de amplio uso, así que quien la conozca puede empezar de inmediato.

Este plugin y [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) son plugins hermanos: este incluye diccionarios completos con soporte de polifonía y segmentación para escenarios donde prima la exactitud de las lecturas; Pinyin4j envuelve la clásica biblioteca Java pinyin4j en un paquete de solo unos 0.3 MB para una conversión ligera carácter a carácter. Ambos pueden instalarse a la vez; vea `Comparación De Plugins Hermanos` más abajo.

******

### Funciones Destacadas

******

- Listo para usar: AutoJs6 lo descubre automáticamente tras la instalación, sin reiniciar el host; los scripts usan directamente el objeto global `pinyin`.
- Diccionarios completos: diccionarios de caracteres, palabras y segmentación más un modelo HMM incluidos, totalmente sin conexión y sin peticiones de red.
- Soporte de caracteres polifónicos: la opción `heteronym` devuelve todas las lecturas candidatas de cada carácter, y el diccionario de palabras elige automáticamente las lecturas habituales.
- Segmentación Jieba: la opción `segment` activa la segmentación de palabras para desambiguar los caracteres polifónicos por palabras y mejorar la exactitud en frases completas.
- Seis estilos de pinyin: marcas de tono, tonos numéricos, número tras la final, sin tono, iniciales y primeras letras, cubriendo ordenación, búsqueda y anotación.
- Modos para nombres propios: `SURNAME` prefiere las lecturas de apellidos, mientras que `PLACE_NAME` aplica primero un corpus selecto de topónimos con fuentes rastreables y luego vuelve a la conversión normal.
- Resultados combinables: el arreglo 2D de candidatos devuelto por `convert` incorpora un método `compact()` que despliega todas las combinaciones de lecturas en un paso.
- Multilingüe: metadatos del plugin, instrucciones, README y registro de cambios disponibles en 10 idiomas.

******

### Uso

******

1. Actualice AutoJs6 a la compilación interna 3923 (6.7.1 Alpha4) o superior; desde la v6.8.0 la conversión a pinyin está delegada por completo en los plugins, por lo que se recomienda la versión más reciente.
2. Descargue el APK del plugin desde la página [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) e instálelo en el dispositivo que ejecuta AutoJs6, o instálelo en línea directamente desde el centro de plugins de AutoJs6.
3. Abra el centro de plugins de AutoJs6 y confirme que el plugin `Pinyin` está reconocido, autorizado y habilitado.
4. Llame al objeto global `pinyin` en sus scripts como se muestra en `Inicio Rápido` más abajo; también puede ejecutar antes la `Comprobación Rápida` para confirmar que el plugin funciona.

> El plugin se publica como un único APK universal (implementación puramente JVM, sin variantes por arquitectura de CPU) y admite dispositivos con Android 7.0 (API 24) o superior. No tiene interfaz propia ni crea icono de lanzador; AutoJs6 lo descubre y lo gestiona de forma unificada.

******

### Inicio Rápido

******

Conversión básica: `convert` devuelve un arreglo 2D de candidatos, `simple` devuelve una cadena compacta:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

Caracteres polifónicos: la opción `heteronym` devuelve todas las lecturas candidatas y `compact()` despliega las combinaciones:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

Desambiguación por segmentación, modo de apellidos y modo de topónimos:

```javascript
console.log(pinyin.simple("音乐重要", false, true));
console.log(pinyin.convert("单田芳", { mode: "SURNAME" }));
console.log(pinyin.convert("六安", { mode: "PLACE_NAME" })); // [["lù"], ["ān"]]
console.log(pinyin.convert("六安", {
  customDictionary: { "六安": [["liú"], ["ān"]] },
})); // [["liú"], ["ān"]]
```

******

### Estilos De Pinyin

******

La opción `style` controla el estilo de salida, ilustrado con "中" (zhōng):

| Estilo | Salida | Descripción |
|---|---|---|
| `TONE` | `zhōng` | Marcas de tono sobre la final (predeterminado) |
| `TONE2` | `zhong1` | Dígito de tono 0-4 añadido al final de la sílaba |
| `TO3NE` | `zho1ng` | Dígito de tono justo después de la final |
| `NORMAL` | `zhong` | Sin tonos |
| `INITIALS` | `zh` | Solo la inicial (cadena vacía para sílabas sin inicial) |
| `FIRST_LETTER` | `z` | Solo la primera letra de la sílaba |

El valor de `style` no distingue mayúsculas de minúsculas y acepta una cadena (como `"TONE2"`) o una constante (como `pinyin.STYLE_TONE2`).

******

### Opciones

******

`pinyin.convert(text, options)` admite las siguientes opciones:

| Opción | Predeterminado | Descripción |
|---|---|---|
| `style` | `TONE` | Estilo de pinyin, vea `Estilos De Pinyin` más arriba |
| `mode` | `NORMAL` | Modo de conversión: `NORMAL` para texto normal, `SURNAME` para apellidos, `PLACE_NAME` para lecturas selectas de topónimos |
| `segment` | `false` | Activa la segmentación Jieba y usa el diccionario de palabras para desambiguar los caracteres polifónicos |
| `heteronym` | `false` | Devuelve todas las lecturas candidatas de cada carácter en lugar de solo la primera |
| `group` | `false` | Agrupa los candidatos de pinyin por palabras segmentadas (úselo junto con `segment`) |
| `customDictionary` | `{}` | Sobrescrituras de lectura Han para esta llamada con el formato `{ frase: [[candidatos con tono], ...] }`; prevalece la coincidencia más larga, no se guardan y requieren un host AutoJs6 y un plugin compatibles |

Los modos también aceptan constantes (como `pinyin.MODE_PLACE_NAME`). `PLACE_NAME` usa la coincidencia más larga en un corpus pequeño revisado manualmente; el texto no incluido vuelve a `NORMAL`. No es un nomenclátor nacional completo; consulte el [corpus y sus fuentes](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/dictionaries/place-names.md).

******

### API De Script

******

El objeto global `pinyin` ofrece los siguientes métodos (llamar directamente a `pinyin(text, options)` equivale a `pinyin.convert`):

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

- `convert` devuelve un arreglo 2D: cada carácter chino o posición de carácter de una palabra ocupa una fila con sus lecturas candidatas; los caracteres no cubiertos y no chinos conservan una fila tal cual. El arreglo devuelto incorpora un método `compact()` que despliega todas las combinaciones de lecturas.
- `simple` devuelve una cadena compacta: se concatena la primera lectura de cada carácter; pase `true` como segundo argumento para tonos numéricos (estilo TONE2, sin tonos en caso contrario) y `true` como tercer argumento para activar la segmentación.
- `fromCodePoint` consulta el registro original del diccionario para un punto de código (candidatos con tono separados por comas) y devuelve `null` cuando no está cubierto.
- `fromPhrase` consulta el diccionario de palabras y devuelve las lecturas candidatas de cada posición de carácter de la palabra; devuelve un arreglo vacío cuando no está cubierta.
- Todos los métodos responden de forma síncrona; la primera llamada inicializa los diccionarios incluidos y puede tardar un poco más.

#### Node.js

En el entorno Node.js, invoque el mismo proveedor mediante la fachada pública `autojs6:bridge` y declare explícitamente la capacidad `pinyin`:

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

### Comprobación Rápida

******

Tras instalar y habilitar el plugin, ejecute esta única línea:

```javascript
console.log(pinyin.simple("拼音"));
```

Una salida `pinyin` significa que el plugin funciona correctamente.

******

### Preguntas Frecuentes

******

#### ¿Cómo confirmo que el plugin está activo?

Abra el centro de plugins de AutoJs6: ver el plugin `Pinyin` listado y habilitado significa que el host lo ha reconocido. Luego ejecute el script de `Comprobación Rápida` de más arriba; una salida `pinyin` confirma que funciona.

#### ¿Un script indica que falta el plugin o que `pinyin` no está disponible?

Asegúrese de que la compilación interna de AutoJs6 sea al menos 3923 y de que el plugin esté instalado, autorizado y habilitado en el centro de plugins. Desde AutoJs6 v6.8.0 el host ya no incluye una implementación de pinyin, así que toda la conversión está delegada en este plugin.

#### ¿Por qué no hay icono en la lista de aplicaciones ni en la pantalla de inicio?

Es lo esperado. El plugin no tiene interfaz propia ni crea icono de lanzador; tras la instalación, AutoJs6 lo descubre y lo invoca en segundo plano, y toda interacción ocurre dentro de AutoJs6.

#### ¿Un carácter polifónico no se convierte como espera?

De forma predeterminada se usa la primera lectura de cada carácter aislado. Active la opción `segment` para desambiguar mediante el diccionario de palabras y la segmentación (por ejemplo `pinyin.simple(text, false, true)`), o use la opción `heteronym` para obtener todos los candidatos. Si una palabra común sigue leyéndose mal, infórmelo mediante [Issues](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues) para mejorar los diccionarios.

#### ¿Cómo elijo entre este plugin y su hermano Pinyin4j?

Elija este plugin cuando necesite polifonía, segmentación, palabras o lecturas de apellidos; elija [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) cuando solo necesite una conversión ligera carácter a carácter y le importe el tamaño del APK. No entran en conflicto y pueden instalarse juntos; vea `Comparación De Plugins Hermanos` más abajo.

#### ¿El plugin accede a la red o solicita permisos sensibles?

No. Todos los diccionarios van incluidos en el APK y la conversión ocurre en el dispositivo; el manifiesto solo declara el permiso de plugin necesario para comunicarse con AutoJs6, sin permisos de red, almacenamiento ni otros permisos sensibles del sistema.

#### ¿Por qué el APK ocupa unos 6 MB?

El APK incluye cuatro conjuntos de datos: un diccionario de caracteres, un diccionario de palabras, un léxico de segmentación y un modelo HMM, cambiando tamaño por un funcionamiento totalmente sin conexión y mayor exactitud. Si el tamaño le importa más, considere el plugin hermano [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) de unos 0.3 MB.

#### ¿Por qué se rechaza `customDictionary` o una llamada Pinyin desde Node.js?

Estas rutas requieren versiones compatibles de AutoJs6 y del plugin Pinyin. Las llamadas Node.js deben declarar `permissions: ["pinyin"]`. El diccionario personalizado solo se aplica a una llamada y debe respetar los límites documentados de entradas, candidatos, combinaciones y 64 KiB.

******

### Permisos Y Seguridad

******

El plugin está diseñado para mantener al mínimo tanto su superficie de datos como su superficie de permisos:

- Permisos mínimos: el manifiesto solo declara el permiso de plugin de AutoJs6 (`org.autojs.permission.PLUGIN`), sin permisos de red, almacenamiento, cámara ni otros permisos sensibles del sistema.
- Conversión local: el texto a convertir viaja solo por Binder dentro del dispositivo, los diccionarios van totalmente incluidos, todo permanece sin conexión y ningún dato sale del dispositivo.
- Firma y autorización: AutoJs6 verifica la firma del plugin, y el plugin debe autorizarse y habilitarse en el centro de plugins antes de que los scripts puedan llamarlo; el servicio y la entrada de activación están protegidos por el permiso de plugin, por lo que las aplicaciones de terceros no pueden invocarlos directamente.
- Abierto y auditable: el código del plugin, el empaquetado de los diccionarios y la cadena de generación de documentación son totalmente de código abierto.

Obtenga el APK del plugin solo desde la página oficial [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) o el centro de plugins de AutoJs6; un APK de origen desconocido puede estar alterado aunque el nombre y la versión parezcan idénticos.

******

### Comparación De Plugins Hermanos

******

AutoJs6 ofrece dos plugins oficiales de pinyin con enfoques distintos, y pueden instalarse a la vez:

| Aspecto | [Pinyin](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) | [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) |
|---|---|---|
| Implementación subyacente | Diccionarios incluidos + segmentación Jieba | Clásica biblioteca Java `pinyin4j` |
| Objeto global | `pinyin` | `pinyin4j` |
| Polifonía | Con soporte, todos los candidatos disponibles | Sin soporte, solo la primera lectura |
| Segmentación y palabras | Con soporte (diccionario de palabras + Jieba) | Sin soporte, conversión carácter a carácter |
| Modo de apellidos | Con soporte | Sin soporte |
| Forma de salida | Arreglo 2D de candidatos (combinable vía `compact()`) o cadena compacta | Cadena con separador configurable |
| Estilos y formatos | 6 estilos de pinyin | 3 formatos de tono + mayúsculas/minúsculas + representación de `ü` |
| Tamaño del APK | Unos 6 MB (diccionarios incluidos) | Unos 0.3 MB |
| Ideal para | Exactitud primero: polifonía, palabras, nombres de personas | Tamaño y sencillez primero: conversión rápida carácter a carácter |

Los dos plugins ni dependen entre sí ni entran en conflicto; con ambos instalados, los scripts pueden llamar a `pinyin` y `pinyin4j` según convenga. Vea [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) para más detalles.

******

### Interfaz Del Plugin

******

La siguiente información está dirigida a los desarrolladores del host AutoJs6 y de plugins; el host usa estos identificadores para descubrir el plugin y negociar capacidades:

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

`PinyinPluginService` responde a la acción `org.autojs.plugin.PINYIN` (categoría `pinyin`) y expone 5 métodos a través de la interfaz AIDL `IPinyinPlugin`; `convert` y `fromPhrase` devuelven arreglos 2D como cadenas JSON, y las opciones viajan en un `Bundle` (claves: `mode` / `style` / `segment` / `heteronym` / `group` / `custom_dictionary_json`). Los diccionarios personalizados requieren la capacidad `pinyin.customDictionary.v1`. Tanto el servicio como `WakeActivity` están protegidos por el permiso `org.autojs.permission.PLUGIN`, por lo que las aplicaciones de terceros no pueden invocarlos directamente.

******

### Hoja De Ruta

******

Las capacidades planificadas del plugin y su avance se mantienen como una lista marcable en ROADMAP.md, organizada por hitos con criterios de aceptación, cubriendo el modo de topónimos, la evolución de los diccionarios, los diccionarios personalizados, el rendimiento y la integración continua. Los elementos sin marcar expresan intención y no capacidades actuales; la discusión mediante Issues es bienvenida.

- [Ver ROADMAP.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/ROADMAP.md)

******

### Historial De Versiones

******

#### v1.0.2

_2026/09/13_

- `Corrección` Mantener la fecha de versión del complemento en inglés sin depender del idioma del equipo de compilación
- `Mejora` Recursos traducidos coherentes, activación explícita del complemento y validación de los paquetes de publicación

#### v1.0.1

_2026/09/11_

- `Aviso` Esta versión solo mejora la documentación y las herramientas de apoyo; el comportamiento de conversión a pinyin y todas las API de script permanecen sin cambios
- `Mejora` Se rehízo el README en 10 idiomas: se añadieron secciones de uso, inicio rápido, tablas de referencia de estilos y opciones de pinyin, API de script, comprobación rápida, preguntas frecuentes, permisos y seguridad, comparación de plugins hermanos e interfaz del plugin
- `Mejora` El generador de documentación se actualizó a la implementación unificada compartida entre plugins hermanos: detección de desviaciones con `--check`, validación de claves y formas entre idiomas, rechazo de símbolos de ancho completo y comprobaciones de alineación de versiones
- `Mejora` Las instrucciones del centro de plugins (`plugin_instruction.md`) se incorporaron a la misma cadena de generación JSON multilingüe, eliminando el mantenimiento de fuentes duplicadas
- `Mejora` Se añadió la hoja de ruta ROADMAP.md y se establecieron referencias cruzadas bidireccionales y una comparación con el plugin hermano Pinyin4j
- `Mejora` Unificar el diseño del README y la gestión de versiones de la plataforma Gradle
- `Mejora` La verificación de compilación rechaza dependencias nativas accidentales y genera un informe JSON

#### v1.0.0

_2026/07/15_

- `Función` Servicio del plugin Pinyin: ID de plugin `pinyin`, descubierto e invocado automáticamente por AutoJs6 mediante `org.autojs.plugin.PINYIN`
- `Función` API de conversión: `pinyin.convert(text, options)` devuelve un arreglo 2D de candidatos con un método de combinación `compact()`, y `pinyin.simple(text)` devuelve una cadena compacta
- `Función` API de consulta de diccionarios: `pinyin.fromCodePoint(codePoint)` consulta el registro de lecturas de un carácter y `pinyin.fromPhrase(phrase)` consulta las lecturas de palabras
- `Función` Seis estilos de pinyin (`NORMAL` / `TONE` / `TONE2` / `TO3NE` / `INITIALS` / `FIRST_LETTER`) más el modo de apellidos (`SURNAME`)
- `Función` Soporte de polifonía y segmentación: diccionarios de caracteres, palabras y segmentación más un modelo HMM incluidos, con las opciones `segment` / `heteronym` / `group` disponibles según se necesite
- `Función` Recursos multilingües: metadatos del plugin e instrucciones disponibles en 10 idiomas
- `Función` README y CHANGELOG generados como Markdown multilingüe desde fuentes JSON mediante `.python/generate_markdown.py`

##### Para más historial de versiones

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/assets/doc/CHANGELOG-es.md)

******

### Compilación

******

Esta sección está dirigida a desarrolladores que quieran compilar el plugin desde el código fuente.

Compilar un APK debug:

```powershell
.\gradlew.bat :app:assembleDebug
```

Ejecutar las pruebas unitarias JVM y compilar el APK de pruebas instrumentation:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

Compilar un APK release (un único paquete universal; la firma es automática una vez configurado el archivo no rastreado `sign.properties`):

```powershell
.\gradlew.bat :app:assembleRelease
```

Compilar y verificar el APK universal firmado con un solo comando, y generar `SHA256SUMS.txt` y `RELEASE_NOTES.md` a partir del CHANGELOG en inglés:

```powershell
py scripts\release\prepare_release.py
```

Comprobar que las fuentes de la documentación multilingüe y los archivos generados están sincronizados (la integración continua también lo comprueba):

```powershell
py .python\generate_markdown.py --check
```

Los parámetros de compilación están centralizados en `version.properties`: SDK mínimo 24 (Android 7.0), SDK objetivo 36, versión actual 1.0.2.

******

### Localización Y Generación De Docs

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

`strings.xml` contiene la descripción localizada del plugin, y `plugin_instruction.md` contiene las instrucciones mostradas en el centro de plugins del host. README, registro de cambios e instrucciones se generan desde fuentes JSON: edite las fuentes bajo `.readme/` y `.changelog/`, luego ejecute `py .python/generate_markdown.py` para regenerar todos los artefactos; los artefactos generados nunca se editan a mano. Ejecute `py .python/generate_markdown.py --check` para verificar que fuentes y artefactos están sincronizados.

******

### Licencia

******

El código del proyecto está licenciado bajo la [Mozilla Public License 2.0](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE). La implementación de segmentación incluida está portada del proyecto [jieba-analysis](https://github.com/huaban/jieba-analysis), y el diseño de la API sigue la biblioteca [pinyin](https://github.com/hotoo/pinyin).

******

### Enlaces

******

- Documentación de AutoJs6 Pinyin: https://docs.autojs6.com/#/pinyin
- Proyecto AutoJs6: https://github.com/SuperMonster003/AutoJs6
- Plugin hermano Pinyin4j: https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j
- Biblioteca pinyin (referencia de diseño de la API): https://github.com/hotoo/pinyin
- Proyecto jieba-analysis: https://github.com/huaban/jieba-analysis


[16 KB page alignment and build verification](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/16kb.md)
