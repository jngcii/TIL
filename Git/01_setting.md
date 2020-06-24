# Setting

###### 2020.06.24

## I. 최초 설정 (로컬에 계정 등록)
```bash
git config --global user.name "Country"
git config --global user.email "hnaras@naver.com"
```

## II. Alias
```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status 
# git config --global alias.lg "log --graph --oneline"
git config --global alias.lg "log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all"
```
