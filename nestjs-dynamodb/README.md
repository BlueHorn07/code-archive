# NestJS-DynomDB

Practice AWS DynamoDB with NestJS.

## DynamoDB Guide

[@aws-sdk/client-dynamodb](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-dynamodb/index.html)

- NoSQL
  - `JOIN`과 같은 관계형 연산이 없음. 
  - `SELECT ... FROM ...` 형태의 SQL 쓸 수 없음.
- 테이블의 속성이 동적임.
- 로깅 데이터를 저장하는데 좋음.
- 파티션키와 정렬키를 잘 지정하는게 중요.
  - ex) 파티션키 = `player_id`, 정렬키 = `last_login_ts`

아래와 같은 패턴으로 코드를 작성.

```js
const command = new DynamodbComamnd({
    TableName: 'your-dynamodb-table',
    Key: {
        'PK_name': { 'PK_Type': 'PK_value'},
        'key_name': { 'type': 'value'},
    }
})

this.dynmodb.send(command);
```

### Query & Scan

- Query
  - 파티션키(PK)와 정렬키(SK)로 데이터를 읽어오는 방식
  - Scan과 비교해 속도가 빠름
  - `GetItemCommand()` 사용
- Scan
  - 파티션키, 정렬키 이외의 키로 데이터를 읽어오는 방식
  - 전체 데이터 모두 읽어올 수 있음
  - Query와 비교해 속도가 느림
  - `ScanCommand()` 사용


### Response

Mysql과 RDS와 다르게 `$metadata`가 있고, `Item`에 쿼리 값이 담겨서 옴.

```json
{
    "$metadata": {
        "httpStatusCode": 200,
        "requestId": "ABCD...",
        "attempts": 1,
        "totalRetryDelay": 0
    },
    "Item": {
        "book_id": {
            "S": "1234"
        },
        "author": {
            "S": "cantor"
        }
    }
}
```

## 후기

- 흠... RDS와 ORM에 익숙해서 그런지 NoSQL인 DynamoDB를 DB 엔진으로 쓰는게 익숙하지 않구먼
- 언제 DynamoDB를 쓰는게 좋을지 사례를 보고 경험을 쌓아야 할 듯
- ORM이 없어서 직접 `Repository.ts`를 구현하는 걸까? 
  - `Service.ts`에 dynamodb client를 넣어도 되지 않을까?라고 고민했는데...
  - dynamodb를 쓰다가 RDS로 바꾸는 상황에서 쉽게 교체하는 상황을 감안해서 `Repository.ts`로 분리하는 거겠지?
