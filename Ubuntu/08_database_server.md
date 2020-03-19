# Database Server

###### 2020.03.19

## 주요 Query문
### DB 관련
- SHOW DATABASES;
- USE [DATABASE NAME];
- CREATE DATABASE [DATABASE NAME];
- DROP DATABASE [DATABASE NAME];
### TABLE 관련
- SHOW TABLES;
- EXPLAIN [TABLE NAME]; or DESC [TABLE NAME];
- CREATE TABLE [TABLE NAME] ([FIELD NAME1] [FIELD TYPE1], [FIELD NAME2] [FIELD TYPE2], ...);
  - FIELD TYPE
    - VARCHAR(n) : 최대 n개 문자의 문자열
    - CHAR(n) : 고정된 n개의 문자열
    - INT : 정수
    - FLOAT : 실수
    - DATE : 날짜
    - TIME : 시간
    - 등등
- DROP TABLE [TABLE NAME];
- ALTER TABLE ~
  - ALTER TABLE [TABLE NAME] MODIFY [FIELD NAME] [NEW FIELD NAME];
  - ALTER TABLE [TABLE NAME] CHANGE [FIELD NAME] [NEW FIELD NAME] [NEW FIELD TYPE];
  - ALTER TABLE [TABLE NAME] ADD [NEW FIELD NAME] [NEW FIELD TYPE] AFTER [FIELD NAME];
  - ALTER TABLE [TABLE NAME] DROP [FIELD NAME];
### 테이블 조회
- SELECT * FROM [TABLE NAME];
- SELECT ([FIELD NAME1], [FIELD NAME2], [FIELD NAME3]) FROM [TABLE NAME] WHERE [조건];

## 데이터베이스 서버 설치
1. http://downloads.mariadb.org/mariadb/repositories/ 의 UBUNTU >> 16.04 LTS xenial >> 10.1 stable >> KAIST FILE Archive 에서 software-properties-common 등 관련 설정 복사해서 터미널에 붙여넣고 `enter`
2. 그냥 apt package 저장소 (ppa) 찾아도 된다.
3. `$ apt-get update`
4. 마리아 DB 설치 `$ apt-get -y install mariadb-server mariadb-client`
5. 데몬 재시작 `$ systemctl restart / status mysql` (mariadb의 데몬 이름이 mysql이다.)
6. 포트 개방 `$ ufw allow 3306` (각 서버 포트번호는 /etc/services에 저장되어있음)
7. `$ mysql -u [DB USERNAME] -p`
8. root 비번 설정 `$ mysqladmin -u root password '1234'`
9. `exit`으로 클라이언트 종료
10. `vim /etc/mysql/my.conf` 47행쯤 bind-address=127.0.0.1 부분에 주석(#) 붙이기 
 - 원래 mariaDB server 는 외부에서 접속이 안되게 설정되어있는데 그걸 없애는 것이다.
11.  systemctl restart mysql

### Client에서 접속할 사용자 생성
```bash
# 1. root로 서버 입장
$ mysql -u root -p

# 2. 데이터베이스 사용
$ USE mysql;

# 3. user 테이블에서 user, host 필드만 가져오기. 단, 사용자 이름이 빈 것은 제외
$ SELECT user, host FROM user WHERE user NOT LIKE '';

# 4. 192.168.111.xxx의 IP 주소 모두에서 접근할 수 있는 사용자 생성
GRANT ALL PRIVILEGES ON *.* TO jngcii@'192.168.111.%' IDENTIFIED BY '1234';
# GRANT 사용권한 ON DB이름.TABLE이름 TO 사용자이름@'호스트이름' IDENTIFIED BY '비번';
# 사용권한 : ALL PRIVILEGES, SELECT, INSERT, UPDATE, DELETE
```

### Client에서 접근
- `$ mysql -h 192.168.111.100 -u jngcii -p` -> `enter` -> 1234 -> `enter`


## MariaDB 데이터베이스 생성 및 운영
1. CREATE DATABASE shopping-db;
2. SHOW DATABASES;
3. USE shopping-db;
4. 테이블 생성
   1. CREATE TABLE customer (id VARCHAR(10) NOT NULL PRIMARY KEY, name NVARCHAR(5), age INT, address NVARCHAR(5));
   2. CREATE TABLE purchase (no INT NOT NULL PRIMARY KEY AUTO_INCREMENT, cust_id VARCHAR(10), date CHAR(8), product NVARCHAR(5));
5. 레코드 입력
   1. INSERT INTO customer VALUES ('hong', '홍길동', 22, '서울');
   2. INSERT INTO purchase VALUES (null, 'hong', '20160122', 'TV');
6. 확인
   1. SELECT * FROM custormer;
   2. SELECT * FROM purchase;