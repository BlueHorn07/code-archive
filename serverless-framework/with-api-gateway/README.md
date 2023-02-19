# 람다에 API Gateway를 연결한 배포

`serverless.yml`에서 아래 부분을 추가했다.

```yml
...
functions:
  hello:
    haldner: haldner.hello
    events:
      - http:
          path: hello
          method: get
...
```

만들어진 AWS 람다의 trigger에 API Gateway가 연결된다.

배포가 완료되면 람다를 트리거 할 수 있는 API Gateway URL도 반환해준다.

```bash
Deploying my-py-serverless to stage dev (ap-northeast-2)

✔ Service deployed to stack my-py-serverless-dev (49s)

endpoint: GET - https://xxxx.execute-api.ap-northeast-2.amazonaws.com/dev/hello
functions:
  hello: my-py-serverless-dev-hello (856 B)
```
