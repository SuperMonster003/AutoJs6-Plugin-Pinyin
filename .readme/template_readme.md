<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="{{ repo_url }}/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="{{ repo_url }}/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="{{ icon_alt }}" border="0" width="128" />
    </picture>
  </p>

  <p>{{ text_plugin_synopsis }}</p>

  <p>
    <a href="{{ repo_url }}/releases"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/{{ repo_slug }}?label=Release"/></a>
    <a href="{{ repo_url }}/issues"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues/{{ repo_slug }}?color=A24232&label=Issues"/></a>
    <a href="{{ license_url }}"><img alt="GitHub License" src="https://img.shields.io/github/license/{{ repo_slug }}?color=534BAE&label=License"/></a>
  </p>
</div>

******

### {{ h3_languages_with_ascii }}

******

{{ p_languages_all_supported_for_readme }}:

{{ placeholder_ul_languages_all_supported }}

******

### {{ h3_introduction }}

******

{{ p_introduction_what }}

{{ p_introduction_how }}

{{ p_introduction_extra }}

******

### {{ h3_features }}

******

{{ placeholder_features }}

******

### {{ h3_usage }}

******

{{ placeholder_usage_steps }}

> {{ p_usage_note }}

******

### {{ h3_quick_start }}

******

{{ p_quick_start_basic }}:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

{{ p_quick_start_heteronym }}:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

{{ p_quick_start_advanced }}:

```javascript
console.log(pinyin.simple("音乐重要", false, true));
console.log(pinyin.convert("单田芳", { mode: "SURNAME" }));
console.log(pinyin.convert("六安", { mode: "PLACE_NAME" })); // [["lù"], ["ān"]]
console.log(pinyin.convert("六安", {
  customDictionary: { "六安": [["liú"], ["ān"]] },
})); // [["liú"], ["ān"]]
```

******

### {{ h3_styles }}

******

{{ p_styles_intro }}:

| {{ th_style_name }} | {{ th_style_output }} | {{ th_style_desc }} |
|---|---|---|
| `TONE` | `zhōng` | {{ td_style_tone }} |
| `TONE2` | `zhong1` | {{ td_style_tone2 }} |
| `TO3NE` | `zho1ng` | {{ td_style_to3ne }} |
| `NORMAL` | `zhong` | {{ td_style_normal }} |
| `INITIALS` | `zh` | {{ td_style_initials }} |
| `FIRST_LETTER` | `z` | {{ td_style_first_letter }} |

{{ p_styles_note }}

******

### {{ h3_options }}

******

{{ p_options_intro }}:

| {{ th_option_name }} | {{ th_option_default }} | {{ th_option_desc }} |
|---|---|---|
| `style` | `TONE` | {{ td_option_style }} |
| `mode` | `NORMAL` | {{ td_option_mode }} |
| `segment` | `false` | {{ td_option_segment }} |
| `heteronym` | `false` | {{ td_option_heteronym }} |
| `group` | `false` | {{ td_option_group }} |
| `customDictionary` | `{}` | {{ td_option_custom_dictionary }} |

{{ p_options_note }}

******

### {{ h3_script_api }}

******

{{ p_script_api_intro }}:

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

{{ placeholder_api_points }}

#### Node.js

{{ p_node_api_note }}:

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

### {{ h3_self_check }}

******

{{ p_self_check_intro }}:

```javascript
console.log(pinyin.simple("拼音"));
```

{{ p_self_check_result }}

******

### {{ h3_faq }}

******

{{ placeholder_faq }}

******

### {{ h3_security }}

******

{{ p_security_intro }}

{{ placeholder_security_points }}

{{ p_security_permission }}

******

### {{ h3_sibling }}

******

{{ p_sibling_intro }}:

| {{ th_sibling_aspect }} | [Pinyin]({{ repo_url }}) | [Pinyin4j]({{ pinyin4j_repo_url }}) |
|---|---|---|
| {{ th_sibling_impl }} | {{ td_sibling_impl_pinyin }} | {{ td_sibling_impl_pinyin4j }} |
| {{ th_sibling_global }} | `pinyin` | `pinyin4j` |
| {{ th_sibling_heteronym }} | {{ td_sibling_heteronym_pinyin }} | {{ td_sibling_heteronym_pinyin4j }} |
| {{ th_sibling_segment }} | {{ td_sibling_segment_pinyin }} | {{ td_sibling_segment_pinyin4j }} |
| {{ th_sibling_surname }} | {{ td_sibling_surname_pinyin }} | {{ td_sibling_surname_pinyin4j }} |
| {{ th_sibling_output }} | {{ td_sibling_output_pinyin }} | {{ td_sibling_output_pinyin4j }} |
| {{ th_sibling_styles }} | {{ td_sibling_styles_pinyin }} | {{ td_sibling_styles_pinyin4j }} |
| {{ th_sibling_size }} | {{ td_sibling_size_pinyin }} | {{ td_sibling_size_pinyin4j }} |
| {{ th_sibling_scenario }} | {{ td_sibling_scenario_pinyin }} | {{ td_sibling_scenario_pinyin4j }} |

{{ p_sibling_note }}

******

### {{ h3_plugin_interface }}

******

{{ p_plugin_interface }}:

```text
application id: {{ plugin_application_id }}
plugin id: {{ plugin_id }}
engine: {{ plugin_engine }}
variant: {{ plugin_variant }}
discovery action: {{ discovery_action }}
discovery category: {{ discovery_category }}
wake action: {{ wake_action }}
binder interface: {{ binder_interface }}
binder methods: getInfo / convert / simple / fromCodePoint / fromPhrase
minimum host build: {{ required_host_version_code }}
native library: none (pure JVM, all ABIs)
```

{{ p_contract_service }}

******

### {{ h3_roadmap }}

******

{{ p_roadmap }}

- [{{ text_link_roadmap }}]({{ roadmap_url }})

******

### {{ h3_release_history }}

******

{{ placeholder_latest_release_history }}

##### {{ h5_for_more_release_history }}

* {{ placeholder_read_more_in_changelog_md }}

******

### {{ h3_build }}

******

{{ p_build_intro }}

{{ p_build_debug }}:

```powershell
.\gradlew.bat :app:assembleDebug
```

{{ p_build_test }}:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

{{ p_build_release }}:

```powershell
.\gradlew.bat :app:assembleRelease
```

{{ p_build_artifacts }}:

```powershell
py scripts\release\prepare_release.py
```

{{ p_build_docs_check }}:

```powershell
py .python\generate_markdown.py --check
```

{{ p_build_params }}

******

### {{ h3_resource_layout }}

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

{{ p_resource_layout }}

******

### {{ h3_license }}

******

{{ p_license }}

******

### {{ h3_links }}

******

- {{ text_link_autojs6_docs_pinyin }}: {{ docs_pinyin_url }}
- {{ text_link_autojs6 }}: {{ autojs6_url }}
- {{ text_link_pinyin4j_plugin }}: {{ pinyin4j_repo_url }}
- {{ text_link_hotoo_pinyin }}: {{ hotoo_pinyin_url }}
- {{ text_link_jieba_analysis }}: {{ jieba_analysis_url }}
