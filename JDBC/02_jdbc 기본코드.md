# jdbc 기본 코드

###### 2020.02.02

### I. 코드

1. `Class.forName("oracle.jdbc.driver.OracleDriver");`

>메모리상에 드라이버가 올라간다.

- 드라이버 로드하기
- oracle.jdbc.driver 패키지의 OracleDriver라는 클래스를 로드해서 객체화한다.
- 일반적으로 객체화는 `new` 연산자를 사용하지만 여기서는 `Class.forName`이라는 특별한 유틸리티를 사용한다.
- 이 과정을 통해 메모리 상에 잡히게 된다.


2. `Connection c = DriverManager.getConnection(...);`

>열결이라는것이 이루어지고 연결이 이뤄지면 객체가 반환된다.

- 드라이버매니저를 통해서 연결 객채를 얻는다.

3. `Statement st = c.createStatement();`

>여기서 쿼리를 사용자로부터 받아 실행하는 state(명령문)을 만든다.

- 실행 도구를 얻는다.

4. `ResultSet rs = st.executeQuery(sql);`

>명령문(state)을 싱핸한다.

- 결과를 실행해 그 결과를 ResultSet 타입의 참조 타입 변수에 넣어준다.

5. `rs.next();`

>명령문 실행으로부터 받아온 데이터를 사용하기 위해 한줄씩 받아온다.

- 한줄씩 가져오기

6. `String title = rs.getString("title");`

>가져온 한줄에서 특정 field(column)을 선택해서 가져온다.

<br />

II. 설명

- 이 4개의 명령들은 총 4개의 객체를 만들어낸다.

- 하지만 어떤것 하나 `new`연산자를 통해 만들어지지 않는다.

- 드라이버 매니저가 있어야 커넥션을 생성할수 있구 커넥션이 있어야만 실행도구가 필요한 것이고 실해도구가 있어야 쿼리를 실행할 수 있기때문에 
이런 순차적 흐름이 존재