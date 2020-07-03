# Profile

###### 2020.07.03

- 어떤 프로파일을 활성화시킬것인가?
- 프로퍼티 파일에서 지정된 프로퍼티의 빈만 컨테이너에 등록이 된다.
- `application.properties`
    ```properties
    spring.profiles.active=prod
    ```
- `/com.jngcii/config/ProdConfiguration.java`
    ```java
    @Profile("prod")
    @Configuration
    public class ProdConfiguration {

        @Bean
        public String hello() {
            return "Hello, Production";
        }

    }
    ```
- `/com.jngcii/config/DevConfiguration.java`
    ```java
    @Profile("dev")
    @Configuration
    public class DevConfiguration {

        @Bean
        public String hello() {
            return "Hello, Development";
        }

    }
    ```
- `JngciiRunner.java`
    ```java
    @Component
    public class JngciiRunner implements ApplicationRunner {

        @Autowired
        String hello;

        @Override
        public void run(ApplicationArguments args) throws Exception {
            System.out.println(hello);
        }
    }
    ```
- **이 경우에는 프로퍼티 파일에 prod를 active로 지정해놨기 때문에 `hello, Production`이 출력된다.**
- 프로파일용 프로퍼티도 만들 수 있다.
    - `application-{profile}.properties`