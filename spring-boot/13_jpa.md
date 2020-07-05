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

## I. 사용해보기

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

## II. 데이터베이스 초기화
- `application.properties`
    ```properties
    spring.jpa.hibernate.ddl-auto=update
    # option을 update, create, create-drop 셋 중 하나로 하면 자동으로 스키마가 생성이 된다.
    # create-drop : 애플리케이션 시작할 때 스키마를 생성하고 끝날 때 아예 지운다.
    # create : 애플리케이션 시작할 때, 스키마가 존재하면 아예 지우고 새로 만든다.
    # update : 기존 데이터를 유지하면서 추가된 것만 변경한다.

    spring.jpa.generate-ddl=true
    # 이게 기본으로 false인데 true로 변경해야 스키마가 자동으로 생성된다.

    spring.jpa.show-sql=true
    # 스키마가 생기는 것을 로그로 볼 수 있다.


    ### 운영 상황에서는 아래 옵션들을 사용해야한다. ###
    spring.jpa.hibernamte.ddl-auto=validate
    spring.jpa.generate-ddl=false
    # 매핑을 할 수 있는 상황인지 검증만 하는 것
    ```
- 만약 운영 상황에서 새로운 컬럼을 추가했다면?
    - `User.java`에 아래 컬럼 추가
        ```java
        private String email;
        ```
    - validate라면 실행하면 에러가 나고 종료된다.
    - update라면 스키마가 없는 것만 바꿔준다.
    - 컬럼명 자체가 바뀌면 (username -> nickname), hibernate는 그것을 알아채지 못한다. (update일 경우에)

## III. 마이그레이션 툴
> Flyway
- DB 스키마 변경이나, 데이터 변경을 버전관리와 같이 관리할 수 있다.
- ... 장고에서 마이그레이션 파일 만드는걸 직접하는거라고 생각하면 된다.... (...?.....)
- 사용법
    - 의존성 추가
        ```xml
        <dependency>
            <groupId>org.flywaydb</groupId>
            <artifactId>flyway-core</artifactId>
        </dependency>
        ```
    - ddl은 운영상황인 validate로 맞춰놓는다.
    - `main/resources/db.migration` 생성
        - 여기에 하나하나 쌓아 나가는 것이다.
        - `V1_init.sql`
            ```sql
            drop table if exists users;
            drop sequence if exists hibernate_sequence;
            create sequence hibernate_sequence start with 1 increment by 1;
            create table users (id bigint not null, username varchar(255), primary key (id));
            ```
    - `User.java`에 새로운 컬럼(예를 들어 active)을 생성하고 실행하면 에러가 난다. (validate에 걸려서)
    - 이때, 마이그레이션 파일을 새로 만들고 실행할 수 있다. (원래 있던 파일들 예를 들어 V1_init.sql은 **저어어어어어얼대** 변경해서는 안된다. )
        - `V2_add_active.sql`
            ```sql
            ALTER TABLE users ADD COLUMN active BOOLEAN;
            ```
    - 이러고 다시 실행하면 마이그레이션 파일을 읽고 마이그레이트를 진행 한 후 validate를 하기 때문에, 에러없이 실행된다.