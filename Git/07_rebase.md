# Rebase

###### 2020.06.25

## I. 다른 브랜치와 병합
- 기능적으로는 merge와 비슷하다.
- 다만 내 브랜치의 커밋을 대상 브랜치의 위(다음)으로 생성해서 깔끔한 로그를 유지할 수 있다.

### Fast-Forward
>`(test)$ git rebase master`
- master브랜치와 test브랜치가 있다고 가정
- master브랜치가 test브랜치보다 커밋이 앞서 있고 test브랜치 이후의 커밋을 가리키고 있다.
- test브랜치의 상태를 최신으로 유지하고 싶다면 test 브랜치의 HEAD를 master 브랜치의 HEAD 커밋으로 이동시키면 된다.
- 이때 사용하는 것이 fast-forward 방식의 rebase

### Auto-Merging
- 두 브랜치 모두 작업을 한 상태에서 rebase하지만 충돌이 나지 않는 상태
- merge같은 경우에는 3-way Merge가 실행되어 브랜치가 나뉘었다가 제일 위에 새로운 커밋을 만들고 그 커밋을 가리키게 된다.
- rebase는 단순히 가장 위로 커밋을 올린다.

### Conflict
- 두 브랜치 모두 커밋이 있고 충돌이 나는 상태
- 해결 방법
  - `git add/rm <conflict_files>` -> `git rebase --continue`
  - `git rebase --skip` : 합치려는 대상 브랜치의 내용이 맞다. 그 내용으로 적용
  - `git rebase --abort` : rebase 안한 상태로 가기


## II. 커밋 여러개 수정하기
- rebase란 커밋을 수정하는 작업
- 주의 : `push`해서 누군가가 사용하고 있는 커밋을 `rebase`하면 안된다.
  - rebase는 기존 커밋을 그대로 사용하지 않고 내용은 같지만 다른 커밋을 만들어 낸다.
  - 새 커밋을 원격저장소에 `push`하고 동료중 누군가가 그 데이터를 `pull`해서 사용한다고 가정했을 때, `push`한 커밋을 `rebase`해서 `push`하면 동료는 `push`하면 에러가 난다. (원격과 로컬의 히스토리가 다르기 때문이다.)
  - 다른 사람은 그 커밋 히스토리를 기반으로 다른 커밋을 쌓으면서 작업을 하고 있을텐데, 커밋을 수정하면 그 기반을 바꿔버리는 것이기 때문이다.
    ![](assets/Screen%20Shot%202020-06-25%20at%2011.14.23%20AM.png)
- `-i` : 대화형 모드
  ![](assets/Screen%20Shot%202020-06-25%20at%2011.33.01%20AM.png)
- 여러개의 커밋이 의미가 없다고 생각해 합치고 싶을 때 : `git rebase -i @~3`
  - @는 HEAD랑 같다.
  - 세개의 커밋을 합치겠다.
  - rebase vim 에디터 나온다.
  - 여기서 옵션
    - `p`, pick = use commit
    - `r`, reword = use commit, but edit the commit message
    - `e`, edit = use commit, but stop for amending
    - `s`, squash = use commit, but meld into previous commit
    - `f`, fixup = like "squash", but discard this commit's log message
    - `x`, exec = run command (the rest of the line) using shell

