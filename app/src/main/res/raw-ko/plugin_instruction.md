중국어 텍스트를 병음으로 변환합니다:

```js
let result = pinyin.convert("重庆", { style: "TONE2", heteronym: true });
console.log(result);
console.log(result.compact());
```

`pinyin.simple(text)` 로 성조 없는 간단한 문자열을 얻을 수 있습니다:

```js
console.log(pinyin.simple("重庆"));
console.log(pinyin.simple("重庆", true, true));
```

지원 옵션은 `style`, `mode`, `segment`, `heteronym`, `group` 입니다. 일반적인 스타일 이름은 `NORMAL`, `TONE`, `TONE2`, `TO3NE`, `INITIALS`, `FIRST_LETTER` 입니다.

더 많은 사용 예는 AutoJs6 문서의 [Pinyin](https://docs.autojs6.com/#/pinyin) 섹션을 참고하세요.
