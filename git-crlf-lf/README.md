

```bash
# Git Workspace의 로컬 설정을 바꾸는 것 (global 설정 아님)
git config core.autocrlf false

# 다 날렸다가 복구
git rm --cached -r .
git reset --hard

# 남은 파일 중에 CRLF 있는지 확인
git ls-files --eol | grep crlf
```
