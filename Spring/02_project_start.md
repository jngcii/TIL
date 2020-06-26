# Start Project

###### 2020.06.25

## I. 작은 프로젝트
1. 메이븐으로 프로젝트시작
    - 이클립스에서 생성할 수도 있고, 로컬에서 메이븐을 통해 만들고 import할 수도 있다.
2. `pom.xml` 작성
3. `/src/main/resources/applicationContext.xml` 생성
    - 이 파일은 스프링이 사용할 객채(Bean)를 만들어주는 역할을 하는 파일
    1. `src/main/resources/`에서 우클릭 New -> XML -> XML file
    2. 파일 이름 : applicationContext.xml (사실 마음대로 해도 됌)
    3. 작성
      ```xml
      <?xml version="1.0" encoding="UTF-8"?>
      <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.springframework.org/schema/beans
              http://www.springframework.org/schema/beans/spring-beans.xsd">

          <bean id="tWalk" class="testPRJ.TransportationWalk" />
      </beans>
      ```
4. `TransportationWalk`, `Main` 자바 클래스 파일 생성
    - 그냥 프로젝트 폴더에서 New -> Class 로 생성하면 적절한 위치(`/src/main/java/`))로 들어간다. (그러면 프로젝트이름의 패키지가 생성되고 그 안에 자바 파일이 생성된다.)
    - `TransportationWalk.java`
      ```java
      package testPRJ;

      public class TransportationWalk {

          public void move() {
              System.out.println("도보로 이동합니다.");
          }

      }
      ```
    - `Main.java`
      ```java
      package testPRJ;

      import org.springframework.context.suppert.GenericXmlApplicationContext;

      public class Main {
          public static void main(String[] args) {

              GenericXmlApplicationContext ctx = new GenericXmlApplicationContext("classpath:applicationContext.xml");

              TransportationWalk transportationWalk = ctx.getBean("tWalk", TransportationWalk.class);

              transportationWalk.move();

              ctx.close();

          }
      }
      ```
      - GenericXmlApplicationContext : 컨테이너에 접근하는 방법 - 인자로 리소스를 적어준다.
      - ctx를 통해 모든 객체(Bean)에 접근할 수 있다.
      - 자바에서는 리소스를 사용하면 반환해주어야 한다. (`ctx.close()`)