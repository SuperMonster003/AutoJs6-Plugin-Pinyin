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

Pinyin 플러그인 (Pinyin Plugin) 은 AutoJs6 에 오프라인 중국어 병음 변환 기능을 제공합니다. 설치 후 스크립트는 전역 객체 `pinyin` 을 통해 중국어 텍스트를 다양한 스타일의 병음으로 변환할 수 있으며, 다음자 후보, 어구 사전, Jieba 단어 분할, 성씨 모드를 지원하여 정렬, 검색, 첫 글자 색인, 발음 표기 등 자동화 시나리오에 적합합니다.

플러그인은 독립적으로 설치되는 APK 로 자체 프로세스에서 실행되며, AutoJs6 이 플러그인 메커니즘을 통해 자동으로 발견하고 AIDL 로 통신합니다. 단일 한자, 어구, 단어 분할 사전이 모두 내장되어 (설치 패키지 약 6 MB) 변환이 전부 기기 안에서 이루어지고 네트워크가 필요 없습니다. AutoJs6 v6.8.0 부터 호스트의 `pinyin` 모듈은 본 플러그인이 구현을 제공합니다. API 설계는 JavaScript 생태계에서 널리 쓰이는 [pinyin](https://github.com/hotoo/pinyin) 라이브러리에 맞추었으므로, 이 라이브러리에 익숙한 사용자는 바로 사용할 수 있습니다.

본 플러그인과 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) 는 서로 자매 플러그인입니다: 본 플러그인은 사전이 완비되어 다음자와 단어 분할을 지원하므로 발음 정확성을 중시하는 시나리오에 적합하고, Pinyin4j 는 클래식 Java 라이브러리 pinyin4j 기반으로 크기가 약 0.3 MB 에 불과해 가벼운 글자 단위 변환에 적합합니다. 둘은 동시에 설치할 수 있으며, 자세한 내용은 아래 `자매 플러그인 비교` 를 참고하세요.

******

### 기능 하이라이트

******

- 바로 사용 가능: 설치 후 AutoJs6 이 자동으로 발견하며, 호스트 재시작 없이 스크립트에서 전역 객체 `pinyin` 을 바로 사용할 수 있습니다.
- 완비된 사전: 단일 한자, 어구, 단어 분할 세 가지 사전과 HMM 모델을 내장하여 완전히 오프라인으로 동작하며 네트워크 요청을 전혀 보내지 않습니다.
- 다음자 지원: `heteronym` 옵션은 각 글자의 모든 후보 발음을 반환하고, 어구 사전은 자주 쓰이는 발음을 자동으로 선택합니다.
- Jieba 단어 분할: `segment` 옵션으로 단어 분할을 활성화하면 어구 단위로 다음자 발음을 가려내어 문장 전체의 발음 표기 정확도를 높입니다.
- 여섯 가지 병음 스타일: 성조 기호, 숫자 성조, 운모 뒤 숫자, 성조 없음, 성모만, 첫 글자만을 갖추어 정렬/검색/발음 표기 등 시나리오를 아우릅니다.
- 고유명사 모드: `SURNAME` 은 성씨 전용 발음을 우선하며, `PLACE_NAME` 은 출처를 추적할 수 있는 엄선된 지명 말뭉치를 먼저 적용한 뒤 일반 변환으로 대체합니다.
- 조합 가능한 결과: `convert` 가 반환하는 2차원 후보 배열에는 `compact()` 메서드가 딸려 있어 모든 발음 조합을 한 번에 펼칠 수 있습니다.
- 다국어: 플러그인 정보, 사용 설명, README, 변경 로그가 10 개 언어로 제공됩니다.

******

### 사용 방법

******

1. AutoJs6 을 내부 빌드 3923 (6.7.1 Alpha4) 이상으로 업그레이드합니다; v6.8.0 부터 병음 기능은 전적으로 플러그인이 담당하므로 최신 버전 사용을 권장합니다.
2. [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) 페이지에서 플러그인 APK 를 내려받아 AutoJs6 이 실행되는 기기에 설치하거나, AutoJs6 의 플러그인 센터에서 바로 온라인으로 설치합니다.
3. AutoJs6 의 플러그인 센터를 열어 `Pinyin` 플러그인이 인식되었는지 확인하고, 승인을 완료하여 활성화 상태로 만듭니다.
4. 스크립트에서 전역 객체 `pinyin` 을 바로 호출합니다. 아래 `빠른 시작` 예시를 참고하세요; 먼저 `자가 점검` 을 실행하여 플러그인이 동작하는지 확인할 수도 있습니다.

> 플러그인은 범용 설치 패키지 하나만 제공하며 (순수 JVM 구현으로 CPU 아키텍처를 구분하지 않음), Android 7.0 (API 24) 이상 기기를 지원합니다. 플러그인은 독립된 화면이 없고 설치 후 홈 화면에 아이콘을 만들지 않으며, AutoJs6 이 일괄 발견하고 관리합니다.

******

### 빠른 시작

******

기본 변환: `convert` 는 2차원 후보 배열을, `simple` 은 간결한 문자열을 반환합니다:

```javascript
console.log(pinyin.convert("中心"));                     // [["zhōng"], ["xīn"]]
console.log(pinyin.convert("中心", { style: "TONE2" })); // [["zhong1"], ["xin1"]]
console.log(pinyin.simple("拼音插件"));                  // "pinyinchajian"
console.log(pinyin.simple("拼音插件", true));            // "pin1yin1cha1jian4"
```

다음자: `heteronym` 옵션은 모든 후보 발음을 반환하고, `compact()` 는 발음 조합으로 펼칩니다:

```javascript
let result = pinyin.convert("重庆", { heteronym: true });
console.log(result);
console.log(result.compact());
```

단어 분할을 통한 발음 판별, 성씨 모드와 지명 모드:

```javascript
console.log(pinyin.simple("音乐重要", false, true));
console.log(pinyin.convert("单田芳", { mode: "SURNAME" }));
console.log(pinyin.convert("六安", { mode: "PLACE_NAME" })); // [["lù"], ["ān"]]
console.log(pinyin.convert("六安", {
  customDictionary: { "六安": [["liú"], ["ān"]] },
})); // [["liú"], ["ān"]]
```

******

### 병음 스타일

******

`style` 옵션은 병음 출력 스타일을 제어합니다. "中" (zhōng) 을 예로 듭니다:

| 스타일 | 출력 | 설명 |
|---|---|---|
| `TONE` | `zhōng` | 성조 기호를 운모 위에 표기 (기본값) |
| `TONE2` | `zhong1` | 성조를 숫자 0-4 로 음절 끝에 추가 |
| `TO3NE` | `zho1ng` | 성조 숫자를 운모 바로 뒤에 배치 |
| `NORMAL` | `zhong` | 성조 없음 |
| `INITIALS` | `zh` | 성모만 반환 (성모가 없는 글자는 빈 문자열) |
| `FIRST_LETTER` | `z` | 병음 첫 글자만 반환 |

`style` 값은 대소문자를 구분하지 않으며, 문자열 (예: `"TONE2"`) 또는 상수 (예: `pinyin.STYLE_TONE2`) 로 전달할 수 있습니다.

******

### 옵션

******

`pinyin.convert(text, options)` 는 다음 옵션을 지원합니다:

| 옵션 | 기본값 | 설명 |
|---|---|---|
| `style` | `TONE` | 병음 스타일, 위의 `병음 스타일` 참고 |
| `mode` | `NORMAL` | 변환 모드: `NORMAL` 일반 텍스트, `SURNAME` 성씨 발음, `PLACE_NAME` 엄선된 지명 발음 |
| `segment` | `false` | Jieba 단어 분할을 활성화하고 어구 사전으로 다음자 발음을 판별 |
| `heteronym` | `false` | 첫 번째 발음만이 아니라 각 글자의 모든 후보 발음을 반환 |
| `group` | `false` | 분할된 어구 단위로 병음 후보를 병합 (`segment` 와 함께 사용) |
| `customDictionary` | `{}` | 현재 호출에만 적용되는 한자 발음 재정의이며 형식은 `{ 어구: [[성조 후보], ...] }` 입니다. 최장 일치가 우선하고 저장되지 않으며 호환되는 AutoJs6 호스트와 플러그인이 필요합니다 |

모드는 상수 (예: `pinyin.MODE_PLACE_NAME`) 로도 전달할 수 있습니다. `PLACE_NAME` 은 소규모 수동 검토 말뭉치에서 최장 일치를 사용하며, 미수록 텍스트는 `NORMAL` 로 대체됩니다. 전국 지명의 완전한 목록은 아닙니다. [말뭉치와 출처](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/dictionaries/place-names.md) 를 참고하세요.

******

### 스크립트 API

******

전역 객체 `pinyin` 은 다음 메서드를 제공합니다 (`pinyin(text, options)` 를 직접 호출하는 것은 `pinyin.convert` 와 같습니다):

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

- `convert` 는 2차원 배열을 반환합니다: 한자 또는 어구의 각 글자 자리가 한 행을 차지하고 행 안은 후보 발음입니다; 사전에 없는 문자와 중국어가 아닌 문자는 그대로 한 행을 차지합니다. 반환된 배열에는 `compact()` 메서드가 딸려 있어 모든 발음 조합으로 펼칠 수 있습니다.
- `simple` 은 간결한 문자열을 반환합니다: 글자마다 첫 번째 발음을 골라 바로 이어 붙입니다; 두 번째 인자가 `true` 이면 숫자 성조 (TONE2 스타일) 로 출력하고, 아니면 성조 없이 출력합니다; 세 번째 인자가 `true` 이면 단어 분할을 활성화합니다.
- `fromCodePoint` 는 단일 글자 코드 포인트의 사전 원본 발음 기록 (쉼표로 구분된 성조 포함 후보) 을 조회하며, 사전에 없으면 `null` 을 반환합니다.
- `fromPhrase` 는 어구 사전을 조회하여 해당 어구의 각 글자 자리 후보 발음을 반환합니다; 사전에 없으면 빈 배열을 반환합니다.
- 모든 메서드는 동기적으로 반환합니다; 첫 호출 시 내장 사전 초기화가 필요하여 약간 지연될 수 있습니다.

#### Node.js

Node.js 런타임에서는 공개 `autojs6:bridge` facade 로 동일한 provider 를 호출하고 `pinyin` capability 를 명시적으로 선언합니다:

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

### 자가 점검

******

플러그인을 설치하고 활성화한 뒤 다음 한 줄 스크립트를 실행하세요:

```javascript
console.log(pinyin.simple("拼音"));
```

`pinyin` 이 출력되면 플러그인이 정상 동작하는 것입니다.

******

### 자주 묻는 질문

******

#### 플러그인이 정상 동작하는지 어떻게 확인하나요?

AutoJs6 의 플러그인 센터를 열어 `Pinyin` 플러그인이 보이고 활성화 상태이면 호스트가 인식한 것입니다; 이어서 위의 `자가 점검` 스크립트를 실행해 `pinyin` 이 출력되면 정상 동작하는 것입니다.

#### 스크립트가 플러그인이 없다거나 `pinyin` 을 사용할 수 없다는 오류를 보고합니다?

AutoJs6 내부 빌드가 3923 이상인지, 그리고 플러그인 센터에서 플러그인의 설치, 승인, 활성화가 완료되었는지 확인하세요. AutoJs6 v6.8.0 부터 호스트는 병음 구현을 내장하지 않으며, 병음 기능은 전적으로 본 플러그인이 담당합니다.

#### 앱 목록과 홈 화면에 플러그인 아이콘이 없는 이유는 무엇인가요?

정상입니다. 플러그인은 독립된 화면이 없고 홈 화면에 실행 아이콘도 만들지 않습니다. 설치 후 AutoJs6 이 백그라운드에서 자동으로 발견하고 호출하며, 모든 상호작용은 AutoJs6 안에서 이루어집니다.

#### 다음자 발음이 기대와 다릅니다?

기본값으로는 글자마다 첫 번째 발음으로 변환합니다. `segment` 옵션을 켜서 어구 사전과 단어 분할로 발음을 가려내는 것을 권장합니다 (예: `pinyin.simple(text, false, true)`); 모든 후보가 필요하면 `heteronym` 옵션을 사용하세요. 자주 쓰는 단어의 발음이 여전히 틀리면 [Issues](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/issues) 로 알려 주시면 사전 개선에 반영하겠습니다.

#### 자매 플러그인 Pinyin4j 와는 어떻게 선택하나요?

다음자, 단어 분할, 어구, 성씨 발음이 필요하면 본 플러그인을 선택하고, 가벼운 글자 단위 변환만 필요하며 설치 패키지 크기가 중요하면 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) 를 선택하세요. 둘은 충돌하지 않고 동시에 설치할 수 있으며, 자세한 내용은 아래 `자매 플러그인 비교` 를 참고하세요.

#### 플러그인이 네트워크에 접속하거나 민감한 권한을 요청하나요?

아니요. 모든 사전이 설치 패키지에 내장되어 변환이 기기 안에서 이루어집니다; 플러그인 매니페스트는 AutoJs6 과 통신하는 데 필요한 플러그인 권한만 선언하며, 네트워크, 저장소 등 어떤 민감한 시스템 권한도 요청하지 않습니다.

#### 설치 패키지가 약 6 MB 인 이유는 무엇인가요?

설치 패키지에는 단일 한자 사전, 어구 사전, 단어 분할 어휘집, HMM 모델 네 가지 데이터가 내장되어 있으며, 그 대가로 완전한 오프라인 동작과 더 높은 발음 표기 정확도를 얻습니다. 크기가 더 중요하다면 약 0.3 MB 인 자매 플러그인 [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) 를 고려해 보세요.

#### `customDictionary` 또는 Node.js 병음 호출이 거부되는 이유는 무엇인가요?

이 경로에는 호환되는 AutoJs6 와 Pinyin 플러그인 빌드가 필요합니다. Node.js 호출은 `permissions: ["pinyin"]` 를 선언해야 합니다. 사용자 사전은 한 번의 호출에만 적용되며 문서의 항목 수, 후보 수, 조합 수, 64 KiB 제한을 지켜야 합니다.

******

### 권한과 보안

******

플러그인은 설계상 데이터 노출 면과 권한 면을 최대한 좁혔습니다:

- 최소 권한: 플러그인 매니페스트는 AutoJs6 플러그인 권한 (`org.autojs.permission.PLUGIN`) 만 선언하며, 네트워크, 저장소, 카메라 등 어떤 민감한 시스템 권한도 요청하지 않습니다.
- 로컬 변환: 변환할 텍스트는 Binder 를 통해 기기 안에서만 전달되고, 사전이 모두 내장되어 전 과정이 오프라인이므로 데이터가 기기를 벗어나지 않습니다.
- 서명과 승인: AutoJs6 은 플러그인 서명을 검증하며, 플러그인은 플러그인 센터에서 승인되고 활성화된 뒤에만 스크립트가 호출할 수 있습니다; 서비스와 웨이크 진입점은 모두 플러그인 권한으로 보호되어 서드파티 앱이 직접 호출할 수 없습니다.
- 공개적이고 감사 가능: 플러그인 코드, 사전 패키징, 문서 생성 파이프라인이 모두 오픈 소스입니다.

플러그인 설치 패키지는 공식 [Releases](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/releases) 페이지나 AutoJs6 플러그인 센터에서만 받으세요; 출처가 불분명한 패키지는 이름과 버전이 같아 보여도 변조되었을 수 있습니다.

******

### 자매 플러그인 비교

******

AutoJs6 은 공식적으로 두 가지 병음 플러그인을 제공하며, 각자 중점이 달라 동시에 설치할 수 있습니다:

| 비교 항목 | [Pinyin](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) | [Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) |
|---|---|---|
| 내부 구현 | 내장 사전 + Jieba 단어 분할 | 클래식 Java 라이브러리 `pinyin4j` |
| 전역 객체 | `pinyin` | `pinyin4j` |
| 다음자 | 지원, 모든 후보 반환 가능 | 미지원, 항상 첫 번째 발음 |
| 단어 분할과 어구 | 지원 (어구 사전 + Jieba) | 미지원, 글자 단위 변환 |
| 성씨 모드 | 지원 | 미지원 |
| 출력 형태 | 2차원 후보 배열 (`compact()` 로 조합 가능) 또는 간결한 문자열 | 문자열, 구분자 설정 가능 |
| 스타일과 형식 | 병음 스타일 6 종 | 성조 형식 3 종 + 대소문자 + `ü` 표기 방식 |
| 설치 패키지 크기 | 약 6 MB (내장 사전) | 약 0.3 MB |
| 적합한 시나리오 | 발음 정확성 우선: 다음자, 어구, 인명 | 크기와 단순함 우선: 빠른 글자 단위 변환 |

두 플러그인은 서로 의존하지도 충돌하지도 않습니다; 동시에 설치하면 스크립트에서 필요에 따라 `pinyin` 과 `pinyin4j` 를 각각 호출할 수 있습니다. Pinyin4j 플러그인에 대한 자세한 내용은 [AutoJs6-Plugin-Pinyin4j](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j) 를 참고하세요.

******

### 플러그인 인터페이스

******

다음 정보는 AutoJs6 호스트와 플러그인 개발자를 위한 것으로, 호스트는 이 식별자들로 플러그인을 발견하고 기능을 협상합니다:

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

`PinyinPluginService` 는 `org.autojs.plugin.PINYIN` action (category `pinyin`) 에 응답하며, AIDL 인터페이스 `IPinyinPlugin` 를 통해 5 개 메서드를 노출합니다; `convert` 와 `fromPhrase` 는 2차원 배열을 JSON 문자열로 반환하고, 옵션은 `Bundle` 로 전달됩니다 (키: `mode` / `style` / `segment` / `heteronym` / `group` / `custom_dictionary_json`). 사용자 사전에는 `pinyin.customDictionary.v1` capability 가 필요합니다. 서비스와 `WakeActivity` 는 모두 `org.autojs.permission.PLUGIN` 권한으로 보호되어 서드파티 앱이 직접 호출할 수 없습니다.

******

### 개발 로드맵

******

플러그인의 기능 계획과 완료 현황은 ROADMAP.md 에서 체크 가능한 목록으로 관리되며, 마일스톤별로 정리되고 수용 기준이 첨부되어 지명 모드, 사전 발전, 사용자 정의 사전, 성능 최적화, 지속적 통합 등의 방향을 다룹니다. 체크되지 않은 항목은 계획 의도일 뿐 현재 버전의 기능이 아니며, Issues 를 통한 토론을 환영합니다.

- [ROADMAP.md 보기](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/ROADMAP.md)

******

### 릴리스 기록

******

#### v1.0.3

_2026/09/19_

- `수정` 공유 빌드 플러그인 1.8.3을 통해 AGP 9.1의 SDK XML v4 파싱 경고 및 JVM 단위 테스트 조립 작업에서 APK 네이티브 라이브러리 정렬 검사가 잘못 실행되는 문제 해결
- `개선` compileSdk 와 targetSdk 를 37 (Android 17) 로 올리며, 플러그인 동작은 새 대상 버전의 영향을 받지 않음

#### v1.0.2

_2026/09/13_

- `수정` 빌드 환경의 언어와 관계없이 플러그인 버전 날짜를 영어로 유지
- `개선` 다국어 리소스 통일, 명시적인 플러그인 활성화 및 릴리스 산출물 검증

#### v1.0.1

_2026/09/11_

- `힌트` 이 버전은 문서와 관련 도구만 개선하며, 병음 변환 동작과 모든 스크립트 API 는 그대로 유지됩니다
- `개선` 10 개 언어의 README 재구성: 사용 방법, 빠른 시작, 병음 스타일과 옵션 참조 표, 스크립트 API, 자가 점검, 자주 묻는 질문, 권한과 보안, 자매 플러그인 비교, 플러그인 인터페이스 등의 장을 추가
- `개선` 문서 생성 스크립트를 자매 플러그인들이 공유하는 통합 구현으로 업그레이드: `--check` 드리프트 감지, 언어 간 키와 형태 정합 검증, 전각 기호 차단, 버전 정합 검증 지원
- `개선` 플러그인 센터 사용 설명 (`plugin_instruction.md`) 을 동일한 다국어 JSON 생성 파이프라인에 통합하여 이중 소스 유지보수를 제거
- `개선` ROADMAP.md 개발 로드맵을 추가하고 자매 플러그인 Pinyin4j 와 양방향 상호 링크 및 선택 비교를 구축
- `개선` README 레이아웃과 Gradle 플랫폼 버전 관리 방식을 통일
- `개선` 빌드 시 의도하지 않은 네이티브 의존성을 거부하고 JSON 보고서 생성

##### 더 많은 릴리스 기록은 다음을 참고

* [CHANGELOG.md](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/app/src/main/assets/doc/CHANGELOG-ko.md)

******

### 빌드

******

이 절은 소스에서 플러그인을 빌드하려는 개발자를 위한 것입니다.

debug APK 빌드:

```powershell
.\gradlew.bat :app:assembleDebug
```

JVM 단위 테스트를 실행하고 instrumentation 테스트 APK 빌드:

```powershell
.\gradlew.bat :app:testDebugUnitTest :app:assembleDebugAndroidTest
```

release APK 빌드 (단일 범용 패키지; 버전 관리에서 제외된 `sign.properties` 에 서명을 설정하면 자동 서명됩니다):

```powershell
.\gradlew.bat :app:assembleRelease
```

하나의 명령으로 서명된 universal APK 를 빌드하고 검증한 뒤 영어 CHANGELOG 에서 `SHA256SUMS.txt` 와 `RELEASE_NOTES.md` 생성:

```powershell
py scripts\release\prepare_release.py
```

다국어 문서 소스와 생성물이 동기화되어 있는지 검증 (CI 에서도 실행됩니다):

```powershell
py .python\generate_markdown.py --check
```

빌드 매개변수는 `version.properties` 에 집중되어 있습니다: 최소 SDK 24 (Android 7.0), 대상 SDK 37, 현재 버전 1.0.3.

******

### 현지화와 문서 생성

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

`strings.xml` 은 현지화된 플러그인 설명을, `plugin_instruction.md` 는 호스트 플러그인 센터에 표시되는 사용 설명을 제공합니다. README, 변경 로그, 사용 설명은 모두 JSON 소스에서 생성됩니다: `.readme/` 와 `.changelog/` 아래의 소스를 수정한 뒤 `py .python/generate_markdown.py` 를 실행해 모든 산출물을 다시 생성하세요. 생성된 산출물은 손으로 편집하지 않습니다; `py .python/generate_markdown.py --check` 로 소스와 산출물의 동기화를 검증할 수 있습니다.

******

### 라이선스

******

프로젝트 코드는 [Mozilla Public License 2.0](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/LICENSE) 라이선스를 따릅니다. 내장 단어 분할 구현은 [jieba-analysis](https://github.com/huaban/jieba-analysis) 프로젝트에서 이식했으며, API 설계는 [pinyin](https://github.com/hotoo/pinyin) 라이브러리에 맞추었습니다.

******

### 관련 링크

******

- AutoJs6 Pinyin 문서: https://docs.autojs6.com/#/pinyin
- AutoJs6 프로젝트: https://github.com/SuperMonster003/AutoJs6
- 자매 플러그인 Pinyin4j: https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin4j
- pinyin 라이브러리 (API 설계 참고): https://github.com/hotoo/pinyin
- jieba-analysis 프로젝트: https://github.com/huaban/jieba-analysis


[16 KB page alignment and build verification](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin/blob/master/docs/16kb.md)
