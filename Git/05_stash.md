# Stash

###### 2020.06.24

- 작업하던 내용을 임시 저장
- 브랜치에서 작업하다가 다른 브랜치로 변경해야 하는데 커밋을 하고싶지 않은 경우
- stack처럼 작동
- 옵션
  - `git stash list` : 내가 stash 한게 어디있는지 확인하는 명령어
  - `git stash pop` : 마지막에 stash한 변경을 가져온다.
  - `git stash apply` : stack에 쌓여있는 것 중 골라서 pop 하는 명령어
  - `git stash drop` : stack에 저장된 모든 것을 날리는 명령어