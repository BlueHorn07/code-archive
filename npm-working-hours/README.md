# React Working Hours

Working Hours를 표시하는 npm 패키지 검증. (2022.10.30 수행)

- [`opnening_hours`](https://www.npmjs.com/package/opening_hours)
  - [evaluation tool](https://openingh.ypid.de/evaluation_tool/#check)
- [`@phoenix344/opening-hours`](https://github.com/phoenix344/opening-hours) 👍
  - Best Solution!
- ~~[`react-hours`](https://www.npmjs.com/package/react-hours)~~
  - `@fullcalendar` 관련 의존성 해결 안 됨 

결론: `@phoenix344/opening-hours`를 쓰자!

## `opening_hours`

```node
const oh_value = "We 12:00-14:00"
const oh = new opening_hours(oh_value);
```

### 현재 시간을 기준으로 열었는지 체크

```node
const state = oh.getState(); // we use current date
// true -> open
// false -> close
```

### 시작(`from`)과 끝(`to`) 날짜 기준으로 가능한 시간 목록 얻기

```node
const from = new Date("01 Jan 2012");
const to = new Date("01 Feb 2012");

const intervals = oh.getOpenIntervals(from, to);
```

응답

```json
[
  [
    "2012-01-04T03:00:00.000Z",
    "2012-01-04T05:00:00.000Z",
    false,
    null
  ],
  ...
]
```

### Stringify

```js
oh.prettifyValue()
```

```text
Mo 08:00-12:30,13:00-16:00 Tu 08:00-12:30,13:00-16:00 We 08:00-14:00 Th 08:00-12:30,13:00-16:00 Fr 08:00-12:30,13:00-16:00 Sa 10:00-14:00
```

### 의견

Working Hours 형식을 잘 파싱하고, 심플하지만, 편의 기능이 너무 부족한 것 같다.

Working Hours를 추가하는 것 등등 `@phoenix344/opening-hours`와 비교하면 너무 많은 기능이 부족하다.

## `@phoenix344/opening-hours`

바닐라 버전보다 훨씬 편의성이 좋음.

`oh.toString()` 응답

```text
mon 08:00 - 12:30, 13:00 - 16:00
tue 08:00 - 12:30, 13:00 - 16:00
wed 08:00 - 14:00
thu 08:00 - 12:30, 13:00 - 16:00
fri 08:00 - 12:30, 13:00 - 16:00
sat 10:00 - 14:00
```

위와 같이 그냥 바로 랜더링 되어서 나옴.

`opening_hours.prettifyValue()` 함수가 있지만 흠... 왜인지 configuration이 잘 안 되고 커스텀이 말을 안 들음.

