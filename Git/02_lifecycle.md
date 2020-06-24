# Git Lifecycle

###### 2020.06.24

## I. Git의 네가지 상태
![lifecyle](./assets/lifecycle.png)
> [2.2 Git의 기초 - 수정하고 저장소에 저장하기](https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%88%98%EC%A0%95%ED%95%98%EA%B3%A0-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%97%90-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0)
- Untracked
  - Git과 아무 상관이 없는 상태
  - Git이 관리하고 있는 폴더에 파일이 존재하더라도 Untracked 상태일 경우 관리하지 못한다.
  - 최초 `add`를 해줘야 Git의 관리 대상이 된다.
  - Git이 관리하는 파일을 삭제하면 Untracked가 된다.
- Staged
  - 이제 코드를 저장해도 좋다는(`commit`이 가능한) 상태
  - Untracked/Modified 상태인 파일을 `add` 하면 Staged가 된다.
- Unmodified
  - 코드 저장이 완료된 상태
  - Staged 상태에서 `commit`을 하면 Unmodified가 된다.
- Modified
  - Git으로 관리되고 있던 코드를 수정하여 변경이 일어난 상태
  - Unmofieid 상태인 파일을 수정하면 Modified가 된다.
  - `commit` 할 수 없음. `commit` 하려면 Staged 상태가 되야한다.

## II. Git 명령어

- status
  - 현재 Git의 상태를 보여준다.
  - Unmodified 상태의 파일은 보이지 않는다.

-log
  - history를 조회하는 명령어
  - log를 볼 줄 알아야 develop, release, hotfix 브랜치가 난무할 때 merge 방향이나 순서를 이해할 수 있다.

- add
  - 파일을 Git이 관리하는 상태로 만든다.
  - Untracked 혹은 Modified 상태의 파일을 Staged 상태로 만드는 명령어

- commit
  - 파일을 Unmodified 상태로 만드는 명렁어
  - Git 시스템에 영구적으로 상태를 저장
  - SHA-1 알고리즘을 적용한 해시 값을 키로 생성
  - 히스토리가 하나 추가된다.
  - 실무에서는 한 작업 (기능, 피처) 단위로 한 커밋 권장
  - 옵션
    - `-m` : 커밋 메세지를 넣는 명령어
    - `-a` : add를 같이 한다. 단순히 Modified
    - `-am` : `-a`와 `-m`을 합친 것
    - `--amend`
      - 마지막 커밋을 수정
      - `Staged` 상태의 파일들과 같이 커밋된다.
      - 만약 `Staged` 상태의 파일이 없다면 마지막 커밋의 메세지만 수정된다.
      - 메세지를 같이 입력하고 싶으면 `-m`을 함께 입력하며 된다.

- branch
  - commit 사이를 가볍게 이동할 수 있는 어떤 포인트 같은 것
  - 하나의 작업 공간
  - `git br` : 브랜치 확인
  - `git br test/1` : 브랜치 생성
  - `get br -D test/1` : 브랜치 삭제

- checkout
  - 다른 브랜치로 이동
  - 옵션
    - `-b` : 브랜치를 생성하고 그 브랜치로 checkout

- push
  - 로컬 브랜치의 정보를 원격 저장소로 업로드
  - Clone한 리모트 저장소에 쓰기 권한이 있어야 한다.
  - 같은 브랜치로 여러명이 받아서 누군가 push를 했다면 나는 push할수 없다.
    - 왜냐하면 누군가가 push한 상태의 저장소 입장에서 나의 로컬은 최신이 아니기 때문이다.
    - 다른 사람이 작업한 것을 합친 후에 (merge or rebase) push 할 수 있다.
  - 옵션
    - `-f(--force)`
      - 내 로컬 브랜치로 원격 브랜치를 덮어 씌워버림
      - 내가 혼자 작업하던 feature 브랜치에서만 사용해야 한다.
      - 누군가가 push한 상태에서 이 명령어를 사용하면 다른사람의 작업은 날아가버린다..

- pull
  - 원격 저장소에서 데이터를 가져오고, 그 데이터를 자동으로 현재 작업하는 코드와 merge

- fetch
  - 원격 저장소에서 데이터를 가져오고, 자동으로 코드르 합치지는 않는다.
  - fetch를 받아온 상태에서 log를 확인하면, HEAD는 나의 마지막 commit으로 나타나 있고 그 위에 fetch 받아온 커밋들이 있다.
  - 이 상황에서 rebase or merge or pull을 실행하면 적용된다.

- push&pull (adv.)
  - 추가 명령어
    - 파일 변경 내용 보기 : `git diff`
    - 리모트의 브랜치 삭제 : `git push origin --delete [브랜치명]`
    - 삭제된 리모트 브랜치를 로컬에도 반영 : `git fetch -p`
  1. 2개의 로컬 저장소 만들기 (A, B)
  2. A에서 test branch 만들기 - `git co -b test`
  3. A에서 push - `git push`
      - 원격저장소에 test라는 브랜치가 없다는 에러가 발생
      - 원격에 test 브랜치가 있을 경우 현재 브랜치에서 그냥 `git push`만 입력하면 현재 브랜치로 push한다.
  4. A에서 - `git push origin test`
  5. B에서 원격 저장소 받아오기 - `git fetch`
  6. B에서 로그 확인 - `git lg`
      - HEAD는 그대로 있고 원격의 test 브랜치 커밋만 받아온 상태
  7. B에서 적용까지 하려면 pull - `git pull`
      - HEAD는 test 브랜치 커밋을 가리킨다.
  8. 이번엔 A에서 파일을 수정하고 B에서 같은 부분을 수정한다.
  9. A에서 commit & push - `git push`
  10. B에서 commit & pull - `git pull`
  11. B에서 status 확인 - `git st`
      - 너의 로컬 브랜치와 origin/test 브랜치는 갈라졌다.
      - 실제로 `git lg`를 입력해보면 브랜치가 갈라진 것을 확인 할 수 있다.
  12. 이 상태에서 B에서 머지하기 싫다면 abort - `git merge --abort`
      - 이 명령어는 `git pull` 명령어를 안한 상태로 만들어버림
  13. 혹은 B에서 해당 충돌을 Resolve한 후 커밋하면 된다.