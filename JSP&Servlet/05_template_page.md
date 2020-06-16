# 액션 태그를 활용한 템플릿 페이지 작성

###### 2020.06.16

## I. 템플릿 페이지
- 대부분의 웹사이트 화면 구성은 비슷하다.
- 미리 정의되어있는 템플릿 페이지를 사용하고 필요한부분만 수정하면 매우 편하다.
- JSP의 모듈화

### 1) 템플릿 페이지의 설계
- 템플릿 페이지의 설계에서 중요한 것은 레이아웃 구조를 결정하는 것이다.
- 템플렛 페이지 설계를 위해서는 사이트의 화면의 틀이 결정되어야 한다.

### 2) 액션 태그를 이용한 템플릿 페이지의 작성
|파일 이름 | 설명 |
| --- | --- |
|top.jsp |화명 상단에 표시될 네비게이션 파일|
|bottom.jsp | 화면 하단에 표실될 파일 |
|left.jsp | 화면 좌측에 표시될 메뉴 파일 |
|newItem.jsp | 신상품 페이지 파일 |
|bestItem.jsp | 인기상품 파일 |
|template.jsp | 템플릿 페이지 파일 |

## II. 각 페이지 작성

### `top.jsp`
```html
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" @>

<a href="login.jsp">Login</a>
<a href="join.jsp">Join</a>
```

### `bottom.jsp`
```html
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" @>

<center>Since 2020</center>
```

### `left.jsp`
```html
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" @>

<center>
  <a herf="./template.jsp?page=newitem">신상품</a><br><br>
  <a herf="./template.jsp?page=bestitem">인기상품</a><br><br>
</center>
```

### `newitem.jsp`
```html
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" @>

<b>신상품 목록입니다.</b>
```

### `bestitem.jsp`
```html
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" @>

<b>인기상품 목록입니다.</b>
```

## III. 템플릿 페이지 작성

### `template.jsp`
```html
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" @>
<%
  String pagefile = request.getParameter("page");
  if (pagefile==null) { pagefile="newitem"; }
%>

<html>
<head>
<title>Template Test</title>
<style>
  table {
    margin: auto;
    width: 960px;
    color: gray;
    border: 1px solid gray;
  }
</style>
</head>

<body>
<table>
  <tr>
    <td height="43" colspan=3 align=left>
      <jsp:include page="top.jsp" />
    </td>
  </tr>
  <tr>
    <td width="15%" align=right valign=top><br>
      <jsp:include page="left.jsp" />
    </td>
    <td colspan=2 align=center>
      <jsp:include page='<%=pagefile+".jsp" %>' />
    </td>
  </tr>
  <tr>
    <td width="100%" height="40" colspan="3">
      <jsp:include page="bottom.jsp" />
    </td>
  </tr>
</table>
</body>
</html>
```