# 예외처리

###### 2020.06.16

## I. page 지시자의 errorPage 속성 사용
```html
<%@ page errorPage="errorProcessing.jsp" @>
```
- JSP 페이지에서 에러를 처리하는 페이지를 지정하는 가장 간단한 방법은 page 지시자에서 errorPage를 지정하는 방법이다.

### 1) `NullPointException` 발생 에러 페이지
- `createError.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
  <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
  <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Insert title here</title>
  </head>

  <body>
  <%
    String name = request.getParameter("name");
    if(name == null) {
        throw new NullPointerException();
    }
  %>
  </body>
  </html>
  ```

### 2) 위의 형태로 표시되지 않고 원하는 형태의 에러 페이지로 출력하려면 page 액션태그 부분을 바꿔주면된다.
- `createError.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" errorPage="errorProcessing.jsp" %>
  ```

### 3) errorProcessing.jsp 페이지 코드 작성
- `errorProcessing.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" isErrorPage="true" %>
  <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
  <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Insert title here</title>
  </head>

  <body>
  발생한 예외 종류 : <%=exception.getClass().getName() %>
  <!--
      사용 브라우저가 IE일 경우는 에러 페이지 크기가 513바이트 이상 되어야 인식된다. 513 바이트 이상을 주석으로 만들어주자.
      사용 브라우저가 IE일 경우는 에러 페이지 크기가 513바이트 이상 되어야 인식된다. 513 바이트 이상을 주석으로 만들어주자.
      사용 브라우저가 IE일 경우는 에러 페이지 크기가 513바이트 이상 되어야 인식된다. 513 바이트 이상을 주석으로 만들어주자.
      사용 브라우저가 IE일 경우는 에러 페이지 크기가 513바이트 이상 되어야 인식된다. 513 바이트 이상을 주석으로 만들어주자.
      사용 브라우저가 IE일 경우는 에러 페이지 크기가 513바이트 이상 되어야 인식된다. 513 바이트 이상을 주석으로 만들어주자.
  -->
  </body>
  </html>
  ```

## II. web.xml에서 error-code 엘리먼트 값 설정
```xml
<error-page>
    <error-code>500</error-code>
    <location>/500.jsp</location>
</error-page>
```

## III. web.xml에서 exception-type 엘리먼트 값 설정
```xml
<error-page>
    <error-code>500</error-code>
    <location>/500.jsp</location>
</error-page>
<error-page>
    <exception-type>java.lang.NullPointerException</exception-type>
    <location>/null.jsp</location>
</error-page>
```