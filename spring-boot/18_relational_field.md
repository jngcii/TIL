# 관계형 데이터

###### 2020.07.06


## 들어가기 전 (Entity의 상태)
- `Transient` : 객체를 생성하고, 값을 주어도 JPA나 hibernate가 그 객체에 관해 아무것도 모르는 상태. 즉, 데이터베이스와 매핑된 것이 아무것도 없다.
- `Persistent` : 저장을 하고나서, JPA가 아는 상태 (관리하는 상태). 그러나 .save()를 했다고 해서, 이 순간 바로 DB에 이 객체에 대한 정보가 들어가는 것은 아니다. JPA가 persistent 상태로 관리하고 있다가, 후에 데이터를 저장한다. (1차 캐시, Dirty Checking, Write Behind 등의 기능을 제공)
- `Detached` : JPA가 더이상 관리하지 않는 상태. JPA가 제공해주는 기능들을 사용하고 싶다면, 다시 persistent 상태로 돌어가야한다.
- `Removed` : JPA가 관리하는 상태이긴 하지만, 실제 commit이 일어날 때, 삭제가 일어난다.

## `@ManyToOne`
- optional
  - false로 설정하면 해당 객체에 null이 들어갈 수 있다.
  - default는 true
- targetEntity
- cascade
- fetch

## `@OneToMany`
> `@JoinColumn(name = "parent_id")`를 같이 쓰는 것을 권장
- targetEntity
  - 관계맺을 Entity Class 정의
  - `targetEntity = User.class`
- cascade
  - Entity의 상태 변화를 전파시키는 옵션
  - 기본적으로는 아무 것도 전이시키지 않는다.
  - 옵션
    - **ALL** : 모두 적용
    - **PERSIST** : 저장할때 같이 저장한다.
    - MERGE
    - **REMOVE** : 지울때 같이 지운다.
    - REFRESH
    - DETACH
- fetch
  - 관계 Entity의 데이터 읽기 전략
  - 옵션
    - EAGER : 미리 읽어온다.
    - LAZY : 실제로 요청하는 순간 가져온다.
- mappedBy
  - Many쪽의 필드명을 저의
  - User입장에서 Post entity의 user필드
  - `mappedBy = "user"`
- orphanRemoval
  - 관계 Entity에서 변경이 일어난 경우 DB 변경을 같이 할지 결정
  - cascade와 다른 점
    - cascade : JPA 레이어 수준
    - orphanRemoval : DB 레이어 수준
  - default는 false