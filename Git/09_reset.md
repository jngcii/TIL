# Reset

###### 2020.06.25

- 상태를 이전으로 돌리는 명령어
- 옵션에 따라서 몇 단계 이전 / 어느 단계 (`Staged`, `Modified`, `Unmodifed`)까지 되돌릴지 결정
- `show` : 커밋 정보를 보여줌
  - `HEAD`(=`@`), `~`(=`^`)
  - ex) 한 커밋 이전 `HEAD~`, `HEAD^`, `@~`, `@^`
  - ex) 두 커밋 이전 `@~2`
- 옵션
  - `--soft`
    - commit 명령만 되돌린다. (`Staged` 상태가 된다)
    - `HEAD`만 해당 상태로 되될린다.
      ```bash
      vi README.md
      git ci -am 'Commit for reset exer'
      git reset --soft @^
      git st

      ---

      On branch develop
      Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

      modified:   README.md
      ```
  - `--mixed` (default)
    - `commit` 명령도 되돌리고, `add` 명령까지 되돌린다. (`Modified` 상태가 된다)
    - ```bash
      git ci -am 'Commit for reset exer'
      git reset --mixed @~1
      git st

      ---

      On branch develop
      Changes not staged for commit:
        (use "git add <file>..." to update what will be committed)
        (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   README.md      
      ```
  - `--hard`
    - `commit` 명령도 되돌리고, `add` 명령도 되돌리고, 워킹 디렉토리까지 되돌림 (`Unmodified` 상태가 됨)
    - 워킹 디렉토리까지 되돌려 버리기 때문에 복구가 불가능!
    - ```bash
      git ci -am 'Commit for reset exer'
      git reset --hard @^
      git st

      ---

      On branch develop
      nothing to commit, working tree clean