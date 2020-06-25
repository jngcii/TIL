# cherry-pick

###### 2020.06.25

- 다른 브랜치의 커밋을 가져오는 방법
- 커밋의 수가 적다면 merge나 rebase보다 깔끔한 트리를 유지할 수 있다.
  ```bash
  git co master
  git co -b feature
  vi README.md
  git ci -am 'Cherry-pick test'

  git co master
  git cherry-pick {{hash}}
  ```
- master브랜치에서 feature브랜치의 commit을 가져오는데 commit메세지는 같지만 hash 값은 다른 엄연히 다른 commit이 생성된다.
- 같은 커밋을 가져왔기때문에 feature 브랜치는 지운다.
  - `$ git br -D feature`