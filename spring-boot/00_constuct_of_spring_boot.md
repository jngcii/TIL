# Spring Boot의 구성

###### 2020.07.02

- 스프링부트는 프로덕션 환경에서 실행할 수 있는 애플리케이션 개발을 쉽게 빠르게 할 수 있다.
- 서드파티 라이브러리나 스프링 플랫폼 설정이 처음부터 들어있어, 최소한의 작업으로 개발을 시작할 수 있다.
- 설정을 변경하지 않는다면 내장된 컨테이너로 톰캣을 사용해 미리 준비된 환경에 따라 동작한다. 
- 명령줄에 `java -jar` 명령의 파라미터로 작성한 jar파일을 지정하면 내장된 톰캣이 실행된 후, 개발한 애플리케이션이 실행된다.

## I. 스프링부트 기초

### 1) 스프링부트란?
- 스프링부트 그 자체로 완전한 프레임워크는 아니다.
- 스프링 MVC 프레임워크를 사용한다. (Model, View, Controller)
- 스프링은 스프링 MVC와 스프링 배치 등의 다양한 프레임워크를 조합해 신속하고 간단하게 애플리케이션을 개발할 수 있다.

### 2) 스프링부트의 대표적인 특징

#### (1) 스타터
- 의존관계를 간단하게 정의하는 모듈 (세트로 정리)
- 필요한 라이브러리를 준비하거나 각각의 라이브러리 버전을 선정하는 번거로운 작업에서 해방
- 예를들어 `spring-boot-starter-web`이라는 하나의 의존관계를 추가하기만 하면 스프링 MVC 또는 톰캣 등 웹 애플리케이션에 필요한 라이브러리가 함께 추가된다.
  - `spring-boot-starter-web` : 스프링 MVC, 톰캣이 의존관계에 추가된다.
  - `spring-boot-starter-jdbc` : 스프링 JDBC, 톰캣 JDBC 커넥션 풀이 의존관계에 추가된다.
- 독자적인 스타터 만드는 법
  - `*-spring-boot-starter`라는 명명 규칙 사용

#### (2) 빌드 도구
- Gradle 혹은 Maven 사용 권장
- 스프링부트는 일반적인 자바 라이브러리와 마찬가지로 클래스 경로에 spring-boot-*.jar를 포함하여 이용할 수도 있지만 의존관계 관리가 가능한 빌드 도구를 이용하는 것이 좋다.
- 빌드 도구로 메이븐을 이용하려면 `spring-boot-starter-parent` 프로젝트를 상속한다. 그러면 플러그인의 default 설정, 의존 라이브러리의 버전 정의, 자바 컴파일러 준수 레벨, unicode를 이어받을 수 있다.
  ```xml
  <!-- Inherit defaults from Spring boot -->
  <parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.0.6.RELEASE</version>
  </parent>
  ```
- 자바 컴파일러 준수 레벨의 디폴트 값은 1.8이다. 버전 11로 변경하려면 다음 속성 태그를 `pom.xml` 파일에 작성하여 디폴트 값을 덮어 쓰면 된다. (하지만 왠만하면 default 값 사용)
  ```xml
  <properties>
    <java.version>11</java.version>
  </properties>
  ```

#### (3) 구성 클래스
- 스프링 부트는 자바 기반으로 구성하는 것을 선호한다.
- `@Configuration` 어노테이션을 부여한 클래스로 작성하는 것을 권장한다.
- 받스히 하나로 만들 필요는 없으며 `@import`를 사용해 다른 구성을 로드할 수도 있다.
  >JavaConfig로 구성하기
  ```java
  // 디폴트 설정을 위해 아무것도 하지 않는다.
  @Configuration
  public class ApplicationConfig implements WebMvcConfigurer {

  }

  @SpringBootApplication(scanBAsePackages = { "com.sample.web" })
  public class Application {
      public static void main(String[] args) {
          SpringApplication.run(Application.class, args);
      }
  }
  ```

#### (4) 자동 구성
- 스프링 부트는 설정을 변경하지 않으면 미리 정해진 디폴트 설정에 따라 동작한다. (자동 구성 기능이 디폴트 동작을 설정)
- 의존관계에 `HSQLDB` 라이브러리를 추가한 상태에서 데이터베이스에 대한 접속 설정을 정의하지 않으면, 내장형 인메모리 데이터베이스를 데이터 소스로 사용하도록 자동으로 설정된다.
- 자동구성을 사용하려면 `@EnableAutoConfiguration` 또는 `@SpringBootApplication` 어노테이션을 부여한다.
- 특정 자동 구성을 비활성화라려면 `@EnableAutoConfiguration` 어노테이션의 속성에서 제외한 구성 클래스를 지정한다.
  ```java
  import org.springframework.boot.autoconfigure.*;
  import org.springframework.boot.autoconfigure.jdbc.*;
  import org.springframework.context.annotation.*;

  @Configuration
  @EnableAutoConfiguration(exclude = { DataSourceAutoConfiguration.class })
  public class MyConfiguration {

  }
  ```

#### (5) 메인 애플리케이션 클래스
- 메인 애플리케이션 클래스는 스프링 부트의 애플리케이션을 실행하는 메서드를 호출한다.
- 자바 애플리케이션의 엔트리 포인트인 main메서드 안에서 `SpringApplication` 클래스의 `run` 메서드를 호출하면 내장된 톰캣이 실행되고 `IoC` 컨테이너가 초기화된다.
- 메인 애플리케이션 클래스는 default 패키지가 아닌 루트 패키지에 배치할 것을 권장한다.
- 자동으로 구성에 의해 `@EnableAutoConfiguration`이 부여된 클래스의 패키지를 기준으로 동작하기 때문이다.
  ```
  com
    sample
        web
            Application.java
            domain
                entity
                    Customer.java
                dao
                    CustomerDao.java
                repository
                    CustomerRepository.java
                service
                    CustormerService.java
            controller
                CustomerForm.java
                CustomerController.java
  ```
- 루트 패키지에 메인 애플리케이션 클래스르 배치함으로써 `@ComponentScan`의 `basePackage` 속성을 명시적으로 지정할 필요는 없지만, `scanBasePackageClasses` 속성에는 컴포넌트 스캔의 기준 패키지에 배치한 클래스를 지정할 것을 권한한다.
  - 리팩토링이 쉬워진다.
  - 기준 패키지가 어떤 패키지인지 쉽게 알 수 있다.
- 스프링부트를 사용하는 애플리케이션에는 메인 애플리케이션 클래스에 대부분 `@Configuration`, `@EnableAutoConfiguration`, `@ComponentScan` 을 지정한다.
- **이를 대신하는 어노테이션은 `@SpringBootApplication`이다.**
  ```java
  package com.sample.web;

  import org.springframework.boot.*;
  import org.springframework.boot.autoconfigure.*;
  import org.springframework.stereotype.*;
  import org.springframework.web.bind.annotation.*;

  import com.sample.ComponentScanBasePackage;   //  상위 컴퍼넌트를 스캔의 기준으로 한다.
  
  @SpringBootApplication(scanBasePackageClasses = {ComponentScanBasePackage.class})
  @RestController   // 원래 컨트롤러에 작성할 어노테이션
  public class Application {

      @RequestMapping("/")  // 원래 컨트롤러에 작성할 메서드
      public String hello() {
          return "Hello World!";
      }

      public static void main(String[] args) {
          SpringApplication.run(Application.class, args);
      }
  }
  ```
  ```java
  package com.sample;

  /*
   * 컴퍼넌트 스캔의 basePackages를 설정한다.
   */
  public class ComponentScanBasePackage {}
  ```

#### (6) 설정 파일
- 애플리케이션을 실행하면 다음 위치에 있는 `application.properties` 설정 파일을 읽어 들인다.
    1. 현재 디렉터리의 `/config` 서브 디렉터리
    2. 현재 디렉터리
    3. 클래스 경로의 `/config` 패키지
    4. 클래스 경로의 루트
- 여러 설정 파일이 존재할 때는 순위가 우선인 설정값으로 덮어 씌인다.
- 설정 파일은 **프로파일**이라는 단위로 별도의 설정을 가진다.
- 개발 환경, 프로덕션 환경 등 환경별로 설정을 나누고 싶을 때는 `application-{profile}.properties`의 명명규칙으로 설정 파일을 만든다.


## II. 웹 애플리케이션 개발
- 웹 애플리케이션을 개발할 때는 로컬 환경에서 애플리케이션을 실행해 동작을 확인하며 작업한다.
- 자바의 소스 코드를 변경할 때는 동작 확인을 위해 빌드를 새로 하고 애플리케이션을 다시 실행하는 절차를 반복한다.
- 웹 애플리케이션이란 다양한 기능을 조합해서 구축한 것인데, 스프링 MVC/부트는 클라이언트에 표시되는 부분인 **프레젠테이션 계층**만 제공한다.
- 데이터베이스 사용에 필요한 각종 기능을 위해 `Spring Data JPA`(SQL) 혹은 `Spring Data MongoDB`(noSQL) 필요
- View와 Controller는 단순히 구조를 만들 뿐 실제 화면 표시 등을 설계할 때는 **템플릿 엔진**이라는 기술을 이해해야 한다.