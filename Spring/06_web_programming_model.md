# 웹 프로그래밍 설계 모델

###### 2020.06.27

> 스프링 MVC 프레임워크 기반의 웹 프로그래밍 구조

## I. 웹 프로그래밍을 구축하기 위한 설계 모델
> Model 1 & Model 2
### 1) Model 1
- MVC 기능을 모듈화시키지 않고 하나의 파일로 처리
- 장점 : HTML 코드에 자바 코드도 있어서 개발이 편하다
- 단점 : 유지 보수가 어렵다. 프로젝트의 확장이 어렵다.

### 2) Model 2
- MVC 기능을 모듈화
  - M (Model) : Service가 Dao를 이용해 조작
  - V (View) : 보여지는 부분을 처리
  - C (Controller) : 처음 요청을 받고 라우팅하고 특정 Service가 처리할 수 있게 한다.

## II. 스프링 MVC 프레임워크 설계 구조
![](assets/Screen%20Shot%202020-06-27%20at%203.22.28%20PM.png)
- Controller : 여러개 있다.
- DispatchServlet : 요청을 받고 HandlerMapping에게 요청을 준다.
- HandlerMapping : 많은 Controller중에 가장 적합한 Controller를 선택
- HandlerAdapter : 선택한 Controller의 메서드들 중 가장 적합한 메서드 선택
- ViewResolver : Controller로부터 모델데이터와 View에 대한 정보가 왔는데 이 것에 대한 처리결과를 출력할 View(JSP파일)를 선택

## III. DispatcherServlet 설정
- 웹 어플리케이션을 개발할때 먼저 설정을 해줘야한다. (`web.xml`에 매핑)
- `WEB-INF/web.xml`을 생성하고 `<servlet>`태그와 `<servlet-mapping>`태그를 이용한다.
- `web.xml` 설정 방법
  ```xml
  <servlet>
    <servlet-name>servlet name</servlet-name>
    <servlet-class>패키지이름을 포함한 전체 서블릿명<servlet-class>
  </servlet>

  <servlet-mapping>
    <servlet-name>servlet name</servlet-name>
    <url-pattern>/매핑명<ulr-pattern> 
  </servlet-mapping>
  ```
- DispatchServlet을 등록하는 `web.xml` 파일 작성
  ```xml
  <servlet>
    <servlet-name>appServlet</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
      <param-name>contextConfigLocation</param-name>
      <param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>

  <servlet-mapping>
    <servlet-name>appServlet</servlet-name>
    <url-pattern>/</url-pattern>
  </servlet-mapping>
  ```
  - `/WEB-INF/spring/appServlet/servlet-context.xml` : 컨테이너를 생성하는 스프링 설정 파일
  - `web.xml`에 DispatcherServlet(웹어플리케이션에 진입하기 위한 첫번째 관문)을 동록하고 등록할때 초기 파라미터로 스프링 설정 파일을 설정해주면 이 설정 파일을 기반으로 스프링 컨테이너를 생성한다.
  - 컨테이너가 생성되면 HandlerMapping, HandlerAdapter와 ViewResolver는 내가 생성하지 않아도 자동으로 생성이 된다.
  - 만약 초기 파라미터를 설정하지 않으면?
    - 자동으로 스프링 프레임워크가 특정한 이름(`appServlet-context.xml`)을 이용해서 스프링 설정 파일을 생성한다.

## IV. Controller 객체
- HandlerAdapter나 HandlerMapping 등은 스프링 프레임워크가 자동으로 생성해주지만, Controller는 개발자가 직접 작성해야한다.
- `servlet-context.xml` (스프링 설정 파일)에 아래 태그를 추가해줘야한다.
  ```xml
  <annotation-driven />
  ````
  - 위 태그 하나로 스프링 컨트럴러를 사용하기 위한 여러가지 도와주는 클래스들이 Bean객체로 생기게 된다.

### 1) `@Controller`
- Controller 객체로 사용할 클래스 정의
  ```java
  @Controller
  public class HomeController {
      // ...
  }
  ```

### 2) `@RequestMapping`
> `@Controller` 어노테이션으로 컨트럴러는 찾았는데 사용자가 요청한 기능에 대해 어떤 메서드가 실행되야하는지 찾는 방법
- `@RequestMapping` 어노테이션 사용
  ```java
  @Controller
  public class HomeController {
      // ...

      @RequestMapping("/success")
      public String success(Model model) {
          // ...

          return "success";
      }

      // ...
  }
  ```

### 3) Model 타입의 파라미터
- 개발자는 Model 객체에 데이터를 담아서 DispatcherServlet에 전달할 수 있다.
- DispatcherServlet에 전달된 Model 데이터는 View에서 가공되어 클라이언틍한테 응답처리된다.
- Controller에서 Service, Dao와 작업을 하고 Model과 View 결과를 DispatcherServlet로 돌려준다.
- Model데이터는 View에서 사용할때, model.setAttribute()로 사용한다.


## V. View 객체
```xml
<beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
  <beans:property name="prefix" value="/WEB-INF/view/" />
  <beans:property name="suffix" value=".jsp />
</beans:bean>
```
- jsp 파일명 : `/WEB-INF/views/success.jsp`

## VI. 전체적인 웹 프로그래밍 구조
![](assets/Screen%20Shot%202020-06-27%20at%204.10.31%20PM.png)