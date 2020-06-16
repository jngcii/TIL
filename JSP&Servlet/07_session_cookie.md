# 세션과 쿠기

###### 2020.06.16

## I. 세션

- 세션이란 서버 측의 컨테이너에서 관리되는 정보이다.
- 세션의 정보는 컨테이너에 접속해서 종료되기까지 유지되며, 만료시간을 둘 수 있다.

### 1) HTTP 프로토콜의 특성
- HTTP 프로토콜은 데이터를 요청하고 데이터의 결과 값을 받게 되면 바로 연결은 종료된다.

### 2) 세션이이란
- 세션은 클라이언트와 서버 간의 접속을 유지시켜주는 역할을 한다.
- 서버에서 클라이언트를 구분할 수 있는 식별자라고 생각하면 된다.

### 3) JSP에서의 세션 관리
| 메서드 | 설명 |
| --- | --- |
|setAttribute(String attrName, Object attrValue) | 세션 영역에 속성을 생성한다. |
|removeAttribute(String attrName) | 파라미터로 지정된 이름의 속성을 제거한다. |
| getAttribute(String attrName) | 지정된 이름의 속성 값을 반환한다. |
| getId() | 클라이언트의 세션 ID 값을 반환한다. |
| setMaxInactiveInterval(int seconds) | 세션의 유지 기간을 설정한다. |
| getMaxInactiveInterval() | 세션의 유지 시간을 반환한다. |
| invalidate() | 현재의 세션 정보들을 모두 제거한다. |

#### 주의 (`getAttribute("세션명")` 사용법)
```java
String name = (String)session.getAttribute("name");
```

## II. 쿠키

- 쿠키란 클라이언트측에서 관리되는 정보를 의미한다.
- 세션은 서버측에서 관리되고, 쿠키는 클라이언트에서 관리된다.
- 쿠키의 정보는 브라우저를 종료한다고 해도 생존 기간이 지정되면 생존 기간동안 데이터가 사라지지 않는다.

### 1) HTTP 헤더를 이용한 쿠키 설정
- 쿠키를 설정하는 방법에는 HTTP 헤더를 이용한 쿠키 설정 방법과 서블릿 API를 이용한 쿠키 설정 방법 이렇게 두가지가 있다.

### 2) HTTP 헤더를 통한 쿠키 설정
- `Set-Cookie: name=value; expires=date; domain=domain; path=path; secure`
- 필수로 요구되는 속성은 name, value

### 3) 서블릿 API를 이용한 쿠키 설정
```java
Cookie cookie = new Cookie(name, value);

// cookie 에서 사용되는 메서드
cookie.setValue("jngcii");  // 쿠키 값을 설정한다.
cookie.setMaxAge(3600);     // 쿠키 만료 기간을 초단위로 지정한다.
cookie.getValue();          // 쿠키 값을 얻어온다.
cookie.getMaxAge();         // 쿠키 만료 기간을 얻어온다.
cookie.getName();           // 쿠키 이름으 얻어온다.

response.addCookie(cookie);
```

