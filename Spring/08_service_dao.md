# Service & Dao 객체 구현

###### 2020.06.28

## I. 한글 처리
- `web.xml`의 `<web-app />` 태그 속의 맨 뒤에 아래 태그 붙여넣기
    ```xml
    <filter>
        <filter-name>encodingFilter</filter-name>
        <filter-class>
		    org.springframework.web.filter.CharacterEncodingFilter
        </filter-class>
        <init-param>
            <param-name>encoding</param-name>
            <param-value>UTF-8</param-value>
        </init-param>
        <init-param>
            <param-name>forceEncoding</param-name>
            <param-value>true</param-value>
        </init-param>
    </filter>

    <filter-mapping>
        <filter-name>encodingFilter</filter-name>
        <url-pattern>/*</url-pattern>
    </filter-mapping>
    ```
- jsp 파일 맨 위에 UTF-8 설정 넣어주기
  ```jsp
  <%@ page contentType="text/html;charset=UTF-8" pageEncoding="UTF-8" language="java" %>
  ```

## II. Service & Dao 객체 구현

### 1) 방법 1
- new 연산자를 이용한 service 객체 생성 및 참조
  ```java
  MemberService service = new MemberService();
  ```

### 2) 방법 2
- 스프링 설정파일을 이용한 서비스 객체 생성 및 의존 객체 자동 주입
  ```xml
  <beans:bean id="service" class="com.jngcii.pjt.member.service.MemberService"></beans:bean>
  ```
  ```java
  @Autowired
  MemberService service;
  ```

### 3) 방법 3
- 어노테이션을 이용해 서비스 객체 생성 및 의존 객체 자동 주입
  ```java
  // @Service
  // @Component
  // @Repository
  @Repository("memService")
  public class MemberService implements IMemberService {
      // ...
  }
  ```
  ```java
  // @Autowired
  @Resource(name="memService")
  MemberService service;
  ```
