# Spring Data JPA

###### 2020.07.04

- jpa를 사용하기 위한 의존성 추가
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    ```
- Spring Data JPA를 사용하는 것은 결국 JDBC를 사용하는 것이다.
  - SDJ -> JPA -> Hibernamte -> DataSource
- 원래는 `@EnableJpaRepositories`를 사용해서 설정해야 본격적으로 Spring Data JPA 를 사용할 준비가 되는것인데, 이것을 스프링부트가 알아서 설정해준다.

## 사용해보기

- `com.ex/users/User.java`
    ```java
    package com.example.sprintbootjpa.users;

    import javax.persistence.Entity;
    import javax.persistence.GeneratedValue;
    import javax.persistence.Id;
    import java.util.Objects;

    @Entity
    public class User {

        @Id @GeneratedValue
        private Long id;

        private String username;
        private String password;

        public Long getId() {
            return id;
        }

        public void setId(Long id) {
            this.id = id;
        }

        public String getUsername() {
            return username;
        }

        public void setUsername(String username) {
            this.username = username;
        }

        public String getPassword() {
            return password;
        }

        public void setPassword(String password) {
            this.password = password;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            User user = (User) o;
            return Objects.equals(id, user.id) &&
                    Objects.equals(username, user.username) &&
                    Objects.equals(password, user.password);
        }

        @Override
        public int hashCode() {
            return Objects.hash(id, username, password);
        }
    }
    ```
- `UserRepository.java`
    ```java
    package com.example.sprintbootjpa.users;

    import org.springframework.data.jpa.repository.JpaRepository;

    public interface UserRepository extends JpaRepository<User, Long> {

        // 이렇게 메서드만 만들어줘도 이것에 대한 구현체를 만들어서 빈으로 등록해주는 것까지 SDJ가 알아서 해준다.
        User findByUsername(String username);
    }
    ```
- `UserRepositoryTest.java`
    ```java
    package com.example.sprintbootjpa.users;

    import org.junit.Test;
    import org.junit.runner.RunWith;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
    import org.springframework.jdbc.core.JdbcTemplate;
    import org.springframework.test.context.junit4.SpringRunner;

    import javax.sql.DataSource;

    import java.sql.Connection;
    import java.sql.DatabaseMetaData;
    import java.sql.SQLException;

    import static org.assertj.core.api.Assertions.assertThat;


    // slicing test : repository를 포함해서 repostory와 관련된 Bean들만 등록해서 테스트를 만드는 것
    //      slicing test를 할 때는 inmemory db가 반드시 필요하다.
    // 만약 @SpringBootTest를 사용하면, 이 테스트는 인티그레이션 테스트로 애플리케이션에 있는 모든 빈이 다 등록된다.
    //      즉, 데이터베이스도 psql을 사용하게 된다. (권장 X)
    @RunWith(SpringRunner.class)
    @DataJpaTest
    public class UserRepositoryTest {

        @Autowired
        DataSource dataSource;

        @Autowired
        JdbcTemplate jdbcTemplate;

        @Autowired
        UserRepository userRepository;

        @Test
        public void di() {
            User user = new User();
            user.setUsername("jngcii");
            user.setPassword("7777");

            User newUser = userRepository.save(user);
            assertThat(newUser).isNotNull();

            User existingUser = userRepository.findByUsername(newUser.getUsername());
            assertThat(existingUser).isNotNull();

            User nonExistingUser = userRepository.findByUsername("bbbbb");
            assertThat(nonExistingUser).isNull();
        }

    }
    ```