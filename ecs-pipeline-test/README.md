# ecs-pipeline-test

## Secret Key 등록

Settings -> Secrets -> Actions

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

이걸 해야 Github Action이 안 터진다.

## ECR 레포 생성

ECR 레포 만들고, ECR에서 제공하는 Push 커맨드 확인할 것

## Github Action 파일 세팅


## ECS 세팅

### ECS 클러스터 생성

클러스터에 묶인 ec2에 접속 잘 되는지 체크

### ECS Task Definition 생성

Task Definition만 돌렸을 때, `8080` 접속 잘 되는지 체크

### ECS Service 생성

`docker stop`으로 내렸을 때, 다시 container를 띄워주는지 체크


## CodePipeline 세팅

귀찮아서 생-략
