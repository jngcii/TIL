# 외부 설정

###### 2020.07.03

- 애플리케이션에서 사용하는 여러가지 설정 값들을 애플리케이션 밖이나 안에 정의할 수 있는 기능
- 사용할 수 있는 외부 설정
  - `application.properties`
  - YAML
  - 환경 변수
  - 커맨드 라인 arguments

## I. `application.properties`
- 흔히 볼 수 있는 가장 중요한 애플리케이션 설정 파일
- 이 파일은 스프링 부트가 애플리케이션을 구동할 때 자동으로 로딩하는 파일 이름이다. ( 규약 )
    ```properties
    jngcii.name = hyungsoo
    ```
    - 위와 같이 key, value 형태로 값을 정의하면 애플리케이션에서 참조해서 사용할 수 있다.
    - 참조해서 사용하는 방법 중 가장 기본적인 방법
        ```java
        @value("${jngcii.name}")
        private String name;

        @Override
        public void run(ApplicationArguments args) throws Exception {
            System.out.println(name);
        }
        ```

### 프로퍼티 우선순위
1. 유저 홈 디렉토리에 있는 spring-boot-dev-tools.properties
2. 테스트에 있는 @TestPropertySource
3. @SpringBootTest 애노테이션의 properties 애트리뷰트
4. 커맨드 라인 arguments
    - `java -jar target/~~ --jngcii.name=hs`를 통해 실행할 경우 properties파일에 들어있는 값을 덮어씌운다.
5. SPRING_APPLICATION_JSON (환경 변수 또는 시스템 프로티) 에 들어있는 프로퍼티
6. ServletConfig 파라미터
7. ServletContext 파라미터
8. java:comp/env JNDI 애트리뷰트
9.  System.getProperties() 자바 시스템 프로퍼티
10. OS 환경 변수
11. RandomValuePropertySource
12. JAR 밖에 있는 특정 프로파일용 application properties
13. JAR 안에 있는 특정 프로파일용 application properties
14. JAR 밖에 있는 application properties
15. JAR 안에 있는 application properties
16. @PropertySource
17. 기본 프로퍼티 (SpringApplication.setDefaultProperties)
> 우선순위가 높은 프로퍼티가 overriding한다.

### `application.properties` 파일의 위치 (우선순위 높은 순)
1. file system : `./config/application.properties`
2. file system : `./application.properties`
3. classpath : `/config/application.properties`
4. classpath : `/application.properties`
> **### classpath와 current directory의 기준 ###**
> 현재 디렉터리 : 애플리케이션을 실행하는 위치
> - 예 : `/users/jngcii/workspace/`에서 java -jar example.jar를 실행하면 여기서 `/users/jngcii/workspace/`가 1, 2에서 말하는 현재 디렉터리
> 
> 클래스패스 : `src/main/resource/`를 의미한다고 보면 된다.


## II. `@ConfigurationProperties`
- 타입-세이프 프로퍼티
- 위 어노테이션을 사용하려면 아래 의존성이 필요하다.
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-configuration-processor</artifactId>
        <optional>true</optional>
    </dependency>
    ```
- 여러 프로퍼티를 묶어서 가져올 수 있다.
    ```java
    @Component
    @ConfigurationProperties("jngcii")
    public class JngciiProperties {

        private String name;
        private int age;
        private String username;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public int getAge() {
            return age;
        }

        public void setAge(int age) {
            this.age = age;
        }

        public String getUsername() {
            return username;
        }

        public void setUsername(String username) {
            this.username = username;
        }
    }
    ```
    ```java
    @Component
    public class ArgsPrinter implements ApplicationRunner {

        @Autowired
        JngciiProperties jngciiProperties;

        @Override
        public void run(ApplicationArguments args) throws Exception {
            System.out.println(jngciiProperties.getName());
            System.out.println(jngciiProperties.getAge());
        }
    }
    ```
- 빈으로 등록해서 다른 빈에 주입할 수 있다.
  - 원래는 `@EnableConfigurationProperties` Application 클래스에 어노테이션을 달아서 등록을 해줘야하는데 이것은 내부적을 등록되어있다.
  - 그래서 `@Component` 어노테이션을
  - `@Bean`
- 융통성있는 바인딩 : properties 파일에 아래 아무거나 적어도 매핑해준다.
  - `context-path`
  - `context_path`
  - `contextPath`
  - `CONTEXTPATH`
<!-- - 프로퍼티 타입 컨버전
  - `@DurationUnit` -->
- 프로퍼티 값 검증
  - `@Validated`
  - JSR-303 (`@NotNull`, ...) 의 구현체를 사용
    ```java
    @Component
    @ConfigurationProperties("jngcii")
    @Validated
    public class JngciiProperties {

        @NotEmpty
        private String name;
        private int age;
        private String username;
    ```