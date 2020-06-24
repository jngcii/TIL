# IoC Container

###### 2020.06.23

- 스프링은 IoC용 컨테이너를 제공해준다.
  - 컨테이너의 가장 핵심적인 인터페이스 : ApplicationContext (BeanFactory)
- 아이러니하게도 직접 쓸 일은 많지 않다.
- 그럼 도대체 얜 뭐냐?
  - 얘는 제어역전 코드를 동작하게 만들어준다.
  - ex) OnwerController가 IoC Container 내부에 들어오고 IoC Container 내부에서 OnwerController 객체를 만들어준다. 그리고 OwnerRepository의 객체도 만들어주고 (빈과 관련됨) 자기가 Container 내부에 만든 객체들(빈이라 불림)의 의존성을 관리해준다.
  - 오로지 빈만 관리한다.
  - `@Controller`, `@Service` 등의 어노테이션이 붙어있으면 자동으로 빈으로 등록이 된다. (컴퍼넌트 스캔이라는 방법)
- 빈(bean)을 만들고 엮어주며 제공해준다. (의존성을 관리해준다.)
- 빈 설정
  - 이름 또는 ID
  - 타입
  - 스코프

# 빈 (Bean)

- 스프링 IoC 컨테이너가 관리하는 객체
- 어떻게 등록하나?
  - Component Scanning
    - 스프링부트로 만든 애플리케이션은 대부분 @SpringBootApplication이라는 어노테이션을 갖은 클래스가 하나 있다. (베스트프렉티스는 기본 패키지 루트에 있는 것)
    - 해당 클래스의 어노테이션(@SpringBootApplication)을 따라가보면 @ComponentScan이라는 어노테이션이 붙은 것을 확인할 수 있다.
    - 이 @ComponentScan이라는 어노테이션은 이 @ComponentScan 어노테이션을 처리하는 핸들러(프로세서)가 본인의 역할을 하게끔한다.
    - 역할 : @Component 어노테이션이 붙은 클래스를 찾아서 빈으로 등록을 해준다.
      - 어노테이션은 기능이 없다. 다만 어노테이션을 마커로 해서 처리하는 프로세서들이 있는 것
    - @Component
      - @Repository
      - @Service
      - @Controller
  - 또는 직접 일일이 xml이나 자바 설정 파일에 등록
    - @SpringBootApplication이 붙은 클래스에 직접 작성
    - 예시
      ```java
      @SpringBootApplication
      public class PetClinicApplication {

        @Bean
        public String jngcii() {
          return "jngcii";
        }

        public static void main(String[] args) {
          SpringApplication.run(PetClinicApplication.class, args);
        }
      }
      ```
      - 메서드 이름이 빈의 이름이 된다.
      - 다만 @Configuration이라는 어노테이션이 붙은 클래스에만 작성할 수 있다.
      - @SpringBootApplication 어노테이션을 따라가다 보면 @Configuration이라는 어노테이션을 찾을 수 있다.
- 어떻게 꺼내 스나?
  - @Autowired 또는 @Inject
    - 예시
      ```java
      @RestController
      public class SampleController {

        @Autowired
        String jngcii;

        @GetMapping("/jngcii");
        public String context() {
          return "hello " + jngcii;
        }

      }
      ```
  - 또는 ApplicationContext에서 getBean()으로 직접 꺼내기
- 특징
  - 