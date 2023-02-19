# Docker Mysql

Docker로 mysql 인프라 구축

[DockerHub](https://hub.docker.com/_/mysql)

## 셋업

### mysql Container

```bash
# run mysql container
docker run --name my_mysql -p xxxx:3306 -e MYSQL_ROOT_PASSWORD=my_password -d mysql

# access to the container
$ docker exec -it my_mysql /bin/bash
mysql -uroot -p

# (mysql client 설치가 되어 있을 때)
mysql -uroot -p -h localhost --port xxxx
```

### Connect

```bash
mysql -uroot -p -h localhost --port xxxx
```

### docker-compose

`docker-compose up` 하기 전에 `mysql.docer-compose.yaml` 파일을 수정할 것. `xxxx`로 표기된 모든 부분을 수정하자.

```bash
docker compose -f mysql.docker-compose.yaml up -d
```

