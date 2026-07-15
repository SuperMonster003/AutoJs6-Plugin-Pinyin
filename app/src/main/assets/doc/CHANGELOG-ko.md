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
