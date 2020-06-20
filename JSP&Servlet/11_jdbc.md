# JDBC

###### 2020.06.18

## I. JDBC
- JDBC란 자바와 DBMS를 연결시켜주는 API이다.
- DBMS 종류에 상과없이 독립적으로 사용 가능
- 자바에서 제공하는 API중 가장 성공적인 API중 하나

## II. JDBC 드라이버 설치
- JDBC 드라이버는 각 DBMS와 연동하여 JDBC API를 사용할 수 있도록 지원해주는 JDBC API 모듈이다.
- DBMS 종류에 맞는 JDBC 드라이버를 설치해주어야 한다.
- 드라이버 설치는 간단한데 아래의 설치방법을 익히면 다른 DBMS 드라이버도 쉽게 설치할 수 있다.
- `C:\oraclexe\app\oracle\product\11.2.0\server\jdbc\lib` 폴더 안의 ojdbc6.jar 가 JDBC 드라이버 파일이다.
- 해당 파일을 톰캣의 lib 디렉터리에 복사한다. (jsp2.3\Tomcat\lib)
- 톰캣의 라이브러리 디렉터리에 ojdbc6.jar 파일을 복사하면 해당 톰캣을 사용하는 모든 프로젝트에서 DB 작업이 가능하지만, 개별 프로젝트에서만 라이브러리를 등록하려면 이클립스에서 JDBC를 사용할 프로젝트의 라이브러리 폴더에 ojdbc6.jar 파일을 복사하면 된다. (WebContent 안의 lib 폴더에 ojdbc6.jar 파일을 복사)

## III. JDBC 프로그램의 작성 단계
1. JDBC 드라이버 이름 및 접속할 JDBC URL 설정
    - JDBC 드라이버 이름을 설정하는 이유 : JDBC가 어느 DBMS에 대한 드라이버를 사용하는지 알아야 하기 때문
    - 오라클을 사용하는 경우는 오라클에 맞는 드라이버 이름을 사용해야 한다.
    - 접속할 JDBC URL은 접속할 DBMS의 호스트 주소 등을 의미
2. JDBC 드라이버 로드
3. JDBC URL과 계정 정보를 이용하여 Connection 객체를 얻음
    - Connection 객체는 실제 데이터베이스 작업을 하기 위해 꼭 필요한 객체
    - 이 객체를 얻어왔다면 이것을 이용하여 여러 가지 작업을 수행할 수 있다.
4. JDBC를 이용한 데이터베이스 작업

## IV. JDBC 연동 예제
- `jdbcTest.jsp`
  ```jsp
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>
  <%@ page import="java.sql.*" %>
  <%
    Connection conn=null;

    String driver="oracle.jdbc.driver.OracleDriver";
    String url="jdbc:oracle:thin:@localhost:1521:XE";

    Boolean connect=false;

    try {
        Class.forName(driver);
        conn=DriverManager.getConnection(url, "jngcii", "7777");

        connect=true;

        conn.close();
    } catch(Exception e) {
        connect=false;
        e.printStackTrace();
    }
  %>

  <html>
  <head>
    <title>JDBC 연동 테스트 예제</title>
  </head>

  <body>
    <h3>
      <% if(connect==true) { %>
        연결되었습니다.
      <% } else { %>
        연결에 실패하였습니다.
      <% } %>  
    </h3>
  </body>
  </html>
  ```
  > 연결에 실패한 경우 해결 방법 ( p.433 )

## V. MySQL과 연동하기
1. `C:\Program Files (x86)\MySQL\Connector J 8.0` 경로에서 mysql-connector-java-8.0.20.jar 파일 복사
2. `WebContent\WEB-INF\lib` 디렉터리에 붙여넣기
3. MySQL로 접속할 때 사용할 사용자명과 데이터베이스를 생성
   ```sql
   CREATE USER 'jngcii'@'%' IDENTIFIED BY '7777';
   GRANT ALL PRIVILEGES ON *.* TO 'jngcii'@'%' WITH GRANT OPTION;
   CREATE DATABASE testDB;
   SHOW DATABASES;
   ```
   - `*.*`의 의미는 모든 데이터베이스의 모든 객체에 대한 권한을 부여한다는 의미
   - `'jngcii'@'%'`는 jngcii 계정에 권한을 부여한다는 의미인데 @ 뒤에 있는 내용은 어떤 호스트에서 접속을 허용하겠느냐를 지정하는 부분이다. 이 부분을 %로 지정하면 다른 모든 호스트에서 jngcii 계정으로 로그인이 가능하다는 의미이다. 만약 로컬로만 인증이 가능하게 하려면 이 부분을 localhost로 지정하면 된다.

### 작성 예제
- `mySQLJdbcTest.jsp`
  ```jsp
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>
  <%@ page import="java.sql.*" %>
  <%
    Connection conn=null;

    String driver="com.mysql.jdbc.Driver";
    String url="jdbc:mysql://localhost:3306/testDB";

    Boolean connect=false;

    try {
        Class.forName(driver);
        conn=DriverManager.getConnection(url, "jngcii", "7777");

        connect=true;

        conn.close();
    } catch(Exception e) {
        connect=false;
        e.printStackTrace();
    }
  %>

  <html>
  <head>
    <title>JDBC 연동 테스트 예제</title>
  </head>

  <body>
    <h3>
      <% if(connect==true) { %>
        연결되었습니다.
      <% } else { %>
        연결에 실패하였습니다.
      <% } %>  
    </h3>
  </body>
  </html>
  ```
