# Docker Redis

Docker로 redis 인프라 구축

## 셋업

### redis-cli

Redis 서버 설치 없이 redis-cli 실행 [link](https://redis.com/blog/get-redis-cli-without-installing-redis-server/)

```bash
# install using npm
npm install -g redis-cli

# connect redis!
rdcli -h localhost -p xxxx

# check connection!
localhost:xxxx> PING
PONG
```

### redis container

```bash
# run redis container
docker run --name my-redis -d -p xxxx:6379 redis

# connect
rdcli -h localhost -p xxxx
```


