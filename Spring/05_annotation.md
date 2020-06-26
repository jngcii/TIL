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