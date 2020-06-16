# 자바빈 (JavaBean)

###### 2020.06.16

## I. 자바빈 개요

### 1) 사용 이유
- 디자인 부분과 비즈니스 로직 부분을 분리하기 위해서

### 2) 설계 규약
> 자바빈은 다른 클래스와는 달리 약속에 따라 작성해야 하며, 이에 맞지 않을 경우는 자바빈의 특성을 갖지 않는 클래스가 되버릴수 있다.
1. 멤버 변수마다 별도의 get/set 메서드가 존재해야한다.
2. get 메서드는 파라미터가 존재하지 않아야 한다.
3. set 메서드는 반드시 하나 이상의 파라미터가 존재해야 한다.
4. 빈즈 컴퍼넌트의 속성은 반드시 읽기 또는 쓰기가 가증해야 한다. 즉, get 메서드와 set 메서드를 구현해야 한다.
5. 생성자는 파라미터가 존재하지 않아야 한다. 인자 없는 생성자가 반드시 있어야 한다.
6. 멤버 변수의 접근 제어자는 private이며, 각 set/get 메서드의 접근 제어자는 public으로 정의되어야 하며 클래스의 접근자는 public으로 정의한다.

### 3) 기본 작성 예제
- `BeanTest.java`
  ```java
  package test;

  public class BeanTest {
    private String name="jngcii";

    public String getname() {
      return name;
    }

    public void setName(String name) {
      this.name = name;
    }
  }
  ```

- `beanTest.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>

  <jsp:useBean id="beantest" class="test.BeanTest" scope="page" />

  <html>
  <head>
  <title>JavaBean Test</title>
  </head>

  <body>
  <b>자바빈 사용 예제</b>
  <h3><%=beantest.getname() %></h3>
  </body>
  </html>
  ```

## II. JSP에서 자바빈 사용하기

### 1) `<jsp:useBean /> 태그`
```html
<jsp:useBean id="빈 이름" class="자바빈 클래스명" scope="사용 범위" />
```
- `id` : 페이지에서 사용될 자바빈의 변수명
- `class` : 자바빈의 설계 규약에 맞게 작성된 클래스명 (클래스가 패키지 안에 작성되었다면 패키지 경로까지 작성해야함)
- `scope` : 사용 범위
  - `request`
  - `page` (기본값)
  - `session`
  - `application`

### 2) `<jsp:setProperty /> 태그`
```html
<jsp:setProperty name="빈 이름" property="속성명" value="설정할 속성 값" />
```
- 자바빈 클래스의 속성 값을 설정하기 위한 태그이다.
- 예시
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>

  <jsp:useBean id="beantest" class="test.BeanTest" scope="page" />
  <jsp:setProperty name="beantest" property="name" value="BeanTest!" />

  <html>
  <head>
  <title>JavaBean Test</title>
  </head>

  <body>
  <b>자바빈 사용 예제</b>
  <h3><%=beantest.getname() %></h3>
  </body>
  </html>
  ```
  - `<jsp:setProperty />` 태그를 사용하여 BeanTest 자바빈에 접근하여 name 변수를 변경한 것
  - 자바빈의 name은 private로 선언되어있으므로 직접 변경할 수 없다. `<jsp:setProperty />` 태그는 자바빈 객체의 멤버 변수를 직접 수정하는 것이 아니라 set 메서드를 호출하여 멤버 변수를 수정하는 것이다.
- 클라이언트에서 전송되어 오는 파라미터 값을 속성 값으로 할당할 경우는 value 대신 param을 사용한다.
  - `<jsp:setProperty name="빈 이름" property="속성명" param="파라미터명" />`
  - 파라미터의 이름이 설정하려는 빈 객체의 속성명과 같으면 param 속성은 생략해도 된다.
- 클라이언트에서 전송되어오는 파라미터 이름이 빈 객체의 속성명과 모두 같다면 다음과 같이 한 번에 할당할 속성명을 할당할 수 있다.
  - `<jsp:setProperty name="빈 이름" property="*" />`

### 3) `<jsp:getProperty /> 태그`
```html
<jsp:getProperty name="빈 이름" property="속성명" />
```
- 자바빈 클래스의 속성 값을 가져오기 위한 태그

### 4) 자바빈의 영역
- `<jsp:useBean />` 태그의 scope 속성
- 자바빈 객체가 저장될 영역
  |영역 | 설명 |
  |--- | --- |
  | page | 빈 객체 공유 범위가 현재 페이지의 범위에만 한정된다. 페이지가 변경되면 공유가 유지되지 않는다. |
  | request | request 요청을 받고 처리를 완료할 때까지 생존되는 scope이다. |
  | session | 클라이언트당 하나씩 할당되는 영역이다. 클라이언트가 브라우저를 종료하기 전까지 유지되는 scope이다. |
  | application | 사이트 전체의 범위를 가지며, 서버가 종료되기 전에는 계속 유지되는 scope이다. |
- 일반적으로 request 영역은 모델2로 요청 처리를 할 때 서블릿에서 데이터를 공유하고 jsp 페이지에서 공유된 데이터를 사용할 때 많이 사용된다.
- 세션 영역은 요청이 바뀌어도 정보가 유지되어야 하는 경우, 즉 로그인이나 장바구니 등에 많이 사용된다.
- 애플리케이션 영역은 애플리케이션 전체 영역에서 데이터를 공유해야 하는 경우 (전체 방문자 수 계산) 등에 많이 사용한다.
- 개발하고 있는 프로그램의 기능을 고려하여 적절한 영역을 사용해야 메모리의 낭비를 줄일 수 있다.