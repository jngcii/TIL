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