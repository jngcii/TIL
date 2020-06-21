# 커넥션 풀 (Connection Pool)

###### 2020.06.21

## I. 커넥션 풀
- 데이터베이스와 연결된 Connection 객체를 사용하고, 작업이 끝나면 다시 반환하는 것
- 사용자가 웹사이트에 요청을 하는데 이 때마다 매번 Connection 객체를 생성하여 연결하면 메모리에 Connection 객체가 너무 많이 생성되게 된다.
- 커넥션 풀을 사용하면 풀 속에 미리 커넥션이 생성되어있기 때문에 커넥션을 생성하는데 드는 연결 시간이 소비되지 않고, 다른 사용자가 사용하지 않는 커넥션을 재사용이 가능하기 때문에 사용자가 접속할 때마다 계속해서 커넥션을 생성할 필요가 없다.
- 사용자가 웹사이트에 접속하여 데이터베이스 관련 작업을 요청하면 서버는 커넥션 객체를 얻어와 데이터베이스에 접속하여 데이터베이스 작업을 수행한다. 수행을 완료하였다면 커넥션 객체를 다시 커넥션 풀로 반환하는 작업을 한다. 반환된 커넥션 객체는 데이터베이스 작업을 요청한 다른 사용자에 의해서 사용될 수 있다.
- CP(Connection Pool)을 사용하는 것은 데이터베이스 관련 애플리케이션을 개발할 때는 필수적이다.

## II. JNDI
- JNDI (Java Naming and Directory Interface)란 명명 서비스 및 디렉터리 서비스에 접근하기 위한 API이다.
- 특정 자원에 접근하기 위한 이름

## III. DBCP API를 사용하여 데이터베이스 사용하기
- 톰캣에서는 `Tomcat\lib\` 디렉터리 경로에 CP 기능을 제공하기 위한 DBCP API를 제공한다. (tomcat-dbcp.jar)

1. `Chapter13\WebContent\META-INF` 디렉터리 밑에 context.xml 파일을 생성해서 서버에 공유할 리소스를 정의한다.
    - `context.xml`
        ```xml
        <Context>
            <Resource
                name="jdbc/OracleDB"
                auth="Container"
                type="javax.sql.DataSource"
                username="jngcii"
                password="7777"
                driverClassName="oracle.jdbc.driver.OracleDriver"
                factory="org.apache.tomcat.dbcp.dbcp2.BasicDataSourceFactory"
                url="jdbc:oracle:thin:@127.0.0.1:1521:XE"
                maxActive="500"
                maxIdle="100"
            />
        </Context>
        ``
        - name : 공유하는 리소스의 이름을 지정하는 부분. 클라이언트에서 정의하는 리소스를 얻어갈 때는 여기서 name 속성으로 정의한 리소스명을 사용해야 한다.
        - auth : 클라이언트에서 리소스를 얻어갈 때 인증은 톰캣 컨테이너에서 하겠다는 의미
        - type : 공유할 리소스의 타입을 DataSource로 지정하는 부분. 클라이언트에서는 공유된 DataSource의 getConnection() 메서드를 사용해서 Connection 객체를 얻어갈 수 잇다.
        - factory : DBCP API를 사용해서 클라이언트에 공유할 DataSource를 생성하도록 지정하는 부분. 자바 API 클래스 중 이름이 Factory로 끝나는 클래스들은 특정 객체를 생성하여 반환하는 역할을 하는 클래스이다.
        - maxActive : 동시에 제공할 수 있는 최대 Connection 개수를 지정하는 부분
        - maxIdle : 현재 서비스되고 있는 Connection 객체를 제외한 CP에 여유로 남길 수 있는 최대 Connection 개수를 지정한 부분
2. `dbcpAPITest.jsp` 코드 작성
    - `dbcpAPITest.jsp`
        ```jsp
        <%@ page language="java" contentType="text/html; charset=UTF-8" %>
        <%@ page import="java.sql.*" %>
        <%@ page import="javax.sql.*" %>
        <%@ page ipmort="javax.naming.*" %>
        <%
            Connection conn = null;

            try {
                Context init = new InitialContext();
                DataSource ds = (DataSource) init.looup("java:comp/env/jdbc/OracleDB");
                conn = ds.getConnection();
                out.println("<h3>연결되었습니다.</h3>");
            } catch(Exception e) {
                out.println("<h3>연결에 실패하였습니다.</h3>");
                e.printStackTrace();
            }
        %>
        ```

## IV. 트랜잭션 (Transaction)
- 일 처리의 최소 단위
- 데이터베이스 처리를 모두 일관되게 하기 위해 존재
- 만약 테이블에 10000개의 데이터가 있고 10000개의 데[이터에 대해서 수정 작업을 하는데, 5000개의 데이터에 수정 작업이 완료된 후 시스템에 문제가 발생한 경우 5000개만 수정된 상태에서 작업이 완료되면 데이터의 일관성이 깨지기 대문에 수정이 완료된 5000개의 데이터 작업도 취소시켜서 원래 데이터로 되돌려야 한다.
- 계좌이체 요청 시 인출 계좌에서 금액을 차감하는 작업은 성공하고, 이체 대상 계좌의 금액을 증감하는 작업은 실패한 상황에서 계좌이체가 마무리되면 문제가 발생할 수 있기 때문에 두 개의 작업이 모두 성공했을 때만 계좌이체 작업을 마무리해 주어야 한다.

### 트랜직션의 기본 흐름
1. 처음 데이터베이스 작업을 시작하기 전에 Begin으로 작업이 시작된다.
2. Process 단계에서 각 데이터베이스 작업들을 처리하게 되면 이 작업들이 오류 없이 모두 잘 작동된다면 Commit을 수행하게 된다.
3. 이로써 트랜잭션 처리가 마무리된 것이다.
4. 여러 데이터베이스 작업들 중 하나의 작업이라도 문제가 발생하게 되면 Rollback을 실행하여 begin 이후에 처리한 데이터 작업은 모두 무효 처리가 된다.
5. Process 단계에서 처리되는 작업들은 Commit이 실행되지 않는 한 실제데이터베이스 파일에 업데이트 작업이 아루어지지 않는다.
    > 이처럼 트랜잭션을 이용하면 하나의 트랜잭션으로 묶인 작업들을 전부 실행되든지 전부 취소되게 처리할 수 있다.