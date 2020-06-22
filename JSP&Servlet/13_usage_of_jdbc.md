# JDBC의 실전 활용

###### 2020.06.21

## I. Statement와 PreparedStatement

### 1) Statement
- 실제 데이터베이스에 SQL문을 보내기 위해 필요한 객체이다.
- 삽입, 수정, 삭제, 검색을 처리하는 DML문을 사용할 때는 이 인터페이스를 사용한다.
- 이 객체는 Connection 객체의 연결 정보를 가져와서 DB에 접근하므로 이 객체를 사용하기 위해서는 접속 상태인 Connection 객체가 먼저 존재해야 한다.
- 자주 사용되는 메서드
    | 메서드 | 설명 |
    | --- | --- |
    |executeQuery(String sql) | SELECT문을 실행할 때 사용한다. (ResultSet 객체 반환) |
    |executeUpdate(String sql) | 삽입, 수정, 삭제와 관련된 SQL문을 실행에 사용한다. 적용된 행수를 반환한다. |
    | close() | Statement 객체를 반환할(닫을) 때 사용한다. |
- 예시(`statementTest.jsp`)
  ```jsp
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>
  <%@ page import="java.sql.*" %>
  <%@ page import="javax.sql.*" %>
  <%@ page import="javax.naming.*" %>

  <%
    Connection conn = null;
    String sql="INSERT INTO student (num, name) VALUES (7, 'jngcii')";
    Statement stmt = null;

    try {
        Context init = new InitialContext();
        DataSource ds = (DataSource) init.lookup("java:comp/env/jdbc/OracleDB");
        conn = ds.getConnection();
        stmt = conn.createStatement();

        int result = stmt.excuteUpdate(sql);
        if(result!=0) {
            out.println("<h3>레코드가 등록되었습니다.</h3>");
        }
    } catch(Exception e) {
        out.println("<h3>레코드 등록에 실패하였습니다.</h3>");
    } finally {
        try {
            stmt.close();
            conn.clse();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
  %>
  ```

### 2) PreparedStatement
- PreparedStatement 인터페이스는 Statement 인터페이스를 상속한다.
- Statement와 같이 레코드 조작 및 검색 쿼리를 위한 SQL 문을 전달하기 위해 사용되지만 **PreparedStatement를 이용하게 되면 값 매핑 기능을 사용해서 Statement 인터페이스보다 편리하게 SQL문을 전송할 수 있다.**
- 예시(`preparedStatementTest.jsp`)
  ```jsp
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>
  <%@ page import="java.sql.*" %>
  <%@ page import="javax.sql.*" %>
  <%@ page import="javax.naming.*" %>

  <%
    Connection conn = null;
    String sql="INSERT INTO student (num, name) VALUES (?, 'jngcii')";
    PreparedStatement pstmt = null;

    try {
        Context init = new InitialContext();
        DataSource ds = (DataSource) init.lookup("java:comp/env/jdbc/OracleDB");
        conn = ds.getConnection();
        pstmt = conn.prepareStatement(sql);

        for(int i=8; i<=11; i++) {
            pstmt.setInt(1, i);
            if (pstmt.executeUpdate()!=0) {
                out.println("<h3>" + i + "번 레코드를 등록하였습니다.</h3");
            }
        }
    } catch(Exception e) {
        out.println("<h3>레코드 등록에 실패하였습니다.</h3>");
    } finally {
        try {
            stmt.close();
            conn.clse();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
  %>
  ```
- PreparedStatement를 사용하면 반복되는 SQL문을 쉽게 구현할 수 있게 된다.

## II. Stored Procedure와 CallableStatement
- Stored Procedure는 데이터베이스 내에 프로시저를 선언하여 클라이언트가 필요할 때마다 호출하여 사용하도록 하는 단위로, '저장된 프로시저'라고도 한다.
- 클라이언트에서 SQL문을 실행하는 것과 달리 데이터베이스쪽에서 프로시저로 존재하는 것이기 때문에 클라이언트에서 저장된 프로시저를 실행만 해주면 그 프로시저 내용이 오라클 내부에서 바로 처리되므로 실행 속도 또한 더 빠르면 네트워크에서 사용하는 쿼리 양도 줄어드므로 부하가 적다는 장점이 있다.
- 데이터베이스 내에 존재한다는 특성 때문에 각 DBMS마다 프로시저를 생성하는 문법도 다르다.
- 간단한 예제
  ```jsp
  <%
  //...
  conn = ds.getConnection();
  CallableStatement cs = conn.prepareCall("{call procedure_name(?,?,?)}");
  cs.setInt(1, 1);
  cs.setString(2, "jngcii");
  cs.registerOutPrameter(3, java.sql.Types.VARCHAR);
  cs.execute();
  out.println("<h3>" + cs.getString(3) + "</h3>");
  cs.close();
  //...
  %>
  ```

## III. ResultSet과 ResultSetMetaData

### 1) ResultSet
- Statement 객체 또는 PreparedStatement 객체로 SELECT 문을 사용하여 얻어온 레코드 값을 테이블의 형태로 갖게 되는 객체
- SELECT 문을 통해 데이터를 얻어오면 ResultSet 객체에 그 데이터가 저장된다.
- 메서드
  | 메서드 | 설명 |
  | --- | --- |
  |close() | ResultSet 객체를 반환한다. (닫는다.) 객체를 사용했다면 필수적으로 실행해주어야 하는 메서드 |
  |getXXX(int ColumnIndex) | 인자로 지정된 번호의 칼럼을 XXX 데이터 타입으로 가져온다. (컬럼 인덱스 지정) |
  |getXXX(String ColumnName) | 인자로 지정된 컬럼명의 컬럼값을 XXX 데이터 타입으로 가져온다. (컬럼명 지정) |
  |next() | 다음 행(레코드)으로 커서(작업 위치)를 이동한다. (다음 행이 없으면 false 반환, 있으면 true 반환) |

### 2) ResultSetMetaData
- ResultSet으로 얻어온 레코드들의 메타 정보에 해당하는 컬럼의 정보들을 제공한다.
- ResultSetMetaData 객체를 사용하게 되면 컬럼 수나 각 컬럼 이름, 컬럼 타입 등의 정보를 쉽게 알아낼 수 있다.
- 메서드
  | 메서드 | 설명 |
  | --- | --- |
  |getColumnCount() | ResultSet에 저장되어있는 테이블의 컬럼의 수를 반환한다. |
  |getColumnLabel(int column) | 해당 번호의 컬럼의 레이블을 반환한다. |
  |getColumnName(int column) | 해당 번호의 컬럼의 이름을 반환한다. |
  |getColumnType(int column) | 해당 번호의 컬럼의 데이터 타입을 int형으로 반환한다. |
  |getColumnTypeName(int column) | 해당 번호의 컬럼의 데이터 타입을 String형으로 반환한다.|
- 예시(`resultSetMetaDataTest.jsp`)
  ```jsp
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>
  <%@ page import="java.sql.*" %>
  <%@ page import="javax.sql.*" %>
  <%@ page import="javax.naming.*" %>
  <%
    Connection conn = null;
    String sql = "SELECT * FROM student";
    PreparedStatement pstmt = null;
    ResultSet rs = null;
    ResultSetMetaData rsmd = null;

    try {
        Context init = new InitialContext();
        DataSource ds = (DataSource) init.lookup("java:comp/env/jdbc/OracleDB:");
        conn = ds.getConnection();

        pstmt = conn.preparedStatement(sql);
        rs = pstmt.executeQuery();
        rsmd = rs.getMetaData();

        out.println("컬럼 수 : " + rsmd.getColumnCount() + "<br>");
        for (int i=1; i<=rsmd.getColumnCount(); i++) {
            out.println(i + "번째 칼럼의 이름 : " + rsmd.getColumnName(i) + " : ");
            out.println(i + "번째 컬럼의 타입 이름 : " + rsmd.getColumnTypeName(i) + "<br>");
        }
    } catch (Exception e) {
        e.printStackTrace();
    } finally {
        try {
            res.close();
            pstmt.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
  %>
  ```

## IV. ResultSet의 커서 자유롭게 움직이기
- ResultSet 객체는 여러 레코드들이 저장되어 있는 객체이다.
- 여기서 자신이 원하는 레코드에 접근하려면 커서를 자유롭게 움직일 수 있어햐 한다.
- 메서드
  | 메서드 | 설명 |
  |--- | --- |
  |absolute(int rowNum) | 지정한 위치로 커서를 이동한다. |
  |beforeFirst() | 커서를 처음 레코드 이전 위치로 이동한다. 커서를 실제 레코드가 아닌 ResultSet 객체의 처음 부분으로 이동한다. |
  |afterLast() | 커서를 마지막 레코드 이후 위치로 이동한다. 커서를 실제 레코드가 아닌 ResultSet 객체의 끝 부분으로 이동한다. |
  |first() | 처음 레코드가 존재하는 행으로 이동한다. |
  |last() | 마지막 레코드가 존재하는 행으로 이동한다. |
  |next() | 다음 레코드 행으로 이동한다. |
  |previous() | 이전 레코드 행으로 이동한다. |
- 예시 (`resultSetCursorTest.jsp`)
  ```jsp
  <%@ page language="java" contentType="text/html; charset=UTF-8" %>
  <%@ page import="java.sql.*" %>
  <%@ page import="javax.sql.*" %>
  <%@ page import="javax.naming.*" %>
  <%
    Connection conn = null;
    String sql = "SELECT * FROM student";
    PreparedStatement pstmt = null;
    ResultSet rs = null;

    try {
        Context init = new InitialContext();
        DataSource ds = (DataSource) init.lookup("java:comp/env/jdbc/OracleDB:");
        conn = ds.getConnection();

        pstmt = conn.preparedStatement(sql, ResultSet.TYPE_SCROLL_SENSITIVE, ResultSet.CONCUR_UPDATABLE);
        rs = pstmt.executeQuery();

        rs.last();
        out.println(rs.getInt(1) + "," + rs.getString(2) + "<br>");

        rs.fisrt();
        out.println(rs.getInt(1) + "," + rs.getString(2) + "<br>");

        rs.absolute(3);
        out.println(rs.getInt(1) + "," + rs.getString(2) + "<br>");

    } catch (Exception e) {
        out.println("<h3>데이터를 가져오지 못했습니다.</h3>");
        e.printStackTrace();
    } finally {
        try {
            res.close();
            pstmt.close();
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
  %>
  ```
- ResultSet 옵션 값
  | 상수명 | 설명 |
  |---|---|
  |TYPE_FORWARD_ONLY | 커서 이동을 다음 레코드로만 이동되도록 한다. |
  | TYPE_SCROLL_SENSITIVE | 커서 이동을 자유롭게 하고 업데이트 내용을 반영한다. |
  |TYPE_SCROLL_INSENSITIVE | 커서 이동을 자유롭게 하고 업데이트 내용을 반영하지 않는다. |
  | CONCUR_UPDATABLE | 데이터 변경이 가능하도록 한다. |
  | CONCUR_READ_ONLY | 데이터 변경이 불가능하도록 한다. |
    - 앞 예제 코드에서 아무 옵션을 주지 않게 되면 기본 값으로 TYPE_FORWARD_ONLY 값이 적용되는데 이 때문에 first(), last() 등 커서를 이동하는 메서드를 사용할 수 없게 되는 것이다.
    - 즉, 스크롤이 가능하게 하는 TYPE_SCROLL_SENSITIVE, TYPE_SCROLL_INSENSITIVE 옵션 등을 주어야 레코드의 위치를 자유롭게 이동시킬 수 있다.


## V. CLOB 데이터 다루기
- CLOB이란 오라클에 존재하는 데이터 타입으로 대량의 텍스트 데이터를 저장할 수 있다.
- 다른 필드 타입과는 달리 다루기가 조금 까다롭다.
- CLOB 타입 데이터를 다루려면 톰캣과의 호환성과 오라클 버전을 모두 잘 살펴보아야 한다. 오라클 버전에 따라서도 CLOB 타입 데이터를 다루는 방법이 다르기 때문이다.

### 1) CLOB 데이터 삽입하기
1. 우선 다음과 같이 clobtable을 생성한다.
   ```sql
   CREATE TABLE clobtable (num Number, content CLOB);
   ```
2. 그 다음 아래와 같이 clob 타입을 사용하는 코드를 작성하도록 한다.
    ```jsp
    <%@ page language="java" contentType="text/html; charset=UTF-8" %>
    <%@ page import="java.sql.*" %>
    <%@ page import="javax.sql.*" %>
    <%@ page import="javax.naming.*" %>
    <%
        Connection conn = null;
        PreparedStatement pstmt = null;
        StringBuffer sb = null;

        try {
            Context init = new InitialContext();
            DataSource ds = (DataSource) init.lookup("java:comp/env/jdbc/OracleDB:");
            conn = ds.getConnection();

            String sql = "INSERT INTO clobtable (num, content) VALUES (1, ?)";
            sb = new StringBuffer();

            for (int i=0; i<10000; i++) {
                sb.append("홍길동");
            }

            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, sb.toString());
            pstmt.executeUpdate();
            out.println("데이터를 저장했습니다.");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                pstmt.close();
                conn.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    %>
    ```

### 2) 삽입된 CLOB 데이터 읽기
- `clobReadTest.jsp`
  ```jsp
    <%@ page language="java" contentType="text/html; charset=UTF-8" %>
    <%@ page import="java.sql.*" %>
    <%@ page import="javax.sql.*" %>
    <%@ page import="javax.naming.*" %>
    <%
        Connection conn = null;
        PreparedStatement pstmt = null;
        StringBuffer sb = null;
        ResultSet rs = null;

        try {
            Context init = new InitialContext();
            DataSource ds = (DataSource) init.lookup("java:comp/env/jdbc/OracleDB:");
            conn = ds.getConnection();
            pstmt = conn.prepareStatement("SELECT * FROM clobtable WHERE num=1");
            rs = pstmt.executeQuery();
            
            if (rs.next()) {
                out.println(rs.getString("content"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try {
                rs.close();
                pstmt.close();
                conn.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    %>
  ```