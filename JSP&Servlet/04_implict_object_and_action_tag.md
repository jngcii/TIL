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