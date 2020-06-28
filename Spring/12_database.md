# Database

###### 2020.06.28

## I. Oracle 다운로드 및 설치
- 윈도우
  - `https://www.oracle.com/database/technologies/xe-downloads.html`에서 다운로드
- MacOS
  - Docker 설치
  - `$ docker pull jaspeen/oracle-xe-11g` : jaspeen의 oracle 11g 이미지 다운로드
  - `$ docker run --name oracle11g -d -p 8080:8080 -p 1521:1521 jaspeen/oracle-xe-11g` : 이미지를 컨테이너로 생성한 뒤 실행
  - `$ docker ps` : 커넽이너 목록을 출력
  - `$ docker exec -it oracle11g sqlplus` : 현재 oracle 컨테이너가 가동중이기 때문에 sqlplus 명령을 통해 실행 가능
    - username : system, password : oracle


## III. SQLPlus에서 계정 생성 및 삭제
- 생성
  ```SQL
  SQL> create user jngcii identified by mypassword;
  SQL> grant connect, resource to jngcii;
  SQL> exit
  ```

- 삭제
  ```SQL
  SQL> drop user jngcii cascade;
  SQL> exit
  ```


## IV. SQL Developer
- https://www.oracle.com/technetwork/developer-tools/sql-developer/downloads/index.html 에서 다운로드