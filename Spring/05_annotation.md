# 어노테이션을 이용한 스프링 설정

###### 2020.06.26

> xml이 아닌 스프링 설정파일 제작을 java파일로 제작할 수 있는 방법

## I. xml파일을 java파일로 변경하기

- `MemberConfig.java` 작성 (설정을 위한 새로운 패키지)
  ```java
  package ems.member.confiuration;

  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;

  import ems.member.dao.StudentDao;
  import ems.member.service.StudentRegisterService;

  @Configuration
  public class MemberConfig {

      // <bean id="studentDao" class="ems.member.dao.StudentDao" />
      @Bean
      public StudentDao studentDao() {
          return new StudentDao();
      }
      // bean의 id와 method명이 같아야한다.
      
      // 생성자 사용 빈객체 등록
      // <bean id="registerService" class="ems.member.service.StudentRegisterService"><constructor-arg ref="studentDao" /></bean>
      @Bean
      public StudentRegisterService registerService() {
          return new StudentRegisterService(studentDao());
      }

      // setter사용 빈객체 등록
      @Bean
      public DataBaseConnectionInfo dataBaseConnectionInfo() {
          DataBaseConnectionInfo infoDev = new DataBaseConnectionInfo();
          infoDev.setJdbcUrl("jdbc:oracle:thin:@localhost:1521:xe");
          infoDev.setUserId("jngcii");
          infoDev.setUserPw("mypassword");
      }

      // List, Map 타입의 setter사용 빈객체 등록
      @Bean
      public EMSInformationService informationService() {
          EMSInformationService info = newEMSInformationService();

          // 여기는 그냥 String타입 받는 setter
          info.setInfo("Education Management System");

          // List 타입의 seter
          ArrayList<String> developers = new ArrayList<String>();
          developers.add("developer A");
          developers.add("developer B");
          developers.add("developer C");

          info.setDevelopers(developers);

          Map<String, String> admins = new HashMap<String, String>();
          admins.put("developer A", "a@ex.com");
          admins.put("developer B", "b@ex.com");

          info.setAdministrators(admins);
      }

  }
  ```

- `Main.java` 작성 (설정파일 가져와서 사용하는 곳)
  ```java
  class Main {

      public static void main(String[] args) {

          // ...

          AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(MemberConfig.class);

          // ...
      }

  }
  ```

## II. java 파일 분리하기
- `MemberConfig.java` 파일을 1, 2, 3으로 나눈다.
- 하나의 Config에서 다른 Config파일의 메서드 참고하는 방법
- `MemberConfig2.java`
  ```java
  @Configuration
  public class MemberConfig2 {

      @Bean
      public DataBaseConnectionInfo dataBaseConnectionInfoDev() {
          DataBaseConnectionInfo infoDev = new DataBaseConnectionInfo();
          infoDev.setJdbcURL("jdbc:oracle:thin:@localhost:1521:xe");
          infoDev.setUserId("jngcii");
          infoDev.setUserPw("mypassword");
      }

      @Bean
      public DataBaseConnectionInfo dataBaseConnectionInfoReal() {
          DataBaseConnectionInfo infoReal = new DataBaseConnectionInfo();
          infoDev.setJdbcURL("jdbc:oracle:thin:@192.168.0.1:1521:xe");
          infoDev.setUserId("jngcii");
          infoDev.setUserPw("mypassword");
      }

  }
- `MemberConfig3.java`
  ```java
  @Configuration
  public class MemberConfig3 {

      @Autowired
      DataBaseConnectionInfo dataBaseConnectionInfoDev;

      @Autowired
      DataBaseConnectionInfo dataBaseConnectionInfoReal;

      @Bean
      public EMSInformationService informationService() {

          EMSInformationService info = new EMSInformationService();

          // ...

          Map<String, DataBaseConnectionInfo> dbInfos = new HashMap<String, DataBaseConnectionInfo>();
          dbInfos.put("dev", dataBaseConnectionInfoDev);
          dbInfos.put("real", dataBaseConnectionInfoReal);

          return info;
      }

  }
  ```
- `Main.java`
  ```java
  //...

  AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(MemberConfig1.class, MemberConfig2.class, MemberConfig3.class);

  //...
  ```

## III. `@Import` 어노테이션
> Config파일 1번에서 2번과 3번 import
- `MemberConfig1.java`
  ```java
  @Configuration
  @Import({MemberConfig2.class, MemberConfig3.class})
  public class MemberConfig1 {

      // ...

  }
  ```
- `Main.java`
  ```java
  //...

  AnnotationConfigApplicationContext ctx = new AnnotationConfigApplicationContext(MemberConfig1.class);

  //...
  ```