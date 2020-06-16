# 내장 객체와 액션 태그

###### 2020.06.15

## I. 내장 객체
- JSP 페이지는 웹 컨테이너에 의해 서블릿 클래스로 변환되어 사용자의 요청을 수행한다.
- 이 서블릿 클래스가 인스턴스로 생성되고 사용자의 요청에 맞는 응답 페이지를 생성하기 위해서는 기본적으로 javax.servlet 패키지 아래 몇 가지의 객체가 필수적으로 사용된다.
- 웹 컨테이너가 제공하는 여러 기능을 하는 고정된 이름의 객체를 JSP 내장 객체라고 부르며 JSP를 지원하는 웹 컨테이너에서는 서블릿을 구현하는데 공통적으로 요구되는 javax.servlet 패키지 아래 8개 객체와 예외처리를 위한 java.lang 패키지 아래 1개의 객체를 각각 JSP 스펙에서 정해진 이름의 객체로 제공한다.

### 1) request 객체
- 사용자는 브라우저를 통해 요청을 HTTP 메세지로 구성해 서버에 전송한다.
- JSP/서블릿 컨테이너는 전송받은 HTTP 메세지를 통해 HTTPServletRequest 객체를 생성하고 이를 서블릿 인스턴스에 넘겨줌으로써 서블릿이 사용자의 요청에 관련된 데이터들을 얻게된다.
- JSP 페이지에서는 HttpServletRequest 객체를 request란 이름의 객체로 사용한다.
- 요청파라미터 관련 주요 메서드
  | 리턴 타입 | 메서드명 | 설명 |
  | --- | --- | --- |
  |String | getParameter(String name) | name이란 이름으로 지정된 파라미터에 할당된 값을 리턴한다. 지정된 이름의 파라미터가 없으면 null을 리턴한다. |
  |String[] | getParameterValues(String name) | name이란 이름으로 지정된 파라미터의 모든 값을 String 배열로 리턴한다. |
  |Enumeration | getParameterNames() | 요청에 포함된 모든 파라미터 이름을 java.util.Enumeration 객체로 리턴한다. |
- HTTP 헤더 정보와 관련된 메서드
  | 리턴 타입 | 메서드명 | 설명 |
  | --- | --- | --- |
  |String | getHeader(String headerName) | HTTP 요청 헤더에 headerName으로 할당된 값을 리턴한다. |
  |Enumeration | getHeaders(String headerName) | headerName으로 할당된 모든 값을 java.util.Enumeration 객체로 리턴한다. |
  |Enumeration | getHeadersNames() | HTTP 요청 헤더에 포함된 모든 헤더 이름을 java.uril.Enumeration 객체로 리턴한다. |
  |int | getIntHeader(String headerName) |headerName에 할당된 값을 int 타입으로 리턴한다. 변환할수 없으면 NumberFormatException을, header가 없을 경우엔 -1을 리턴한다.|
- 세션 정보와 관련된 메서드들
  | 리턴 타입 | 메서드명 | 설명 |
  | --- | --- | --- |
  |HttpSession | getSession() | 요청한 클라이언트에 할당된 HttpSession 객체를 반환한다. 이전에 생성된 HttpSession 객체가 없으면 새로운 객체를 생성해 할당한다. |
  |HttpSession | getSession(Boolean create) | create가 true일 경우 getSesison() 메서드와 동일한 결과를 리턴하지만, false일 경우에는 이전에 생성된 HttpSession 객체가 없을 경우 null을 리턴한다.
  |String | getRequestSessionId() | 요청한 클라이언트에 지정된 세션의 ID를 문자열로 리턴한다. |
  |boolean | isRequestedSessionIdValid() | 요청에 포함된 클라이언트의 세션ID가 유효하다면 true를, 아니면 false를 리턴한다.|
- 쿠키, URL/URI, 요청 방식과 관련된 메서드들
  |리턴 타입 | 메서드명 | 설명 |
  | --- | --- | --- |
  |Cookie[] | getCookies() | HTTP 요청 메세지의 헤더에 포함된 쿠키를 javax.servlet.http.Cookie 배열로 리턴한다. |
  |String | getServerName() | 서버의 도메인명을 문자열로 리턴한다. |
  |int | getServerPort() | 서버의 포트 번호를 int형으로 리턴한다. |
  |StringBuffer | getRequestURL() | 요청 URL을 StringBuffer로 리턴한다. |
  |String | getRequestURI() | 요청 URI를 문자열로 리턴한다. |
  |String | getQueryString() | 요청에 사용된 쿼리 문장을 문자열로 리턴한다. |
  |String | getRemoteHost() | 클라이언트의 호스트 이름을 문자열로 리턴한다. |
  |String | getRemoteAddr() | 클라이언트의 IP 주소를 문자열로 리턴한다. |
  |String | getProtocol() | 요청에 사용된 프로토콜 이름을 문자열로 리턴한다. |
  |String | getMethod() | 요청에 사용된 요청 방식을 문자열로 리턴한다. |
  |String | getContextPath() | 해당 JSP 페이지의 컨텍스트 경로를 문자열로 리턴한다. |

### 2) response 객체
- 클라이언트의 요청에 대한 HTTP 응답을 나타내는 객체
- 웹컨테이너에서는 javax.servlet.http.HttpServletResponse 인터페이스를 사용해 response 객체를 생성한다.
- response 객체의 주요 메서드
  | 리턴 타입 | 메서드명 | 설명 |
  | --- | --- | --- |
  |없음 | setHeader(String headerName, String headerValue) | 응답에 포함될 헤더 정보에 headerName의 이름으로 headerValue 값을 설정해 추가한다. |
  |없음 | addCookie(Cookie cookie) | javax.servlet.http.Cookie 타입의 쿠기 객체를 응답 헤더에 추가한다. 쿠키에 대해서는 Chapter 8에서 자세히 다룬다. |
  |없음 | sendRedirect(String url) | 지정된 URL로 요청을 재전송한다. |
  |없음 | setContentType(String type) | 응답 페이지의 contentType을 설정한다. |

### 3) pageContext 객체
- JSP 페이지와 관련된 프고르램에서 다른 내장 객체를 얻어내거나 현재 페이지의 요청과 응답의 제어권을 다른 페이지로 넘겨주는데 사용한다.
- 내장 속성을 제어하는 기능을 한다.
  | 리턴 타입 | 메서드명 | 설명 |
  | --- | --- | --- |
  |ServletRequest|getRequest()|클라이언트의 요청 정보를 담고 있는 객체를 리턴한다. |
  |ServletResponse | getResponse()| 요청에 대한 응답 객체를 리턴한다. |
  |JspWriter | getOut() | 응답 출력 스트림을 리턴한다. |
  |Object | getPage() | 서블릿 인스턴스 객체를 리턴한다. |
  |ServletConfig | getServletConfig() | 서블릿 초기 설정 정보를 담고 있는 객체를 리턴한다. | 

### 4) 기타 객체
- session 객체
- application 객체
- out 객체
- config 객체
- page 객체
- exception 객체


## II. 영역 객체와 속성

### 1) Scope(영역객체)와 Attribute(속성)
- JSP에서 제공하는 내장 객체들 중 session, request, application 객체들은 해당 객체에 정의된 유효 범위 안에서 필요한 객체들을 저장하고 읽어들임으로써 서로 공유할 수 있는 특정한 영역을 가지고 있다.
- Attribute : 공유되는 데이터
- Scope : 속성을 공유할 수 있는 유효 범위
- session 내장 객체는 세션이 유지되고 있는 범위 안에서 서로 다른 페이지라 할지라도 객체들을 공유할 수 있는 속성을 가질 수 있고 이 속성에 저장된 객체는 세션이 종료되는 순간에 반환된다(버려진다).
- request 객체는 클라이언트의 요청이 처리되는 동안에 속성을 사용할 수 있다.
- application 객체는 해당 웹 애플리케이션이 실행되는 동안 속성을 사용할 수 있다.
- 예외 : page 영역 객체는 오직 하나의 페이지 내에서만 유효성을 갖는 영역으로 주의해야 할 점은 page 내장 객체가 아닌 pageContext 내장 객체를 통해 접근할수 있는 영역이라는 점이다.

### 2) 속성과 관련된 메서드들
|리턴 타입 | 메서드명 | 해설 |
|--- | --- | --- |
|Object | getAttribute(String key) | key 값으로 등록되어 있는 속성을 Object 타입으로 리턴 |
|Enumeration |getAttributeNames | 해당 영역에 등록되어 있는 모든 속성들의 이름을 Enumeration 타입으로 리턴 |
|없음 | setAttribute(String key, Object obj) | 해당 영역에 key 값의 이름으로 obj 객체를 등록 |
|없음 |removeAttribute(String key) | key 값으로 등록되어 있는 속성을 제거 |

#### 예시
- `attributeTest1_Form.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
  <html>
  <head>
  <title>Attribute Test Form</title>
  </head>

  <body>
  <h2>영역과 속성 테스트</h2>
  <form action="attributeText1.jsp" method="post">
    <table border="1">
      <tr><td colspan="2">Application 영역에 저장할 내용들</td></tr>
      <tr>
        <td>이름</td>
        <td><input type="text" name="name"></td>
      </tr>
      <tr>
        <td>아이디</td>
        <td><input type="text" name="id"></td>
      </tr>
      <tr>
        <td colspan="2"><input type="submit" value="전송"></td>
      </tr>
    </table>
  </form>
  </body>
  </html>
  ```
- `attributeTest1.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
  <html>
  <head>
  <title>Attribute Test</title>
  </head>

  <body>
  <h2>영역과 속성 테스트</h2>
  <%
  request.setCharacterEncoding("UTF-8");
  String name=request.getParameter("name");
  String id=request.getParameter("id");
  if(name!=null&&id!=null) {
    application.setAttribute("name", name);
    application.setAttribute("id", id);
  }
  %>
  <h3><%=name %>님 반갑습니다.</br><%=name %>님의 아이디는 <%=id %>입니다.</h3>
  <form action="attributeTest2.jsp" method="post">
  <table border="1">
    <tr><td colspan="2">Session 영역에 저장할 내용들</td></tr>
    <tr>
      <td>e-mail 주소</td>
      <td><input type="text" name="email"></td>
    </tr>
    <tr>
      <td>집 주소</td>
      <td><input type="text" name="address"></td>
    </tr>
    <tr>
      <td>전화번호</td>
      <td><input type="text" name="tel"></td>
    </tr>
    <tr>
      <td colspan="2"><input type="submit" value="전송"></td>
    </tr>
  </table>
  </form>
  </body>
  </html>
  ```
  > `application.setAttribute()` : 이름과 아이디 값을 애플리케이션 영역에 속성으로 공유하는 부분

- `attributeTest2.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
  <html>
  <head>
  <title>Attribute Test</title>
  </head>

  <body>
  <h2>영역과 속성 테스트</h2>
  <%
  request.setCharacterEncoding("UTF-8");
  String email = request.getParameter("email");
  String address = request.getParameter("address");
  String tel = request.getParameter("tel");
  session.setAttribute("email", email);
  session.setAttribute("address", address);
  session.setAttribute("tel", tel);

  String name=(String)application.getAttribute("name");
  %>
  <h3><%=name %>님의 정보가 모두 저장되었습니다.</h3>
  </body>
  </html>
  ```
  > `session.setAttribute()` : email, address, tel 값을 session 영역에 속성으로 공유한다.


## III. 액션 태그
- JSP 페이지에서 자바 코드 등의 스크립트 언어를 사용하지 않고도 다른 페이지의 서블릿이나 자바빈의 객체에 접근할 수 있도록 태그를 이용해 구현된 기능
- 기능
  - 페이지의 흐름을 제어
  - 자바빈의 속성 읽고 쓰기
  - 애플릿을 사용
- 액션태그 종류
  - 페이지 흐름 제어 액션 (forward/include 액션)
  - 자바빈 사용 액션 (useBean 액션)
  - 애플릿 사용 액션 (plugin 액션) ; 사용빈도가 현저히 줄어든 추세

### 1) forward 액션
```html
<jsp:forward page="이동할 페이지" />
```
- 액션 태그는 XML 문법을 이용하여 구현된 기능이므로 위에서 보여지듯이 태그의 끝에 종료 태그가 반드시 있어야 한다.
- 내장 객체 중 pageContext 객체의 forward() 메서드가 태그로 구현된 기능
- 따라서 forward 액션은 현재 페이지의 요청과 응답에 관한 처리권을 page 속성에 지정된 이동할 페이지로 영구적으로 넘기는 기능을 한다.
- 이 때 이동하기 전의 페이지에 대한 모든 출력 버퍼의 내용은 무시(버퍼의 내용이 버려짐)되며 이동한 페이지가 요청을 처리하여 응답이 완료되면 원래 페이지로 제어권이 돌아가지 않고 그 상태에서 모든 응답이 종료된다.
- 아래와 같이 변수를 사용할 수 도 있다.
  ```html
  <jsp:forward page='<%=nextPage %>' />
  ```
- forward 태그를 사용하여 이동할 페이지에 추가적으로 파라미터를 넘겨줄 필요가 있을 때에는 다음처럼 forward 태그의 하위 태그인 `<jsp:param />` 태그를 사용할 수 있다.
  ```html
  <jsp:forward page="이동할 페이지">
    <jsp:param name="파라미트 이름1" value="파라미터 값1" />
    <jsp:param name="파라미트 이름2" value="파라미터 값2" />
  </jsp:forward>
  ```
- 혹은 query parameter러 전송할 수 도 있다.
  ```html
  <jsp:forward page="forward.jsp?id=jngcii&password=abc" />
  ```

### 2) include 액션
```html
<jsp:include page="포함될 페이지" flush="false" />
```
- include 액션은 임시로 제어권을 include되는 페이지로 넘겼다가 그 페이지의 처리가 끝나면 처리 결과를 원래 페이지로 되돌리고 다시 원래의 페이지로 제어권을 반환하는 방식이다.
- include 지시어의 경우네는 컨테이너의 버전에 따라서 원래 페이지의 서블릿이 생성된 이후에 include되는 페이지가 변동되었을 경우 그 변동을 원래 페이지가 반영하지 못하는 경우도 있다. 따라서 include 지시어는 일반적으로 정적인 코드를 포함시킬 때 주로 사용하고 include 액션은 JSP 페이지처럼 동적인 페이지를 포함시키고자 할 때 주로 사용된다.

### 3) XMLElement를 생성하는 액션 태그들
- jsp에서 제공하는 XML 엘리먼트 관련 액션 태그들은 jsp 내에 XML 관련 엘리먼트들을 동적으로 생성하는 역할을 한다.
- `<jsp:element>`
  ```html
  <jsp:element name="elementName"></jsp:element>
  ```
  > xml 엘리먼트를 정의하는 액션 테그
- `<jsp:attribute>`
  ```html
  <jsp:attribute name="attributeName">
  attributeValue
  </jsp:attribute>
  ```
  > 엘리먼트의 속성을 정의하는 액션 태그
- `<jsp:body>`
  ```html
  <jsp:body>XML 엘리먼트의 내용</jsp:body>
  ```
  > 엘리먼트의 내용을 지정
