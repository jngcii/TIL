# Git Flow

###### 2020.06.24

> 회사에서 Git을 쓸 때, 어떤식으로 브랜치들을 관리하고 어떤식으로 합쳐서 개발할지 정해놓은 것

![](assets/gitflow.png)

- master
  - git init하면 생기는 태초의 브랜치
  - 배포 가능한, 말그대로 master 브랜치
  - 보통 태그를 따서 태그로 배포한다.
    - 태그는 버전을 의미한다.
  - 어느 태그로 가더라도 문제가 없이 항상 배포 가능한 형태여야만 한다.
- develop
  - 보통 작업할 때 기준이 되는 브랜치
  - 개발 서버에도 평소에는 develop 기준으로 배포하며 테스트 한다.
  - 생성 위치: `master` (태초)
- hotfix
  - 서비스에 문제가 생기거나 갑자기 급하게 무언가 고쳐서 배포해야 할 때 사용
  - 생성 위치: `master` (그렇지 않으면 다른 작업들이 딸려 나감)
  - `master` & `develop` 모두로 merge한다.
- feature
  - 실제로 뭔가 기능(feature)를 만드는 브랜치
  - 생성 위치: `develop`
  - merge: `develop` (code reivew)
- release
  - 새로운 기능들을 추가하여 배포하기 위한 브랜치
  - 생성 위치: `develop`
  - merge: `master` & `develop`


### HEAD
- 지금 작업하는 로컬 브랜치를 가리키는 포인터
- 브랜치를 변경하면 해당 브랜치의 마지막 커밋을 가리키고 있다.
- HEAD를 움직이면서 여러 버전의 코드르 볼 수 있다.