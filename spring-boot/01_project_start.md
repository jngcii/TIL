## Project start

###### 2020.07.02

## I. 스프링부트 문서 참고
- `https://spring.io/projects/spring-boot` - learn - Reference Doc (current)

## II. 프로젝트 시작
1. IntelliJ에서 `Create New Project...`
2. `Spring initialize` 혹은 `Maven`을 통해 프로젝트 시작
3. `pom.xml` 스프링 부트 문서를 따라 아래와 같이 변경
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>com.jngcii</groupId>
        <artifactId>first-spring-project</artifactId>
        <version>1.0-SNAPSHOT</version>

        <parent>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-parent</artifactId>
            <version>2.3.1.RELEASE</version>
        </parent>

        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-web</artifactId>
            </dependency>
        </dependencies>

        <build>
            <plugins>
                <plugin>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-maven-plugin</artifactId>
                </plugin>
            </plugins>
        </build>

    </project>
    ```
    > `parent`, `dependencies`, `build` 추가
4. `main/java`에서 패키지 만들고 안에 `main`메서드를 담을 클래스 만들기 (`Application.class`)
5. 여기까지하면 기본 구조를 만든 것이다. (`Spring initializing`을 사용하면 여기까지 만들어져있다.)
6. 여기까지 만든 프로젝트를 실행하는 방법
   - main에서 run application을 통해
   - `$ mvn package`후 만들어진 jar파일을 실행 (`$ java -jar target/fisrt-spring-project-1.0-SNAPSHOT.jar`)

## III. 어떻게 이것이 가능한가?
- Spring MVC가 동작하려면 여러가지 dependency가 필요한데, 어떻게 수많은 그 의존성이 들어왔는가?
- Spring MVC 앱을 설정해야하는데, (dispatcherServlet, lister에 webApplicationContext 어떤것을 쓸지, 빈 설정 파일 제공 등) 어떻게 알아서 됐는가?
- 어떻게하여 내장 톰캣에 사용되었는가?
- 이 것은 `@EnableAutoConfiguration` 어노테이션과 밀접한 관련이 있다.