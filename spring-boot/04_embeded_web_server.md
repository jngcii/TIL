# 내장 웹 서버

###### 2020.07.03

- 스프링부트는 웹 서버가 아니다!
- 아래와 같이 하면 서버로써 작동하지 않는다는 것이 증거
    ```java
    @SpringBootApplication
    public class Application {

        public static void main(String[] args) {

            SpringApplication application = new SpringApplication(Application.class);
            application.setWebApplicationType(WebApplicationType.NONE);
            application.run(args);

        }

    }
    ```
    - 바로 종료가 된다.
- 스프링 부트는 내장 서블릿 컨테이너를 쉽게 사용할 수 있게 해주는 툴, 스프링 프레임워크를 쉽게 사용할 수 있게 해주는 툴
- 스프링 부트 자체가 서버는 아니다.
- 네티, 제티, 톰캣 등이 서버이다.
  - 얘네들은 자바 코드로 서버를 만들 수 있는 기능을 제공한다.
- 기본적으로 스프링부트 애플리케이션을 만들면, 의존성에 톰캣이 들어와 있다.

## I. 자바 코드로 톰캣 만들기
```java
public class Application {

    public static void main(String[] args) throws LifecycleException {

        Tomcat tomcat = new Tomcat();
        tomcat.setPort(8080);

        Context context = tomcat.addContext("/", "/");

        HttpServlet servlet = new HttpServlet() {
            @Override
            protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
                PrintWriter writer = resp.getWriter();
                writer.println("<h1>Hello, peter.j!</h1>");

            }
        };

        String servletName = "helloServlet";
        tomcat.addServlet("/", servletName, servlet);
        context.addServletMappingDecoded("/hello", servletName);

        tomcat.getConnector();
        tomcat.start();
        tomcat.getServer().await();

    }
}
```

- 이렇게 쓰지 않아도 저절로 되는 이유
- 이런 설정이 어디에 있길래 스프링 부트가 서블릿 컨테이너를 띄워 주는 것인가?
  - 자동설정과 관련이 있다.
  - External Library - autoconfigurer - META-INF - spring.factories를 열어 보면 그 중에 **`ServletWebServerFactoryAutoConfiguration`과 `DispatcherServletAutoConfiguration`을 볼 수 있다.

### `ServletWebServerFactoryAutoConfiguration`
- 서블릿 웹 서버를 생성하고 커스터마이징

### `DispatcherServletAutoConfiguration`
- Spring MVC의 핵심 클래스인 DispatcherServlet을 등록
    > DispatcherServlet은 결국 HttpServlet을 상속해서 만든다.
- 이 설정에서는 dispatcherServlet을 만들고 servlet Container에 등록하는 일이 일어난다.

### 이 두개의 설정이 왜 떨어져있나?
- 서블릿 컨테이너는 바꿔 낄 수 있고, 서블릿은 고정되어 있기 때문이다.
- 서블릿 컨테이너를 교체할 수 있다.


## II. 내장 서블릿 컨테이너 응용
- 스프링부트는 기본적으로 서블릿 기반의 웹 MVC 애플리케이션을 개발할 때 톰캣을 사용하게 되어있다. ( 자동설정에 의해서 )
- `@ConditionalOnClass`에 의해서 톰캣용 자동설정 파일이 읽혀지고 톰캣이 만들어져 사용하게 된다.
- `spring-boot-starter-web` dependency를 추가하므로써 `spring-boot-starter-tomcat`을 가져온다.

### 1) 다른 서블릿 컨테이너 사용하는 방법
- 먼저 `spring-boot-starter-tomcat`을 제외시켜 준다.
    ```xml
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-tomcat</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
    </dependencies>
    ```
- 새로운 의존성으로 사용하고싶은 컨테이너의 의존성을 스타터를 사용해서 넣으면 된다. (undertow, jetty, ...)
    ```xml
    <dependencies>
        ...

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jetty</artifactId>
        </dependency>
    </dependencies>
    ```
    > 만약 이 의존성을 추가하지 않고 tomcat만 제외했을 경우 웹 애플리케이션이 아니라 그냥 애플리케이션이라 애플리케이션이 실행되고 바로 종료된다.

### 2) 애플리케이션 타입 바꾸기
- 기본적으로 스프링부트는 의존성의 그대로이면 웹애플리케이션으로 만들려는 시도를 한다.
- 이때 타입을 SERVLET이 아닌 값으로 바꿔주면 웹애플리케이션이 아니게 된다.
- 방법은 main함수에서 타입을 바꾸는 방법이 있고, 아래의 방법은 프로퍼티를 사용해서 바꾸는 방법이다.
    - `main/resources/application.properties`
        ```properties
        spring.main.web-application-type=none
        # none, servlet, reactive 등 존재
        ```

### 3) 포트 바꾸기
- `main/resources/application.properties`
    ```properties
    server.port=7070
    # 0으로 하면 비어있는 무작위 포트 사용
    ```

### 4) properties 파일에 정해놓은 포트를 애플리케이션 안에서 어떻게 쓸 것인가?
- EventListener 역할을 하는 Bean을 만든다. (`PortListener`라는 클래스 생성)
    ```java
    @Component
    public class PortListener implements ApplicationListener<ServletWebServerInitializedEvent> {

        @Override
        public void onApplicationEvent(ServletWebServerInitializedEvent servletWebServerInitializedEvent) {

            ServletWebServerApplicationContext applicationContext = servletWebServerInitializedEvent.getApplicationContext();
            System.out.println(applicationContext.getWebServer().getPort());

        }

    }
    ```

## III. HTTPS, HTTP/2 적용하기
-- 나중에 --