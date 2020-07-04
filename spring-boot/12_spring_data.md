# Spring Data

###### 2020.07.04

| SQL DB | NoSQL DB |
| --- | --- |
| 인메모리 데이터베이스 지원 | Redis (Key/Value) |
| DataSource 설정 | MongoDB (Document) |
| DBCP 설정 | Neo4J (Graph) |
| JDBC 사용하기 |  |
| 스프링 데이터 JPA 사용하기 |  |
| jooQ 사용하기 |  |
| 데이터베이스 초기화 |  |
| 데이터베이스 마이그레이션 툴 연동하기 |  |

## I. in-memory database
- 스프링부트가 지원하는 인메모리 데이터베이스
  - H2 (추천 - 콘솔때문에)
  - HSQL
  - Derby
- spring-jdbc가 클래스패스에 있으면 자동으로 필요한 빈들(`DataSource`와 `JdbcTemplate`)을 설정해준다.
- 스프링부트 프로젝트 시작할 때, **web 탭에서 web을, sql 탭에서 H2와 JDBC를 선택한다.**
- H2 의존성이 클래스패스에 들어있고 아무런 데이터설정을 하지 않으면, 스프링부트는 자동으로 인메모리 데이터베이스를 설정을 해준다.
- 사용 예시
    ```java
    @Component
    public class H2Runner implements ApplicationRunner {

        @Autowired
        DataSource dataSource;

        @Autowired
        JdbcTemplate jdbcTemplate;

        @Override
        public void run(ApplicationArguments args) throws Exception {
            try (Connection conn = dataSource.getConnection()) {
                System.out.println(conn.getMetaData().getURL());
                System.out.println(conn.getMetaData().getUserName());

                Statement statement = conn.createStatement();
                String sql = "CREATE TABLE user (id INTEGER NOT NULL, username VARCHAR(255), PRIMARY KEY (id))";
                statement.executeUpdate(sql);
            } catch (Exception e) {
                e.printStackTrace();
            }

            jdbcTemplate.execute("INSERT INTO user VALUES (1, 'hyungsoo')");
        }

    }
    ```

## II. MySQL 설정하기

### 1) DBCP
- 데이터베이스 커넥션을 만드는 과정은 굉장히 많은 작업이 일어나는 과정이다. 그래서 미리 만들어놓고 요청이 올때마다 만들어져있는 커넥션을 가져다가 쓰는 방법이 커넥션 풀이다.
  - 몇 개를 만들어놓을 것인가
  - 얼마동안 안쓰이면 몇개를 없앨것이가
  - 최소한 얼마나 만들어 놓을것이가
  - 등에 대한 설정을 할 수 있다.
  - 동시에 일할 수 있는 커넥션 개수는 CPU 코어 개수랑 같다.
- 애플리케이션 성능에 아주아주 핵심적인 역할을 한다. (버그가 있으면 안된다.)
- 지원하는 DBCP
  - HikariCP (기본)
    - https://github.com/brettwooldridge/HikariCP#frequently-used
  - Tomcat CP
  - Commons DBCP2
  - 세가지가 모두 클래스패스에 있으면 hikari를 사용한다.
- DBCP 설정
  - `spring.datasource.hikari.*`
  - `spring.datasource.tomcat.*`
  - `spring.datasource.dbcp2.*`
- 스프링 부트에서 DBCP 설정하는 방법
  - `application.properties` 파일에 아래와 같이 `spring.datasource.~~` 추가
    ```properties
    # ...
    spring.datasource.hikari.max-pool-size=4
    ```
    > 이 값들은 HikariDataSource가 상속하고 있는 HikariConfig에서 온다. (여기에 다 설정되어 있다.)

### 2) MySQL
- MySQL에 접속할 수 있는 커넥터 의존성 추가
    ```xml
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
    </dependency>
    ```