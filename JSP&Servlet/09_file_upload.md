# 파일 업로드

###### 2020.06.17

## I. 파일 업로드의 원리

- 개발자가 입출력 스트림을 이용해서 클라이언트에서 저송되어 오는 파일 객체를 직접 업로드 처리할 수도 있으나 파일 업로드용으로 이미 개발되어 있는 컴포넌트들이 많이 있기 때문에 컴포넌트에서 제공되는 API를 이용하면 보다 쉽게 업로드 기능을 구현할 수 있다.
- 클라이언트 파일 업로드 코드
  ```html
  <form method="post" enctype="multipart/form-data">
    <input type="file" name="filename">
  </form>
  ```
  - enctype이 multipart/form-data로 설정되어 있는데, 이 타입을 지정하지 않으면 파일 선택 박스에서 선택된 파일 객체가 전송되는 것이 아니고 파이 이름만 문자열 형태로 서버로 전송된다.
  - 이 속성을 지정하면 데이터도 파일 형태로 넘어가며, 큰 용량의 데이터도 전송할 수 있다.

## II. 가장 널리 쓰여지는 업로드 모듈 COS 라이브러리

- 현재 자바에서 가장 널리 쓰여지는 업로드 컴퍼넌트
- `http://www.servlets.com`에서 다운로드 (com.oreilly.servlet의 download에서 zip파일 다운)
- 압축풀고 lib 디렉터리 안의 cos.jar 복사해서 이클립스 라이브러리 폴더에 cos.jar 파일을 추가한다.
- `Chapter10/WebContent/WEB_INF/lib/cos.jar`

### 1) MultipartRequest 클래스
- COS 라이브러리에서 가장 핵심적인 역할을 하는 클래스
- 파일 업로드를 직접적으로 담당하는 클래스
- 다른 파일 업로드 라이브러리보다 안정성이 뛰어나고, 파일 중복 처리 인터페이스를 포함하고 있기 때문에 쉽게 중복 처리가 가능하다.
- 한글 관련 문제 또한 인코딩 방식을 지정하여 쉽게 처리할 수 있다.

### 2) MultipartRequest 클래스의 생성자
```java
MultipartRequest(javax.servlet.http.HttpServletRequest request,
                java.lang.String saveDirectory,
                int maxPostSize,
                java.lang.String encoding,
                FileRenamePolicy policy)
```
- request : MultipartRequest와 연결된 request 객체
- saveDirectory : 서버 컴퓨터에 파일이 실질적으로 저장될 경로
- maxPostSize : 한 번에 업로드할 수 있는 최대 파일 크기
- encoding : 파일의 인코딩 방식
- policy : 파일 이름 중복 처리를 위한 클래스 객체

### 3) MultipartRequest 클래스의 메서드
| 메서드 | 설명 |
| --- | --- |
|getParameterNames() | 폼에서 정송된 파라미터의 타입이 file이 아닌 파라미터들의 이름들을 Enumeration 타입으로 반환한다. |
|getParameterValues() | 폼에서 전송된 파라미터 값들을 배열로 받아온다. |
|getParameter() | request 객체에 있는 지정된 이름의 파라미터 값을 가져온다. |
|getFileNames() | 파일을 여러개 업로드할 경우 타입이 file인 파라미터 이름들을 Enumeration 타입으로 반환한다. |
|getFilesystemName() | 서버에 실제로 업로드된 파일의 이름을 반환한다. |
|getOriginalFileName() | 클라이언트가 업로드한 파일의 원본 이름을 반환한다. |
|getContentType() | 업로드된 파일의 마임 타입을 반환한다. |
|getFile() | 서버에 업로드된 파일 객체 자체를 반환한다. |

## III. MultipartRequest 클래스를 이용한 파일 업로드 구현

### 1) 파일 업로드 폼 작성
- `fileUploadForm.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>

  <html>
  <head>
  <title>FileUpload Form</title>
  </head>

  <body>
    <form action="fileUpload.jsp" method="post" enctype="multipart/form-data">
      <label for="title">제목 : </label>
      <input type="text" name="title" id="title">

      <label for="filename">파일명 : </label>
      <input type="file" name="filename" id="filename">
    </form>
  </body>
  </html>
  ```

### 2) 업로드 페이지 작성
- `fileUpload.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>
  <%@ page import="com.oreilly.servlet.MultipartRequest" %>
  <%@ page import="com.oreilly.servlet.DefaultFileRenamePolicy" %>
  <%@ page import="java.uril.*" %>
  <%
    String uploadPath=request.getRealPath("/upload");

    int size = 10*1024*1024;
    String title="";
    String filename="";
    String originfilename="";

    try {
      MultipartRequest multi=newMultipartRequest(request, uploadPath, size, "UTF-8", newDefaultFileRenamePolicy());

      title=multi.getParameter("title");
      
      Enumeration files=multi.getFileNames();

      String file = (String)files.nextElement();
      filename=multi.getFilesystemName(file);
      originfilename=multi.getOriginalFileName(file);
    } catch (Exception e) {
      e.printStackTrace();
    }
  %>

  <html>

  <body>
    <form name="filecheck" action="fileCheck.jsp" method="post">
      <input type="hidden" name="title" value="<%=title%>">
      <input type="hidden" name="filename" value="<%=filename%>">
      <input type="hidden" name="originfilename" value="<%=originfilename%>">
    </form>
    <a href="#" onclick="javascript:filecheck.submit()">업로드 확인 및 다운로드 페이지 이동</a>
  </body>
  </html>
  ```

### 3) 업로드 확인 및 다운로드 페이지 작성
- `fileCheck.jsp`
  ```html
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>
  <%
    request.setCharacterEncoding("UTF-8");
    String title=request.getParameter("title");
    String filename=request.getParameter("filename");
    String originfilename=request.getParameter("originfilename");
  %>

  <html>
  <head>
  <title>파일 업로드 및 다운로드</title>
  </head>

  <body>
  제목 : <%=title %><br>
  파일명 : <a href="file_down.jsp?file_name=<%=filename %>"><%=originfilename %></a>
  </body>
  </html>
  ```

### 4) 다운로드 박스 출력 페이지 코드 작성
- `fileCheck.jsp`
  ```jsp
  <%@ page import="java.net.URLEncoder" %>
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>
  <%@ page import="java.io.File" %>
  <%@ page import="java.io.*" %>

  <%
    String filename = request.getParameter("file_name");

    String savePath = "upload";
    ServletContext context = getServletContext();
    String sDownloadPath = context.getRealPath(savePath);
    String sFilePath = sDownloadPath + "\\" + filename;
    byte b[] = new byte[4096];
    FileInputStream in = new FileInputStream(sFilePath);
    String sMimeType = getServletContext().getMimeType(sFilePath);
    System.out.println("sMimeType>>>" + sMimeType);

    if (sMimeType == null) {
      sMimeType = "application/octet-stream";
    }

    response.setContentType(sMimeType);
    String agent = request.getHeader("User-Agent");
    boolean isBrowser = (agent.indexOf("MSIE")) > -1) || (agent.indexOf("Trident") > -1);

    if (ieBrowser) {
      filename = URLEncoder.encode(fileName, "UTF-8").replaceAll("\\+", "%20");
    } else {
      fiename = new String(filename, getBytes("UTF-8"), "iso-8850-1");
    }

    response.setHeader("Content-Disposition", "attachment; filename= " + filename);

    ServletOutputStream out2 = response.getOutputStream();
    int numRead;

    while ((numRead = in.read(b, 0, b.length)) != -1) {
      out2.write(b, 0, numRead);
    }
    out2.flush();
    out2.close();
    in.close();
  %>

  <html>
  <head>
  <title>파일 업로드 및 다운로드</title>
  </head>

  <body>
  제목 : <%=title %><br>
  파일명 : <a href="file_down.jsp?file_name=<%=filename %>"><%=originfilename %></a>
  </body>
  </html>
  ```

#### part인터페이스 p.323