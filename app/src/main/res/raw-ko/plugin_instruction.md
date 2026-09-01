Pinyin 플러그인 (Pinyin Plugin) 은 AutoJs6 에 오프라인 중국어 병음 변환 기능을 제공합니다. 설치 후 스크립트는 전역 객체 `pinyin` 을 통해 중국어 텍스트를 다양한 스타일의 병음으로 변환할 수 있으며, 다음자 후보, 어구 사전, Jieba 단어 분할, 성씨 모드를 지원하여 정렬, 검색, 첫 글자 색인, 발음 표기 등 자동화 시나리오에 적합합니다.

### 빠른 시작

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

### 병음 스타일

`style` 옵션은 병음 출력 스타일을 제어합니다. "中" (zhōng) 을 예로 듭니다:

```text
TONE (zhōng)  TONE2 (zhong1)  TO3NE (zho1ng)
NORMAL (zhong)  INITIALS (zh)  FIRST_LETTER (z)
```

지원하는 옵션으로는 `style` (병음 스타일), `mode` (일반/성씨/지명 모드), `segment` (단어 분할), `heteronym` (다음자), `group` (어구 병합) 이 있습니다.

### 자가 점검

플러그인을 설치하고 활성화한 뒤 다음 한 줄 스크립트를 실행하세요:

```javascript
console.log(pinyin.simple("拼音"));
```

`pinyin` 이 출력되면 플러그인이 정상 동작하는 것입니다.

더 자세한 사용법과 옵션 설명은 [AutoJs6 Pinyin 문서](https://docs.autojs6.com/#/pinyin) 와 [프로젝트 홈페이지](https://github.com/SuperMonster003/AutoJs6-Plugin-Pinyin) 를 참고하세요.
