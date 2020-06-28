# JDBC

###### 2020.06.28

## I. 테이블 생성 및 삭제

### 1) member 테이블 생성
```sql
CREATE TABLE member (
  memId VARCHAR2(10) CONSTRAINT memId_pk PRIMARY KEY,
  memPw VARCHAR2(10),
  memName VARCHAR2(15),
  memPurcNum NUMBER(3) DEFAULT 0 CONSTRAINT memPurNum_ck CHECK (memPurcNum < 3)
);
```
> memPurcNum : 구매 횟수

### 2) member 테이블에 테스트 차원에서 b 계정을 삽입
```sql
INSERT INTO member (memId, memPw, memName) values ('b', 'bb', 'bbb');
```

### 3) member 테이블의 모든 회원정보 출력
```sql
SELECT * FROM member;
```

### 4) member 테이블에서 memId가 b인 회원 삭제
```sql
DELETE FROM member WHERE memId='b';
```

### 5) member 테이블 삭제
```sql
DROP TABLE member;
```

## II. JDBC
> 드라이버 로딩 -> DB연결 -> SQL작성 및 전송 -> 자원 해제
- `MemberDao.java`
  ```java
  @Component
  public class MemberDao implements IMemberDao {
    
    private String driver = "oracle.jdbc.driver.OracleDriver";
    private String url = "jdbc:oracle:thin:@localhost:1521:xe";
    private String username = "jngcii";
    private String password = "7777";
    
    private Connection conn = null;
    private PreparedStatement pstmt = null;
    private ResultSet rs = null;
    
    public MemberDao() {
  //		dbMap = new HashMap<String, Member>();
    }
    
    @Override
    public int memberInsert(Member member) {

      int result = 0;
      
      try {
        
        Class.forName(driver);
        conn = DriverManager.getConnection(url, username, password);
        String sql = "INSERT INTO member (memId, memPw, memName) VALUES (?, ?, ?)";
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, member.getMemId());
        pstmt.setString(2, member.getMemPw());
        pstmt.setNString(3, member.getMemName());
        result = pstmt.executeUpdate();
        
      } catch (ClassNotFoundException e) {
        // TODO: handle exception
        e.printStackTrace();
      } catch (SQLException e) {
        e.printStackTrace();
      } finally {
        try {
          if (pstmt != null) pstmt.close();
          if (conn != null) conn.close();
        } catch (SQLException e2) {
          e2.printStackTrace();
        }
      }
      
      return result;
      
    }

    // ...

  }
  ```

## III. JdbcTemplate

### 1) JDBC의 단점 보완
- database와 통신하기 위해서는 매번 driver를 메모리에 로드하고 커넥션 객체를 가져오고 질의응답을 하고 자원을 해제하는 작업을 반복했다.
- Spring에서는 jdbc template을 제공해줌으로써 이 동일한 작업을 반복할 필요가 없어졌다.
  ![](assets/Screen%20Shot%202020-06-28%20at%2010.41.14%20PM.png)

### 2) DataSource 클래스
- 데이터베이스 연결과 관련된 정보를 가지고 있는 DataSource는 스프링 또는 c3p0에서 제공하는 클래스를 이용할 수 있다.
- 스프링
  - `org.springframework.jdbc.datasource.DriverManagerDataSource`
- c3p0 (connection pool 쓸 때 사용)
  - `com.mchange.v2.c3p0.DriverManagerDataSource`

### 3) 사용 방법
- `pom.xml`에 respository 및 dependency 추가
  ```xml
  <repositories>
    <repository>
      <id>oracle</id>
      <name>ORACLE JDBC Repository</name>
      <url>http://maven.jahia.org/maven2</url>
    </repository>
  </repositories>

  <dependencies>
    <!-- ... -->

    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-jdbc</artifactId>
      <version>4.1.6.RELEASE</version>
    </dependency>

    <dependency>
      <groupId>com.mchange</groupId>
      <artifactId>c3p0</artifactId>
      <version>0.9.5</version>
    </dependency>
  </dependencies>
  ```

- `MemberDao.java`
  ```java
  @Component
  public class MemberDao implements IMemberDao {
    
    private String driver = "oracle.jdbc.driver.OracleDriver";
    private String url = "jdbc:oracle:thin:@localhost:1521:xe";
    private String username = "jngcii";
    private String password = "7777";
    
    private DriverManagerDataSource dataSource;

    private JdbcTemplate template;
    
    public MemberDao() {
      dataSource = new DriverManagerDataSource();
      dataSource.setDriverClass(driver);
      dataSource.setJdbcUrl(url);
      dataSource.setUser(username);
      dataSource.setPassword(password);

      template = new JdbcTemplate();
      template.setDataSource(dataSource);
    }
    
    @Override
    public int memberInsert(Member member) {

      int result = 0;
  
      String sql = "INSERT INTO member (memId, memPw, memName) VALUES (?, ?, ?)";
      result = template.update(sql, member.getMemId(), member.getMemPw(), member.getName());
      
      return result;
      
    }

    @Override
    public Member memberSelect(Member member) {

      List<Member> members = null;

      final String sql = "SELECT * FROM member WHERE memId = ? AND memPw = ?";

      members = template.query(sql, new PreparedStatementSetter() {
        @Override
        public void setValues(PreparedStatement arg0) throws SQLException {

        }
      }, new RowMapper<Member>() {
        @Override
        public Member mapRow(ResultSet rs, int rowNum) throws SQLException {
          Member mem = new Member();
          mem.setMemId(memId);
          mem.setMemId(rs.getString("memId"));
          mem.setMemPw(rs.getString("memPw"));
          mem.setMemName(rs.getString("memName"));

          return mem;
        }
      })

      if(members.isEmpty()) return null;

      return members.get(0);

    }

    // ...

  }
  ```
