# 데이터베이스

###### 2020.06.18

## I. 데이터베이스 설치
- DBMS
  - Database Management System
  - 응용프로그램과 데이터베이스 사이에서 데이터가 올바르게 정보 교환을 할 수 있도록 관리해주는 시스템
  - 테이블 등을 설계하고 생성하는 **정의 기능**, 데이터를 삽입, 수정, 삭제, 검색 등 조작하는 **조작 기능**, 저장된 데이터가 일관성을 유지하고 데이터의 중복 문제를 발생하지 않도록 하는 **제어 기능**

### 1) MySQL 설치
1. `http://www.mysql.com/` 접속
2. 제일 아래 DOWNLOADS - MySQL Community Server 클릭
3. 사용중인 운영체제 선택 후 Go To Download Page
4. 아래 mysql-installer-community 다운로드
5. No thanks, just start my download
6. Developer Default 선택 후 Next
7. 필요한 구성요소를 모두 설치한 후
8. mysql 설치
9. 구성요소 확인
10. MySQL을 Document Store로 사용할지 선택하는 화면에서 체크하지 않고 Next
11. Execute 버튼을 클릭해 서버 구성을 적용
12. 완료되었으면 Finish 클릭하여 서버 구성 적용 마무리
13. 제품 구성이 완료되면 Next
14. Check 버튼을 클릭해 root 계정을 이용하여 서버 연결을 테스트
15. 연결 테스트가 성공하면 Next
16. Execute 버튼을 클릭하여 서버 구성 적용
17. 서버 구성이 완료되면 Finish
18. 제품 구성 화면이 출력되면 Next
19. 완료
20. 환경변수 설정 (시스템 변수에 `C:\Program Files\MySQL\MySQL Server 8.0\bin;` 추가)
21. `mysql -u root -p`로 확인

### 2) Oracle
> 11g를 가장 흔히 사용한다.
1. `https://www.oracle.com/database/technologies/xe-prior-releases.html` 접속
2. 안내대로 설치
3. 중간에 HTTP port 8080 -> 8081 설치


## II. SQL
- Structured Query Language

### 1) SQL 종류

1. DDL
     - CREATE (데이터베이스 또는 테이블과 같은 객체를 생성한다.)
       ```sql
       CREATE TABLE 생성할 테이블 (
         필드명1 타입명,
         필드명2 타입명,
         ...
         primary key(필드명)
       );

       CREATE USER jngcii IDENTIFIED BY mypassword;
       ```
     - ALTER (데이터베이스 또는 테이블과 같은 객체를 수정한다.)
       ```sql
       ALTER TABLE 테이블명 적용옵션 (
         컬럼명 데이터타입명
       );
       
       ALTER TABLE student MODIFY (
         name varchar2(20)
       );
       ```
     - DROP (데이터베이스 또는 테이블과 같은 객체를 제거한다.)
       ```sql
       DROP TABLE 테이블명;

       DROP TABLE student;
       ```
       > 적용옵션 : ADD, MODIFY, DROP

2. DML
     - INSERT (테이블에 데이터를 삽입한다.)
        ```sql
        INSERT INTO 테이블명 (컬럼명1, 컬럼명2, ...) VALUES (데이터값1, 데이터값2, ...);
        INSERT INTO 테이블명 VALUES (데이터값1, 데이터값2, ...);

        INSERT INTO student (id, name) VALUES (1, '홍길동');
        INSERT INTO student VALUES (1, '홍길동');
        ```
     - UPDATE (테이블에 삽입된 데이터를 수정한다.)
        ```sql
        UPDATE 테이블명 SET 컬럼명1='수정값1', 컬럼명2='수정값2', ... WHERE 컬럼명3='조건값1' AND 컬럼명4='조건값2';

        UPDATE student SET name='정형수' WHERE id=1;
        ```
     - DELETE (테이블에 삽입된 데이터를 삭제한다.)
        ```sql
        DELETE FROM 테이블명 WHERE 컬럼명1='조건값1' AND 컬럼명2='조건값2';

        DELETE FROM student WHERE name='정형수';
        ```
     - SELECT (테이블에 존재하는 데이터를 특정 조건으로 검색하여 결과를 출력한다.)
        ```sql
        SELECT 컬럼명1, 컬럼명2, ... FROM 테이블명1, 테이블명2, ... WHERE 컬럼명3='조건값1' AND 컬럼명4='조건값2' ORDER BY 컬럼명5 [ASC | DESC];

        SELECT * FROM student WHERE name='정형수';
        SELECT * FROM student ORDER BY id DESC;
        ```
3. 횐원 관리 시스템 테이블 예시
   ```sql
   CREATE TABLE member (
     id VARCHAR2(15),
     password VARCHAR2(10),
     name VARCHAR2(10),
     age NUMBER,
     gender VARCHAR2(5),
     email VARCHAR2(30),
     PRIMARY KEY(id)
   );
   ```