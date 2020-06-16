# JSP 기본 요소

###### 2020.06.15

## I. JSP 주석

### 1) HTML 주석
```html
<!-- HTML 주석입니다. -->
```

### 2) JSP 주석
```html
<%-- JSP 주석입니다. %-->
```

### 3) 자바 스타일 주석
```html
<%
/* 여러 줄을 사용할 때의
자바 주석입니다. */
%>

<%
// 한 줄을 사용할 때의 자바 주석입니다.
%>
```

## II. JSP 지시어 (Directive)
```html
<%@ ... %>
```
- JSP 디렉티브는 위와 같은 형식으로 표현되면 JSP 파일 내에서 JSP를 실행할 컨테이너에서 해당 페이지를 어떻게 처리할 것인가에 대한 설정 정보들을 지정해주는데 사용된다.
- 지시어는 page 지시어, include 지시어, taglib 지시어 3가지로 구분된다.

### 1) page 지시어
> JSP 페이지에 대한 속성을 지정하는 지시어
```html
<%@ page 속성1="값1" 속성2="값2" 속성3="값3"... %>
```
- 각각의 속성을 하나의 page 디렉티브에 한번에 지정할 수도 있으며, 여러 개의 page 지시어에 나누어 지정할 수도 있다.
- import 속성을 제외한 나머지 속성은 하나의 페이지에서 오직 한 번씩만 지정할 수 있다.
- 속성에는 다음과 같은 12개의 설정 정보를 지정할 수 있다.
  |속성 | 사용법 | 기본값 | 설명 |
  |---|---|---|---|
  |language|language="java" | java | 스크립트 요소에서 사용할 언어 설정 |
  |extends | extends="클래스명" | 없음 | 상속받을 클래스를 결정 |
  |import | import="패키지.클래스명" | 없음 | 가져올 패키지. 클래스 설정 |
  |session | session="true" | true | HttpSession 사용 여부 |
  |buffer | buffer="16kb" | 8kb | JSP 페이지의 출력 버퍼 크리 설정 |
  |autoFlush | autoFlush="true" | true | 출력 버퍼가 다 찼을경우 처리 방법을 설정 |
  |isThreadSafe | isThreadSafe="true" | true | 다중 스레드의 동시 실행 여부를 설정 |
  |info | info="페이지 설명" | 없음 | 페이지 설명 |
  |errorPage | errorPage="에러페이지.jsp" | 없음 | 에러 페이지로 사용할 페이지를 지정 |
  |contentType | contentType="text/html" | text/html;charset=ISO-8859-1 | JSP 페이지가 생성할 문서의 타입을 지정 |
  |isErrorPage | isErrorPage="false" | false | 현재 페이지를 에러 페이지로 지정 |
  |pageEncoding | pageEncoding="euc-kr" | ISO-8859-1 | 현재 페이지의 문자 인코딩 타입 설정 |


### 2) include 지시어
> JSP 파일 또는 HTML 파일을 해당 JSP 페이지에 삽입할 수 있도록 하는 기능을 제공하는 지시어
```html
<%@ include file="header.jsp" %>
```

### 3) taglib 지시어
> JSTL(JSP Standard Tag Library)이나 커스텀 태그 등 태그 라이브러리를 JSP에서 사용할 때 접두사를 지정하기 위해 사용된다.
```html
<%@ taglib uri="http://taglib.com/sampleURI" prefix="samplePrefix" %>
```
```html
<samplePrefix: table col="2" row="2" border="1">
태그 라이브러리를 이용한 테이블입니다.
</samplePrefix>
```
- taglib 지시어는 uri 속성과 prefix 속성의 두 가지 속성으로 이루어지는데 uri 속성은 태그 라이브러리에서 정의한 태그와 속성 정보를 저장한 TLD 파일이 존재하는 위치를 지정하고, prefix 속성에는 사용할 커스텀 태그의 네임 스페이스를 지정한다.


## III. JSP 스크립트 요소
- JSP 스크립트 요소는 JSP 페이지 내에 자바의 코드를 삽입하기 위해 사용되며 선언문, 스크립틀릿, 표현식의 3가지로 구분된다.

### 1) 선언문
```html
<%!... %>
```
- JSP 페이지에서 자바 코드에서 말하는 멤버 변수와 메서드를 선언하기 위해 사용된다.
- 선언문을 사용해 선언된 변수는 JSP 파일이 웹 컨테이너에 의해 컴파일 될 때 멤버 변수로 인식되기 때문에 JSP 페이지의 어느 위치에서도 해당 변수를 참조하는 것이 가능하다.
- 예시
  ```html
  <%!
  private String str="JSP study";
  public String checkStr() {
    if(str == null) return "no";
    else return "ok";
  }
  %>
  ```

### 2) 스크립틀릿
```html
<% 문장1; %>
<%
문장2; 문장3; 문장4;
%>
```
- HTML 코드로 된 부분은 일반 HTML 파일처럼 그대로 사용하고 자바 코드로 이루어진 비즈니스 로직 부분은 <% ... %>로 표현되는 스크립틀릿 태그를 사용하여 구분함으로써 out 객체를 사용하지 않고도 쉽게 HTML 응답을 만들어 낼 수 있다.
- JSP 파일이 실행되면 웹 컨테이너에 의해 JSP 파일이 파싱되어 서블릿 클래스로 변경된 자바 소스 파일과 클래스 파일이 서버에 저장된다.
- JSP 파일이 서블릿 클래스로 변환되면 그 소스 파일과 클래스 파일의 이름은 각각 "JSP 파일명_jsp.java"와 "JSP 파일명_jsp.class"가 된다.

### 3) 표현식
```html
<%=변수 %>
<%=리턴값이 있는 메서드 %>
<%=수식(변수 또는 리턴값이 있는 메서드를 포함할 수 있음) %>
```
- 표현식은 선언문 또는 스크립틀릿 태그에서 선언된 변수 값이나 메서드의 리턴값을 스크립틀릿 태그 외부에서 출력하기 위해서 사용되는 방법이다.
- 표현식 태그 내 구문 전체의 결과 값은 JSP 파일이 파싱될 때 출력 객체의 print() 메서드를 통해 자동으로 문자열 형식으로 변환되어 출력된다.
- 하나의 표현식 태그 내의 구문 전체가 하나의 print() 메서드의 괄호 안에 통째로 들어가게 되므로 표현식 태그 내부에서는 `;`를 사용하면 안된다.