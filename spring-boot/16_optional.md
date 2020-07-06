# Optional

###### 2020.07.06

- null은 Tony Hoare라는 영국의 컴퓨터 과학자에 의해 처음 고안되었다.
- 당시에는 존재하지 않는 값을 표현할 수 있는 가장 편리한 방법이 null참조라고 생각했지만, 나중에 많이 후회했다고 한다.

## I. NPE (NullPointException)

- 자바 개발자들이 가장 골치아프게 겪는 문제
- 코드 베이스 곳곳에 깔려있다.
- 런타임때 터진다... ㅠㅠ
    ```bash
    java.lang.NullPointerException
        at seo.dale.java.practice(OptionalTest.java:26)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:497)
    ```
- null 처리가 취약한 코드에서는 NPE가 발생할 확률이 높다.
- 널처리가 안된 코드 예시

    ```java
    /* 주문 */
    public class Order {
        private Long id;
        private Date date;
        private Member member;
        // getters & setters
    }

    /* 회원 */
    public class Member {
        private Long id;
        private String name;
        private Address address;
        // getters & setters
    }

    /* 주소 */
    public class Address {
        private String street;
        private String city;
        private String zipcode;
        // getters & setters
    }
    ```

    ```java
    /* 주문을 한 회원이 살고 있는 도시를 반환한다 */
    public String getCityOfMemberFromOrder(Order order) {
        return order.getMember().getAddress().getCity();
    }
    ```

- NPE 발생 시나리오
    1. order 파라미터에 null값이 넘어옴
    2. order.getMember()의 결과가 null
    3. order.getMember().getAddress()의 결과가 null
    4. order.getMember().getAddress().getCity()의 결과가 null

## II. Java 8 이전의 null 처리

- 극혐
- 예시 1
    ```java
    public String getCityOfMemberFromOrder(Order order) {
        if (order != null) {
            Member member = order.getMember();
            if (member != null) {
                Address address = member.getAddress();
                if (address != null) {
                    String city = address.getCity();
                    if (city != null) {
                        return city;
                    }
                }
            }
        }
        return "Seoul"; // default
    }
    ```
- 예시 2
    ```java
    public String getCityOfMemberFromOrder(Order order) {
        if (order == null) {
            return "Seoul";
        }
        Member member = order.getMember();
        if (member == null) {
            return "Seoul";
        }
        Address address = member.getAddress();
        if (address == null) {
            return "Seoul";
        }
        String city = address.getCity();
        if (city == null) {
            return "Seoul";
        }
        return city;
    }
    ```

## III. Java 8 이후의 null 처리 (**`Optional`**)
- `java.util.Optional<T>`라는 새로운 클래스 도입
- Optional : 존재할 수도 있지만 안 할 수도 있는 객체 (null이 될 수 있는 객체)
- 원소가 없거나 최대 하나 밖에 없는 Collection이나 Stream

### 사용 효과
- NPE를 유발할 수 있는 null을 직접 다루지 않아도 된다.
- 수고롭게 null 체크를 직접 하지 않아도 된다.
- 명시적으로 해당 변수가 null일 수도 있다는 가능성을 표현할 수 있다.

### 기본 사용법
```java
    Optional<Order> maybeOrder;
    Optional<Member> optMember;
    Optional<Address> address;
```
- 변수명은 그냥 사용하거나, `maybe`, `apt`와 같은 접두어를 붙여 `Optional` 타입의 변수라는 것을 좀 더 명확히 나타내기도 한다.
- `Optional` 클래스는 간편하게 객체를 생성할 수 있도록 3가지 정적 팩토리 메서드를 제공한다.
    - `Optional.empty()` : 비어있는 (null을 담은) Optional 객체 생성
    - `Optional.of(value)` : 객체를 담고 있는 Optional 객체 생성
    - `Optional.ofNullable(value)` : value가 null인지 아닌지 확실하지 않을때 사용
- `Optinal` 클래스가 담고 있는 객체 접근
    > Optional이 담고 있는 객체가 존재하면 동일한 값을 반환, 비어있는 경우에 다르게 작동하는 메서드들
    - `get()` : 비어있을 경우, `NoSuchElementException`
    - `orElse(T other)` : 비어있는 경우, 넘어온 인자를 반환
    - `orElseGet(Supplier<? extends T> other)` : 넘어온 함수형 인자를 통해 생성된 객체 반환

## III. 잘 사용하기

### Stream 처럼 사용하기
- Optional 클래스는 Stream 클래스가 가지고 있는 `map()` 이나, `filter()` 같은 메서드를 가지고 있다.
- 예시
    ```java
    /* 주문을 한 회원이 살고 있는 도시를 반환한다 */
    public String getCityOfMemberFromOrder(Order order) {
        return Optional.ofNullable(order)
                .map(Order::getMember)
                .map(Member::getAddress)
                .map(Address::getCity)
                .orElse("Seoul");
    }
    ```
    - `ofNullable()` : order 객체가 null인지 아닌지 몰라서
    - 3번의 `map()` 메서드 연쇄 호출을 통해서 `Optional` 객체를 3번 변환
      - Optional<Order> -> Optional<Member> -> Optional<Address> -> Optional<String>
    - 마무리작업으로 `orElse()` 메서드를 통해 이 전 과정에서 통해 얻은 Optional이 비어있을 경우, 디폴트로 사용할 도시 이름을 세팅