# JpaRepository

###### 2020.07.06

- JpaRepository는 메서드 이름 작성 방법만 알면, 필요한 메서드를 빠르게 쓰고 추가할 수 있다.


## 기본 제공
> save
- 레코드 저장 (insert, update)
> findOne
- primary key로 레커드 한건 찾기
> findAll
- 전체 레코드 가져오기 (sort, pagination 가능)
> count
- 레코드 갯수
> delete
- 레코드 삭제

## 규칙에 맞는 메서드 작성 ()
> findByXX
- 기본으로, `findBy` 이후에 인티티의 속성 이름을 붙인다. (대문자로 시작하게)
- 그 다음에는 이 뒤로 계속 이어쓰면 된다.
> Like / NotLike
- Like를 붙이면, 인수에 지정된 텍스트를 포함하는 엔티티를 검색한다.
- NotLike를 붙이면, 포함하지 않는 엔티티를 검색한다.
- `findByNameLike("abc")` : 이름에 "abc"가 포함된 엔테티 검색
> StartingWith / EndingWith
- 위와 비슷
> IsNull / IsNotNull
- 인자는 없고, null이거나 null이 아닌 것을 검색한다.
> True / False
- 인자는 없고, True이거나 False인 것을 검색한다.
> Before / After
- 시간 값으로 사용한다.
- `findByCreateBefore(new Date())`라고 검색하면, create라는 항목의 값이 현재보다 이전의 것만을 찾는다.
> LessThan / GreaterThan
- 숫자 값으로 사용한다. 그 항목의 값이 인자보다 작거나 큰 것을 검색한다.
> Between
- 인자를 두개 받는다. 두 인자 사이의 값을 검색한다.
> OrderBy
- 검색 결과를 정렬하여 전달
- `findByEmailOrderByNameAsc(String email)`와 같이 사용