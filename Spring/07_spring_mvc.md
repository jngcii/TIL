# 스프링 MVC 웹서비스

###### 2020.06.27

## I. 프로젝트 시작

### 1) 웹서버(톰캣) 다운로드
- `http://tomcat.apache.org/`에서 다운로드

### 2) 웹서버(톰캣)와 이클립스 연동
- [Preferences] - [Server] - [Runtime Environment]
- Servers 탭에서 이용중인 서버 더블클릭 - Server Location에서 Use Tomcat installation 선택 - Server Options에서 public module contexts to separate XML files 선택 - Ports에서 HTTP 포트를 8090으로 수정 (나중에 다른 것들과 충돌날까봐) - 저장
- 아래 탭쪽 퍼스팩티브 오른쪽에서 Publish to the server 누르고 Start the server

### 3) 이클립스에 STS 설치
- 서버를 만들었으면 웹서비스 기능구현을 해야한다.
- 그러려면 web.xml을 만들고 servlet(dispatcherServlet)등록도 하고 해야한다.
- STS (Spring Tool Suit) : 이런것들을 일일이 하지않아도, 기본적으로 자동으로 설정해주는 플러그인
- 방법 (두가지 방법)
  - [Menu Bar] - [Help] - [Eclipse MarketPlace] - sts검색 - 모두 체크 후 설치
  - [Menu Bar] - [Help] - [Install New Software] - 직접 사이트 입력
    - 자세한 버전 확인 : http://dist.springsource.com/snapshot/STS/nightly-distributions.html
- 그러면 Spring MVC Project를 이클립스를 이용해 생성할 수 있다.

### 4) STS를 이용한 웹프로젝트 생성
- [New] - [Other...] - [Spring] - [Spring Legacy Project] - Project name 입력 - [Spring MVC Project] - [Next] - package명 작성 - 끝
> Legacy : 하위 호환을 위해 신규 프로그램 속에 남겨두는 기존 프로그램의 소스 코드


## II. 프로젝트 구조

### 1) 프로젝트 전체 구조
- `/src/main/java/`
  - java파일들이 위치한다.
  - 주로 패키지에 묶어서 관리한다.
  - 웹 애플리케이션에서 사용하는 Controller, Service, Dao 객체들이 위치한다.
- `/src/main/resources/`
  - JSP파일을 제외한 html, css, js 파일 등이 위치한다.
- `/src/main/webapp/`
  - 웹 관련된 파일들 (스프링 설정파일, JSP파일, HTML파일 등..)이 위치한다.
- `/src/main/webapp/spring/`
  - 스프링 컨테이너를 생성하기 위한 스프링 설정 파일이 위치한다.
- `/src/main/webapp/views/`
  - View로 사용될 JSP 파일들이 위치한다.
- `/src/main/webapp/web.xml`
  - 웹 설정 파일
- `/pom.xml`
  - 메일 레파지토리에서 프로젝트에 필요한 라이브러리를 내려받기 위한 메이븐 설정 파일

### 2) `web.xml`
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
- 웹 애플리케이션에서 최초 사용자의 요청이 발생하면 가장 먼저 DispatcherServlet이 사용자의 요청을 받는다고 했다. 따라서 개발자는 DispatcherServlet을 서블릿으로 등록해주는 과정을 설정해 주어야 한다. 그리고 사용자의 모든 요청을 받기 위해서 서블릿 매핑 결로는 `/`로 설정한다.

### 3) dispatcherServlet
- `web.xml`에서 서블릿으로 등록이 됨
- `HandlerMapping`과 `HandlerAdapter`를 이용
  - `HandlerMapping`
    - 사용자의 요청에 부합하는 컨트롤러 검색
    - 프로젝트에 존재하는 모든 Controller 객체 검색
    - 검색 결과를 DispatcherServlet 객체에 알려준다.
  - `HandlerAdapter`
    - 이 객체로 사용자의 요청에 부합하는 컨트럴러의 메서드 실행 요청
    - 적합한 메서드를 찾아 해당 Controller객체의 메서드를 실행
- Controller의 비즈니스 로직이 수행되고 그 과정에서 Service, Dao, DB를 거친 작업이 일어난다.
- 메서드 실행 후 Controller 객체는 HandlerAdapter 객체에 ModelAndView 객체를 반환한다.
  - ModelAndView 객체에는 사용자 응답에 필요한 데이터정보와 뷰정도(JSP파일)가 담겨있다.
  - HandlerAdapter 객체는 ModelAndView 객체를 다시 DispatcherServlet 객체에 반환한다.
- 데이터가 오면 ViewResolver를 이용해 적합한 View를 찾고 응답

### 4) `servlet-context.xml`
- 스프링 설정 파일
- `<resources mapping="/resources/**" location="/resources/" />`
  - mapping 속성 : 사용자의 요청 url
  - location 속성 : 파일 위치

### 5) Controller
```java
@Controller
public class HomeController {

    @RequestMapping(value="/", method=RequestMethod.GET)
    public String home(Locale locale, Model model) {

        DateFormat dateFormat = DateFormat.getDateTimeInstance(DateFormat.LONG, DateFormat.LONG, locale);

        String formattedDate = dateFormat.format(date);

        model.addAttirbute("serverTime", formattedDate);

        return "home";
    }
}
```
- `model.addAttribute` : jsp 문서에서 사용될 데이터 세팅