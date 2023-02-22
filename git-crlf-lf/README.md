# Git LF Normalization (특히 Windows)

Windows에서 Pretter의 not `LF` 오류를 해결하기 위한 방법이다.

## git config 변경

```bash
git config core.autocrlf input
git config core.eol lf

git config --global core.autocrlf input
git config --global core.eol lf
```

요것 설정 후에는 git clone으로 받는 파일이 모두 EOL `LF`로 받는다.

그러나 Git 상에 `CRLF`로 인코딩 되어 커밋 된 파일은 여전히 `CRLF`로 남아서 오류를 뱉는다.

(뇌피셜) 딱히 설정을 바꾸지 않았다면, Github에 올라간 파일들은 알아서 EOL `LF`로 올라간다. 그런데, 뭔가를 잘못 건드려서 Github에 `CRLF`로 올라간 경우도 있다... 이 경우는 위의 `git config --global`을 해도 파일의 EOL가 `CRLF`다!

## 로컬에 `CRLF`로 된 파일들 변환

git config 설정 바꾸기 전에 받은 파일들은 여전히 EOL `CRLF`다. 

사실 다른 브랜치로 checkout 하면, 바뀐 git config 대로 `LF`로 변환 된다.

checkout 없이 수동으로 하길 원한다면, 아래 명령어를 통해 `LF`로 바꿔주자.

```bash
# CRLF가 있는지 확인
git ls-files --eol | grep crlf

# 다 날렸다가 복구
git rm --cached -r .
git reset --hard

# working dir에 CRLF가 있는지 확인
git ls-files --eol | grep w/crlf
```

`git ls-files --eol | grep w/crlf`에서 **아무 것도 출력되지 않아야 성공!**

`w/crlf` 상태인 파일이 남아있다면, Windows에서 Prettier가 에러를 뱉을 것이다.

## Git에 `CRLF`에 올라간 파일들 변환

실수로 Git에 EOL `CRLF`로 올린 경우를 처리하는 방법이다.

```bash
# git에 CRLF로 올라간 파일이 있는지 확인
git ls-files --eol | grep i/crlf

git add --renormalize .
git commit -m "LF Normalization"

# 남은 파일 중에 CRLF가 있는지 확인
git ls-files --eol | grep crlf
```

## git ls-files --eol

`i/xxx`는 git에 올라간 파일의 EOL, `w/xxx`는 working directory의 EOL

```bash
$ git ls-files --eol
i/crlf  w/crlf  attr/       .gitattribute
i/lf    w/lf    attr/       .github/workflows/github-action.yaml
i/lf    w/lf    attr/       .gitignore
```


- [Github Doc](https://docs.github.com/ko/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)
- [[git] gitattribute에 대한 설명서](https://git-scm.com/docs/gitattributes)
