# 서블릿의 핵심 사항들

###### 2020.06.13

## I. 서블릿의 라이프사이클
- 서블릿은 클라이언트의 첫 번째 요청이 들어오거나 컨테이너가 시작될 때 생성된다.
- 서블릿 객체가 컨테이너가 시작될 때 생성되게 할 지, 클라이언트의 첫 번째 요청이 들어올 때 생성되게 할 지는 컨테이너 속성 값으로 설정할 수 있다.
- 첫 번째 클라이언트의 요청에 대해서만 객체가 생성되고 두 번째 요청부터는 각 클라이언트마다 스레드를 생성하여 요청을 처리한다.
- 그리고 컨테이너가 종료될 때 서블릿 객체는 소멸된다.
- 클라이언트의 첫 번째 요청이 들어오면 서블릿 객체가 생성되고 init 메서드가 호출되며 서블릿에 필요한 초기화 작업을 수행한다.
- init 메서드 안에서는 주로 서블릿 전체에서 공유되는 자원을 생성한다.
- init 메서드는 첫 번째 클라이언트의 요청이 들어올 때만 서블릿 생애 주기 중 단 한번만 호출된다.
- 두 번째 요청부터는 service 메소드가 반복적으로 호출되면서 요청을 처리한다. 즉, 요청 하나당 service 메서드가 한번 호출된다.
- service 메서드는 doGet() 메서드 혹은 doPost() 메서드를 실행한다.
- 즉, 매 요청마다 service() 메서드와 doGet() 혹은 doPost() 메서드가 실행된다.
- doGet()이나 doPost() 메서드 호출시 인자로 HttpServletRequest 객체와 HttpServletResponse 객체를 전달한다.
- 일반적으로 개발 시 service() 메서드는 재정의하지 않고, doGet()이나 doPost() 메서드를 재정의하여 클라이언트의 요청을 처리한다.


## II. 서블릿을 이용한 클라이언트에서 전송되는 요청 처리

### 1)  웹 프로젝트 생성
1. Project Explorer 탭에서 Dynamic Web Project 생성
2. Project name - Chapter3
3. next
4. Generate web.xml deployment descriptor 체크 후 완료
5. WebContent 디렉터리에 login.html 파일 생성 후 로그인 폼 만들기

### 2) 서블릿 생성하기
1. [New] - [Servlet] 클릭
2. ClassName에 LoginServlet 입력 후 Next
    - 이 부분은 실질적으로 생성되는 자바 파일명을 지정하는 부분으로 web.xml 설정에서 `<servlet-class>` 항목에 설정되는 값이다.
3. 다음 화면에서 URL mappings 항목을 선택하고 `/login`으로 바꿔주고 Next
     - 클라이언트 폼 태그 요청 경로가 `<form action="login">` 으로 설정되어 있었으므로 `/login` 사용
     - 이 부분은 web.xml 설정 파일에서 `<url-pattern>` 항목의 내용으로 추가되는 부분이다. 
4. 현재 예제는 GET 방식으로 요청하고 있으므로 doGet 메서드만 체크된 상태로 완료
5. 그럼 다음과 같은 페이지 생성됨
    ```java
    import java.io.IOException;
    import javax.servlet.ServletException;
    import javax.servlet.annotation.WebServlet;
    import javax.servlet.http.HttpServlet;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;

    /**
    * Servlet implementation class LoginServlet
    */
    @WebServlet("/login")
    public class LoginServlet extends HttpServlet {
        private static final long serialVersionUID = 1L;
        
        /**
        * @see HttpServlet#HttpServlet()
        */
        public LoginServlet() {
            super();
            // TODO Auto-generated constructor stub
        }

        /**
        * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
        */
        protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
            // TODO Auto-generated method stub
            response.getWriter().append("Served at: ").append(request.getContextPath());
        }

    }
    ```
    - 위의 출력 결과를 보면 doGet() 메서드가 자동을 생성되었고
    - web.xml 보다는 어노테이션 기반을 우선으로 제공하고 있다.
    - 어노테이션 : 기존 설정 파일(web.xml)에서 제공하는 설정 내용들을 설정 팡리에서 설정하지 않아도 해당 소스 내에 설정할 수 있는 방법을 제공하므로써 설정 파일의 크기를 줄이거나 설정 파일 자체를 없앨 수 있는 역할을 하는 기능
    - 즉, `http://localhost:8088/Chapter3/login`으로 요청이 전송되어 오면 해당 서블릿 클래스에서 요청을 처리하겠다는 의미이다. (url-pattern과 비슷한 역할이다.)
6. 이제 소스 코드를 작성한다.
    ```java
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String id = request.getParameter("id");
		String passwd = request.getParameter("passwd");
		response.setContentType("text/html;charset=euc-kr");
		PrintWriter out = response.getWriter();
		out.println("아이디="+id +"<br>");
		out.println("비밀번호="+passwd+"<br>");
	}
    ```
    - 바로 `http://localhost:8088/Chapter3/login`으로 접속하면 아무 파라미터가 전달되지 않았기 때문에 null을 출력한다.

## II. 서블릿에서 한글 처리하기

> 기본적으로 한글 처리가 제대로 되기 위해서는 클라이언트(브라우저)에서 문자를 처리하는 방식과 서버에서 문자를 처리하는 방식이 같아야 한다. 또한 톰캣 서버에서 사용하는 캐릭터셋은 UTF-8 방식이므로 한글이 제대로 인식되려면 다음 방법을 사용해 캐릭터셋을 변경해주어야 한다.

### 1) GET 방식으로 요청이 올 경우
- 링크가 걸려서 요청 처리가 되는 경우 form 태그의 method 속성이 GET 방식인 경우에는 페이지에서 사용하고 있는 캐릭터셋으로 인코딩되어 파라미터가 전송된다.
- 이클립스를 이용해서 html 페이지나 jsp 페이지를 생성할 때 이클립스에 지정된 기본 인코딩 방식이 euc-kr 방식이므로 한글이 제대로 인식이 되도록 하려면 이클립스에서 html 페이지와 jsp 페이지의 인코딩 방식을 UTF-8로 지정하고 작업하는 것이 편리하다.

1. 이클립스에서 [Window]-[Preferences] 클릭
2. Preferences 대화 상자에서 [Web]-[CSS Files] 메뉴 선택
3. 다음화면에서 CSS Files의 Encoding을 ISO10646/Unicode(UTF-8)로 선택 후 적용
4. HTML Files, JSP Files 메뉴에 각각 적용
5. html 파일에서 `<meta charset="UTF-8">`로 수정 및 doGet() 메서드에서도 `response.setContentType("text/html;charset=UTF-8");`로 수정

### 2) POST 방식으로 요청이 올 경우
- GET 방식과 흡사하지만 request 객체를 인코딩 처리를 해줘야한다.
- request 객체를 사용하기 전에 `request.setCharacterEncoding("UTF-8");`로 인코딩을 해줘야 한다.


## III. 하나의 파라미터 이름으로 여러 개의 파라미터 값이 전송되어 올 경우
- HttpServletRequest 인터페이스에서 제공되는 `String[] getParameterValues(String paramName)` 메서드를 사용해 처리해야 한다.
    ```java
    // ...

    String[] dog = request.getParameterValues("dog");

    for(int i=0; i<dog.length; i++) {
        out.println("<td>");
        out.println("<imgsrc='"+dog[i]+"'/>");
        // ...
    }
    
    // ...
    ```

## IV. 서블릿에서 세션 살펴보기
- 간단하게 클라이언트가 요청을 했을 때 세션 객체를 생성해서 자신의 세션 영역에 이름을 속성으로 저장하고, 세션에 저장되어 있는 이름 속성 값을 출력해보도록 하겠다.
- 서블릿에서는 세션을 다룰 수 있는 HttpSession 인터페이스를 제공하고 있다.
- 세션 객체는 `HttpServletRequest.getSession(true)`, `HttpServletRequest.getSession(false)` 메서드를 통해 얻을 수 있다.

### 1) 세션을 저장하는 서블릿
```java
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // TODO Auto-generated method stub
    HttpSession session = request.getSession();
    session.setAttribute("name", "정형수");
    session.setContentType("text/html;charset=UTF-8");
    PrintWriter out = response.getWriter();
    out.println("<h1>이름저장</h1>");
}
```

### 2) 세션을 출력하는 서블릿
```java
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // TODO Auto-generated method stub
    HttpSession session = request.getSession();
    String name = (String)session.getAttribute("name");
    response.setContentType("text/html;charset=UTF-8");
    PrintWriter out = response.getWriter();
    out.println("<h1>name="+name+"</h1>");
}
```

### 3) 세션 예제 (로그인)

#### `login.jsp`
```html
<form action="sessionLogin" method="post">
    아이디 : <input type="text" name="id" />
    비밀번호 : <input type="password" name="passwd" />
    <br />
    <input type="submit" value="로그인" />
</form>
```

#### `menu.jsp`
```html
<%
    String id = (String)session.getAttribute("id");
%>
<body>
<%
    if(id == null) {
%>
<a href="login.jsp">로그인</a>
<%
    }
    else {
%>
<%=id %> 님 환영합니다.
<%
    }
%>
</body>
```

#### `SessionLoginServlet.java`
```java
protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // TODO Auto-generated method stub
    rquest.setCharacterEncoding("euc-kr");
    response.setContentType("text/html;charset=euc-kr");
    PrintWriter out = response.getWriter();
    String id = request.getParameter("id");
    String passwd = request.getParameter("passwd");
    if (id.equal("java")&&passwd.equals("java")) {
        HttpSession session = request.getSession();
        session.setAttribute("id", id);
        RequestDispatcher dispatcher = request.getRequestDispatcher("menu.jsp");
        dispatch.forward(request, response);
    } else {
        out.println("<script>");
        out.println("alert('아이디나 비밀번호가 일치하지 않습니다.')");
        out.println("history.back()");
        out.println("</script>");
    }
}
```
> RequsetDispatcher 인터페이스는 특정 페이지로 포워딩하는 기능이 정의되어 있다. 생성할 때 파라미터 값으로 포워딩 될 URL이 온다.


### 서블릿에서 특정 페이지로 포워딩하는 두 가지 방법

- Dispatcher 방식 : 이 방식으로 포워딩하게 되면 주소 표시줄의 주소가 변경되지 않는다. 즉, 하나의 요청이라는 의미이다. 따라서, 같은 request 영역을 공유하게 된다.

- Redirect 방식 : 포워딩될 때 브라우저의 주소 표시줄 URL이 변경되므로 요청이 바뀌게 된다. 따라서 포워딩된 jsp 페이지는 서블릿에서 request 영역에 공유한 속성에 접근할 수 없다.