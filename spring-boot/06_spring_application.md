# SpringApplication 클래스

###### 2020.07.03

## I. 애플리케이션 실행

```java
@SpringBootApplication
public class Application {

    public static void main(String[] args) {

        SpringApplication application = new SpringApplication(Application.class);
        application.run(args);

    }

}
```
- 스프링부트 애플리케이션을 실행하는 방법
- 아무런 옵션을 붙이지 않고 이 상태로 실행하면 기본 로그 레벨인 **INFO 레벨**로 실행된다.
- `run application` 버튼의 옆에 Application 버튼을 누르고 `Edit Configuration`을 누르면 옵션을 설정할 수 있는데, `Environment`의 `VM options`에 `-Ddebug`를 넣거나 `Program arguments`에 `--debug`를 넣으면 debug모드로 애플리케이션이 동작하고 로그 또한 debug 레벨로 출력된다.

## II. 부가 기능

### 1) Failure Analyzer
- 에러가 났을 때, 에러 메세지를 예쁘게 출력해주는 기능
- 기본적으로 스프링부트는 여러가지 failure analyzer를 등록하고 있다.

### 2) banner
- application이 시작할때 콘솔에 보이는 큰 배너형 문구
- 바꾸고 싶으면 `main/resources/banner.txt` 파일을 만들고 배너를 만들면 된다.
- 변수를 넣을 수 있다.
- 예시
    ```txt
    =====================================================
    Jngcii Spring Boot Application ${spring-boot.version}
    =====================================================
    ```
    - 다만 manifest 파일이 있을 경우에만 찍히는 변수들이 있다.


## III. Application Event
- 스프링, 스프링부트에서 기본적으로 제공해주는 다양한 시점의 이벤트들이 있다.
- application이 시작될 때, context를 만들었을 때, context가 refresh가 됐을 때 등...

### application Event Listener를 만드는 방법
- `SampleListener`라는 클래스 생성
    ```java
    // @Component
    public class SampleListener implements ApplicationListener<ApplicationStartingEvent> {

        @Override
        public void onApplicationEvent(ApplicationStartingEvent applicationStartingEvent) {
            System.out.println("=====================");
            System.out.println("Starting Application!");
            System.out.println("=====================");
        }
    }
    ```
    - ApplicationListener의 제네릭 타입에 원하는 이벤트 클래스를 넣어준다.
    - **application context가 만들어진 후의 이벤트와 만들어지기 전의 이벤트는 다르다.**
    - application context가 만들어진 후의 이벤트는 그 이벤트의 리스너가 빈이라면 빈을 실행할 수 있다.
    - application context가 만들어지기 전의 이벤트는 리스너를 빈으로 등록한다 하더라도 리스너가 동작을 안한다.
    - 그래서 사실상 `@Component` 어노테이션은 의미가 없다. (빼버림)
    - ApplicationStartingEvent : application 맨 처음에 발생하는 이벤트 (application context가 만들어지기 전)
    - 이럴 경우에는 어떻게하나?
        - 직접 등록해줘야 한다!
            ```java
            public static void main(String[] args) {
                SpringApplication app = new springApplication(Application.class);

                app.run(args);
            }
            ```
        - 그럼 배너 전에 완전 처음 부분에 리스너가 동작한다.


## IV. 애플리케이션 argument 사용하기
- VM options : `-Dfoo`
- Program arguments : `--bar`
- `ArgsPrinter` 클래스 생성
    ```java
    @Component
    public class ArgsPrinter {

        public ArgsPrinter(ApplicationArguments args) {
            System.out.println("foo : " + args.containsOption("foo"));
            System.out.println("bar : " + args.containsOption("bar"));
        }

    }
    ```
    - 어떤 빈의 생성자가 한개고 생성자의 파라미터 빈일 경우에는 그 빈을 스프링이 알아서 주입을 해준다.
    - 결과는 foo는 없고 bar는 있다고 나온다.
    - 결론 : **Program arguments만 (`--`옵션을 사용하는 것만) ApplicationArguments 빈에 들어있다.**
- 콘솔에서 해도 똑같다.
    1. 프로젝트 루트에서 mvn 실행
        - `$ mvn clean package`
        - 패키지 만들기 (빌드)
    2. `jar` 파일 직접 실행
        - `$ java -jar target/springinit-0.0.1-SNAPSHOT.jar -Dfoo --bar`

## V. `ApplicationRunner`
> 애플리케이션 실행 뒤 뭔가 더 실행하고 싶을 때
```java
@Component
class SampleCode implements ApplicationRunner {

    @Override
    public void run(ApplicationArguments args) throws Exception {
        System.out.println("foo : " + args.containsOption("foo"));
        System.out.println("bar : " + args.containsOption("bar"));
    }

}
```
