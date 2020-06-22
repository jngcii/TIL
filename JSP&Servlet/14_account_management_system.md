# 데이터베이스를 연동한 회원 관리 시스템

###### 2020.06.22

## I. 회원 관리 시스템 설계하기
- 회원 관리 시스템을 개발하기 전에 무엇이 필요한지 미리 준비하고 어떻게 개발할 것인지 설계

### 1) 테이블 설계
  ```sql
  CREATE TABLE member (
      id VARCHAR2(15),
      password VARCHAR2(10),
      name VARCHAR2(15),
      age NUMBER,
      gender VARCHAR2(5),
      email VARCHAR(30),
      PRIMARY KEY(id)
  );
  ```

### 2) 페이지 설계
| 웹 페이지 | 설명 |
|---|---|
|loginForm.jsp | 로그인 폼 페이지(로그인 정보를 입력하는 페이지) |
|joinForm.jsp | 회원 가입 폼 페이지(회원 가입 정보를 입력하는 페이지) |
|loginProcess.jsp | 로그인을 실제로 처리하는 페이지 |
|joinProcess.jsp | 회원 가입을 실제로 처리하는 페이지 |
|main.jsp | 메인 페이지 |
| member_list.jsp | 회원 목록을 확인하는 페이지 |
|member_info.jsp | 특정 회원 정보를 보여주는 페이지 |
|member_delete.jsp | 특정 회원 정보를 삭제하는 페이지 |

### 3) 세부 설계
- 처음에는 회원 가입 페이지에서 회원 가입 처리를 진행하고 로그인 페이지에서 로그인을 하게 되면 메인 페이지가 출력
- 관리자 아이디로 접속했을 경우는 메인 페이지에서 관리자 페이지인 회원 목록 페이지로 이동할 수 있도록 구현한다.
- DB 연결은 CP를 사용할 것이므로 `WebConent\META-INF\context.xml` 파일이 존재해야 한다.

### 4) 이클립스의 DataSource Explorer 툴
> sql 관련 작업을 수행할 때 sqlplus와 같은 별도의 툴을 이용할 필요 없이 이클립스 내에서 모든 처리가 가능
1. `Data Source Explorer` 뷰에서 `DataBase Connections` -> `New` 메뉴를 선택
2. 사용 DBMS 종류를 `Oracle`로 선택하고 `Next` 버튼을 클릭
3. `New Driver Definition` 클릭
4. `Oracle Thin Driver 11`을 선택하고 `JAR List` 탭을 선택
5. 현재 설정되어 있는 jar 파일을 선택하고 `<Edit JAR/Zip>` 버튼을 클릭
6. `C:\oraclexe\app\oracle\product\11.2.0\server\jdbc\lib\ojdbc6.jar` 파일을 연 후 `Properties` 탭을 클릭
7. `Properties` 탭에서 오라클 연결에 관한 설정을 입력한다.
   - Connection URL : Server 부분을 삭제하고 localhost라는 오라클이 실질적으로 구동되고 있는 호스트를 지정한다. 만약 연결하려는 오라클 서버사 localhost가 아니라 다른 시스템에서 실행되고 있ㄴ다면 해당 서버의 ip 주소를 지정해 주어야 한다. 마지막 DB 부분은 실질적으로 서비스되고 있는 오라클의 SID명을 지정하면된다. 여기서는 설치한 데이터베이스명인 XE를 지정한다.
   - Driver Class : 오라클이 제공하는 드라이버 클래스명을 지정한다. 기본적으로 제공되는 이름을 사용한다.
   - Password : 오라클 암호를 지정한다.
   - User ID : 오라클 계정을 지정한다.
8. `Save password` 체크박스를 체크한 후 `<Text Connection>` 버튼을 클릭하여 데이터베이스 연결을 테스트 한 후 `Ping succeeded` 화면이 출력되면 `<Finish>` 버튼을 클릭한다.
   - 여기서 포트번호를 알기 위해서는 `C:\oraclexe\app\oracle\product\11.2.0\server\network\ADMIN\listener.ora`를 확인하면 된다.
9.  `New Oracle`을 클릭하여 확장하였을 때 XE 데이터베이스의 객체들이 출력되면 데이터베이스가 제대로 연결된 것이다.
10. SQL문을 실행할 수 있는 SQL File을 생성하기 위해서 WebContent 디렉터리에서 마우스 우측 버튼을 클릭하고 `New` -> `SQL File` 메뉴를 선택한다. 이클립스에서 SQL File을 생성하면 SQL File 안에서 모든 SQL문을 실행할 수 있다.
11. 필요한 속성들을 설정한 후 완료한다.
12. test 테이블 생성 SQL문을 입력한 후 실행할 SQL문을 마우스로 드래그해서 선택한 후 마우스 우측 버튼을 클릭한 후 `Execute Selected Text` 메뉴를 선택한다. (`alt + x`)
13. succeeded 메뉴가 출력되면 SQL문이 성공적으로 실행된 것이다.
14. 다음 화면에서 `JAVA -> Tables` 디렉터리에 `TEXT` 테이블이 존재하면 SQL문이 성공적으로 실행된 것이다.


## II. 코드 작성
- [코드 링크](https://github.com/jngcii/jsp_member_management_system/tree/master/WebContent)