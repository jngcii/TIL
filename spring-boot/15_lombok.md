# Lombok

###### 2020.07.06

- 자바 컴파일 시점에서 특정 어노테이션으로 해당 코드를 추가할 수 있는 라이브러리

## `@Data` annotation
- `@ToString`, `@EqualsAndHashCode`, `@Getter`, `@Setter`, `@RequiredArgsConstructor`를 한번에 사용하는 어노테이션
- 부작용이 많다.
- 자동으로 Setter를 지원하게 되는데, Setter는 객체르 언제든 변경할 수 있는 강태가 되어서 안전성이 낮다. **변경 기능이 제공되지 않는 필드는 setter를 제공하지 않아야 한다.**
- `@OneToMany`와 `@ManyToOne`의 양방향 관계에서 `@ToString`을 그냥 사용할 경우 무한 순환 참조의 문제가 발생할 수 있다.
  - `@ToString(exclude = "순환참조테이블이름")`으로 순환 탈피 가능


## `@NoArgsConstructor` annotation
- JPA에서는 프록시 생성을 위해 기본 생성자가 반드시 하나 필요한데, 이 때 접근을 protected로 해야한다. (외부에서 접근할 수 없게)
  > protected : 같는 패키지 혹은 자식 클래스에서만 접근 가능
- 이 생성자를 public으로 설정하면, 호출되었을 때, 모든 필드가 null로 세팅되는데, 그것을 막기 위해서는 접근을 제한해야한다.
- 아무 이유없이 기본 생성자를 열어두는 것은 안전하지 않다.
- **객체에 대한 생성자를 하나로 두고, 그것을 `@Builder`를 통해 사용하는것이 효율적이다.**

## `@Builder`
  ```java
    @Builder
    public Account(Long id, String username, String password) {
        Assert.notNull(username, "username must not be null.");
        Assert.notNull(password, "password must not be null.");

        this.id = id;
        this.username = username;
        this.password = password;
    }
  ```
  ```java
    public Account toEntity() {
        return Account.builder()
                .username(username)
                .password(password)
                .build();
    }
  ```
- `Builder`가 사용된 객체를 리턴한다.
- 클래스 위에 `@Builder`를 사용하면 `@AllArgsConstructor` annotation을 사용한 효과를 발생시켜, 모든 멤버 필드에 대해서 매개변수를 받는 생성자를 만든다.