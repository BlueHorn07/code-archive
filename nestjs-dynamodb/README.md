# NestJS-DynamoDB

Practice AWS DynamoDB with NestJS.

## DynamoDB Guide

- NoSQL
  - `JOIN`과 같은 관계형 연산이 없음.
  - `SELECT ... FROM ...` 형태의 SQL 쓸 수 없음.
- 테이블의 속성이 동적임.
- 로깅 데이터를 저장하는데 좋음.
- 파티션키와 정렬키(SK)를 잘 지정하는게 중요.
  - ex) 파티션키 = `player_id`, 정렬키 = `last_login_ts`
  - SK는 `date`, `datetime`과 같이 RANGE 형태의 자료로 설정하는 것이 좋음.
    - SK는 Query에서 `BETWEEN`, `>, >=, <=, <`와 같이 비교 연산을 할 수 있기 때문!

### Query & Scan

- Query
  - 파티션키(PK)와 정렬키(SK)로 데이터를 읽어오는 방식
  - Scan과 비교해 속도가 빠름
  - `GetItemCommand()` 사용
- Scan
  - 파티션키, 정렬키 이외의 키로 데이터를 읽어오는 방식
  - `ScanFilter`가 아무리 추가되어도 무조건 Full scan을 함
    - 데이터가 많으면 Full Scan 비용이 어마어마 하다. 정말정말 특별한 목적이 있지 않다면, 웬만해선 **절대** 쓰지 않아야 한다.
  - Query와 비교해 속도가 느림
  - `ScanCommand()` 사용

## AWS SDK: Dynamodb

- [npm: `@aws-sdk/client-dynamodb`](https://www.npmjs.com/package/@aws-sdk/client-dynamodb)
- [npm: `@aws-sdk/lib-dynamodb`](https://www.npmjs.com/package/@aws-sdk/lib-dynamodb)
- [`@aws-sdk/client-dynamodb`](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-dynamodb/index.html)

`@aws-sdk/client-dynamodb`와 `@aws-sdk/lib-dynamodb`를 함께 쓴다. 
`@aws-sdk/client-dynamodb`는 Dynamodb Client 인스턴스를 만드는데 사용하고, 
`@aws-sdk/lib-dynamodb`는 Dynamodb Client 인스턴스에 JS에 맞게 추상화된 연산을 돕는다.
`@aws-sdk/client-dynamodb` 단독으로 쓸 수도 있지만, `@aws-sdk/lib-dynamodb`를 함께 쓰는 것을 권장한다.


### Response

`$metadata`에 Command에 대한 메타 정보가 있고, `Item`에 쿼리 값이 담겨서 옴. 

```json
{
  "$metadata": {
    "httpStatusCode": 200,
    "requestId": "ABCDEFGHIJK",
    "attempts": 1,
    "totalRetryDelay": 0
  },
  "Count": 3,
  "Items": [...],
  "ScannedCount": 3
}
```

`ScanCommand()`와 같이 반환되는 값이 여러개면 `Items`에 담겨서 옴.

`@aws-sdk/client-dynamodb`와 `@aws-sdk/lib-dynamodb`의 Response 형식이 다름.

```json
// `@aws-sdk/client-dynamodb`
{
    "content": {
        "S": "I bless rains down in Africa"
    },
    "bookbook_name": {
        "S": "Africa"
    },
    "book_id": {
        "S": "toto"
    },
    "author": {
        "S": "TOTO"
    }
}
```

```json
// `@aws-sdk/lib-dynamodb`
{
    "content": "I bless rains down in Africa",
    "bookbook_name": "Africa",
    "book_id": "toto",
    "author": "TOTO"
}
```

## 후기

- 흠... RDS와 ORM에 익숙해서 그런지 NoSQL인 DynamoDB를 DB 엔진으로 쓰는게 익숙하지 않구먼
- 언제 DynamoDB를 쓰는게 좋을지 사례를 보고 경험을 쌓아야 할 듯
- ORM이 없어서 직접 `Repository.ts`를 구현하는 걸까? 
  - `Service.ts`에 dynamodb client를 넣어도 되지 않을까?라고 고민했는데...
  - dynamodb를 쓰다가 RDS로 바꾸는 상황에서 쉽게 교체할 걸 감안해서 `Repository.ts`로 분리하는 거겠지?
