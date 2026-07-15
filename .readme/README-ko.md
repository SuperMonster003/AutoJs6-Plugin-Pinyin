<!--suppress HtmlDeprecatedAttribute, HttpUrlsUsage -->

<div align="center">
  <p>
    <picture>
      <source srcset="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap-night/ic_launcher.png?raw=true" media="(prefers-color-scheme: dark)" />
      <img src="https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/res/mipmap/ic_launcher.png?raw=true" alt="autojs6-plugin-pinyin-ic-launcher" border="0" width="128" />
    </picture>
  </p>

  <p>중국어 병음 변환용 Pinyin 플러그인</p>

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

### 언어 (Languages)

******

현재 README.md 는 다음 언어를 지원합니다:

- [简体中文 [zh-Hans]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hans.md)
- [繁體中文 (香港) [zh-Hant-HK]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-HK.md)
- [繁體中文 (台灣) [zh-Hant-TW]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-zh-Hant-TW.md)
- [English [en]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-en.md)
- [Français [fr]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-fr.md)
- [Español [es]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-es.md)
- [日本語 [ja]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ja.md)
- 한국어 [ko] # 현재
- [Русский [ru]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ru.md)
- [العربية [ar]](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.readme/README-ar.md)

******

### 소개

******

AutoJs6 Pinyin 플러그인은 패키지된 문자, 구문, 분절 사전을 사용해 AutoJs6 에 중국어 병음 변환 기능을 제공합니다. 성조 표시, 숫자 성조, 무성조 병음, 성모, 첫 글자, 분절, 다중 발음, 구문, 성씨 모드를 지원합니다.

******

### 기능

******

- `pinyin` 플러그인 서비스를 제공하며 플러그인 ID 는 `pinyin` 입니다.
- `pinyin.convert(text, options)`, `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)`, `pinyin.fromPhrase(phrase)` 등의 AutoJs6 API 를 지원합니다.
- `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` 병음 스타일과 일반 모드, 성씨 모드를 지원합니다.
- Jieba 기반 분절, 다중 발음, 구문 사전, 병음 결과 조합을 지원합니다.
- 플러그인 메타데이터, 사용 설명, README, CHANGELOG 는 스페인어/프랑스어/러시아어/아랍어/일본어/한국어/영어/중국어 간체/홍콩 번체/대만 번체를 지원합니다.

******

### 사용 예

******

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

간단한 연결 문자열 메서드도 사용할 수 있습니다:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

******

### 옵션

******

일반적인 병음 스타일은 다음과 같습니다:

```text
NORMAL, TONE, TONE2, TO3NE,
INITIALS, FIRST_LETTER
```

모드는 다음과 같습니다:

```text
NORMAL, SURNAME, PLACE_NAME, PLACENAME
```

******

### 릴리스 기록

******

# v1.0.0

###### 2026/07/15

* `추가` 플러그인 ID `pinyin`, 엔진 `pinyin` 인 Pinyin 플러그인 서비스를 추가
* `추가` `org.autojs.plugin.PINYIN` 을 통한 호스트 발견 및 호출을 추가
* `추가` `pinyin.convert(text, options)` 가 중첩된 병음 결과를 반환하도록 지원하고, `compact()` 조합은 AutoJs6 호스트가 제공
* `추가` `pinyin.simple(text)`, `pinyin.fromCodePoint(codePoint)`, `pinyin.fromPhrase(phrase)` 를 지원
* `추가` `NORMAL`/`TONE`/`TONE2`/`TO3NE`/`INITIALS`/`FIRST_LETTER` 병음 스타일과 `NORMAL`/`SURNAME`/`PLACE_NAME` 모드를 지원
* `추가` 문자, 구문, 분절 데이터를 포함해 분절, 다중 발음, 구문, 성씨 병음 처리를 지원
* `추가` 스페인어, 프랑스어, 러시아어, 아랍어, 일본어, 한국어, 영어, 중국어 간체, 홍콩 번체, 대만 번체 플러그인 정보와 사용 설명을 추가
* `추가` 다국어 README 및 CHANGELOG Markdown 생성을 위한 JSON 소스와 `.python/generate_markdown.py` 를 추가

##### 더 많은 릴리스 기록

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/.changelog/CHANGELOG-ko.md)

******

### 빌드

******

```powershell
.\gradlew.bat :app:assembleDebug
```

Release 빌드:

```powershell
.\gradlew.bat :app:assembleRelease
```

빌드 매개변수는 `version.properties` 에서 가져옵니다. 현재 최소 SDK 는 24, 대상 SDK 는 36 입니다.

******

### 리소스 구조

******

```text
.readme/lang_*.json
.changelog/lang_*.json
.python/generate_markdown.py
app/src/main/res/values-*/strings.xml
app/src/main/res/raw-*/plugin_instruction.md
```

`strings.xml` 은 현지화된 플러그인 설명을 제공합니다; `plugin_instruction.md` 는 호스트에 표시되는 사용 설명을 제공합니다. README 와 CHANGELOG 는 `.python/generate_markdown.py` 가 JSON 소스에서 생성합니다.

******

### 관련 링크

******

- AutoJs6 Pinyin 문서: https://docs.autojs6.com/#/pinyin
- AutoJs6 프로젝트: https://github.com/SuperMonster003/AutoJs6
