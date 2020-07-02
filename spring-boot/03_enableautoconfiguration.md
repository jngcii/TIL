# 자동 설정 (enableAutoConfiguration)

###### 2020.07.02


## I. `@EnableAutoConfiguration`
- `@SpringBootApplication` 어노테이션만 붙였는데 톰캣 서버가 동작할 수 있는 이유
  - `@SpringBootApplication` 어노테이션 안의 `@EnableAutoConfiguration`이라는 어노테이션 때문이다.
  - 아래의 코드는
    ```java
    @SpringBootApplication
    public class Application {
        public static void main(String[] args) { SpringApplication.run(Application.class, args); }
    }
    ```
  - 아래와 같이 바꿀 수 있다.
    ```java
    @SpringBootConfiguration      // 사실상 @Configuration과 같다.
    @ComponentScan
    @EnableAutoConfiguration
    public class Application {
        public static void main(String[] args) { SpringApplication.run(Application.class, args); }
    }
    ```
- 스프링부트는 `@ComponentScan`과 `@EnableAutoConfiguration`으로 두 단계로 빈을 등록한다.
  - `@ComponentScan`이 일어난 다음에 `@ComponentScan`으로 추가적인 빈들을 읽어서 등록한다.
- `@ComponentScan`이 하는 일
  - 하위 패키지에 있는 클래스들 중에 `@Component`라는 어노테이션을 갖는 클래스들을 스캔해서 빈으로 등록
  - `@Service`, `@Repository`, `@Controller` 등 모두 안으로 들어가보면 `@Component`가 있다.
  - `@Configuration`을 붙인 것 역시 그 자신도 빈이 된다.
- `@EnableAutoConfiguration`이 하는 일
  - 자바 리소스의 메타 디렉터리 안에 spring.factories라는 파일이 있고, 그 안에 autoconfiguration 키값에 엄청 많은 설정 파일들이 있는데 이 모든 설정파일들은 `@Configuration`이라는 어노테이션이 붙어있다. 즉, `@EnableAutoConfiguration`이라는 어노테이션은 스프링 메타 파일의 모든 설정 파일을 빈으로 등록한다.
  - 그런데, 각 설정 파일의 `@Configuration` 어노테이션 밑에는 `@ConditionalOn*` 어노테이션이 붙어있고 이 조건에 따라 특정 설정 클래스만 빈으로 등록된다.


## II. Custom Auto Configuration

### 1) 스프링 설정 모듈 만드는 방법
- xxx-Spring-Boot-Autoconfigure : 자동 설정 모듈
- xxx-Spring-Boot-Starter : 의존성 정의 모듈
- 두 가지를 하나의 모듈로 하고 싶을 땐? xxx-Spring-Boot-Starter

### 2) 구현
1. 새 프로젝트 (artifactId : jngcii-spring-boot-starter)
2. 의존성 추가
    ```xml
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-autoconfigure</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-autoconfigure-processor</artifactId>
            <optional>true</optional>
        </dependency>
    </dependencies>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>2.3.1.RELEASE</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    ```
3. `com.jngcii` 패키지 만들고 `Holoman`이라는 클래스 만들기
   ```java
   class Holoman {

      String name;
      int howLong;

      // getter
      // setter
      // toString

   }
   ```

> 이 Holoman 같은 설정 파일은 다른 프로젝트에 있는 경우가 흔할 것이다.

4. `HolomanConfiguration`이라는 클래스 생성
    ```java
    package com.jngcii;

    import org.springframework.context.annotation.Bean;
    import org.springframework.context.annotation.Configuration;

    @Configuration
    public class HolomanConfiguration {

        @Bean
        public Holoman holoman() {
            Holoman man = new Holoman();
            man.setHowLong(5);
            man.setName("jngcii");
            return man;
        }

    }
    ```
5. `src/main/resource/META-INF에 spring.factories 파일 만들기
    ```
    org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
      com.jngcii.HolomanConfiguratio
    ```
6. `mvn install`
    - 이 프로젝트를 빌드를 해서 `jar` 파일로 생성된 것을 다른 프로젝트에서 사용할 수 있도록 로컬 메이븐 저장소에 설치한다.

7. 원래의 프로젝트에 의존성을 추가한다. (복붙)
    ```xml
    <dependency>
      <groupId>com.jngcii</groupId>
      <artifactId>jngcii-spring-boot-starter</artifactId>
      <version>1.0-SNAPSHOT</version>
    </dependency>
    ```

8. 의존성 사용하기 (`HolomanRunner.java`)
    ```java
    @Component
    class HolomanRunner implements ApplicationRunner {

        @Autowired
        Holoman holoman;

        @Override
        public void run(ApplicationArguments args) throws Exception {
            System.out.println(holoman);
        }

    }
    ```
    > - 어디서도 Holoman을 빈으로 등록하지 않았는데 어떻게 사용하나??
    > - Autoconfiguration을 통해 설정파일과 빈을 등록

9. 이렇게 `@EnableAutoConfiguration`을 통해 빈이 등록되면, 사용자가 같은 이름의 빈을 등록할 수가 없다. (옛날에는 무시됐고 이제는 에러가 발생한다. - 빈 오버라이딩이 스프리부트2.1부터 막혔기 때문)
10. 해결방법
    - starter프로젝트의 빈에 `@ConditionalOnMissingBean`을 넣어주면 해당 빈이 없을 경우에만 등록하라는 얘기가 된다.
    - 다시 `mvn install` 후 refresh하면 된다.