# Test

###### 2020.07.08

## I. Unit vs Integration
### 1) Unit Test
- 보통 애플리케이션은 여러 모듈들과 컴퍼넌트들로 구성되어져있는데, 특정한 하나의 컴퍼넌트를 고립해서 테스트 하는 것을 Unit Test라고 한다.
- 작은 부분의 코드가 의도대로 동작하는지를 검증하기 위한 테스트이다.
- Unit Test는 애플리케이션 코드가 외부 의존성과 함께 잘 동작하는지 보기 위한 코드가 아니다.
- Unit Test는 하나의 컴퍼넌트에 초점이 맞춰져 있고, 그 컴퍼넌트와 상호작용하는 의존성들의 목업을 만든다.
- 주된 목적은 서로 다른 모듈들이 유저의 요청에 따라 서로 상호작용할 때 발생하는 이슈를 찾기 위함이다.
- REST Controller를 테스트할 때, 각각의 DAO 레이러를 테스트할 때 사용된다.
- Embeded Server가 필요없다.

### 2) Integration Test
- 애플리케이션 전체를 범위로 할 수도 있고, 특정 컴퍼넌트들을 대상으로 할 수 도 있다.
- database instance나 하드웨어 같은 리소스가 필요할 수 있다.
- controller부터 persistence layer까지의 완전한 요청 프로세스를 테스트할 때 사용한다.


## II. Dependencies
- Spring boot 테스트를 위한 가장 좋은 방법은 `pom.xml`에 아래 코드를 포함하는 것이다.
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
    ```

## III. Test Runners
```java
@RunWith(SpringRunner.class)
public class PostControllerTest {
    // test
}
```
- default로 JUnit4가 테스트 의존성으로 사용되고, SpringRunner의 클래스를 인자로 받는 `@Runwith` 어노테이션이 클래스 레이어에 붙는다.


## IV. Spring Boot Test annotations

### 1) `@SpringBootTest`
- 이 어노테이션은 Integrating test에서 사용된다.
- 이 것은 내장서버를 시작하고 애플리케이션 콘텍스트를 완전히 초기화 시작한다.
- `@Autowired`를 통해 테스트에 의존성을 주입할 수 있다.

### 2) `@WebMvcTest`
- Spring MVC를 위한 테스트에 사용된다.
- 모든 자동설정을 해주지 않고, MVC와 관련된 설정만 해준다.
- 또한 MockMvc 인스턴스를 자동설정해준다.
- 딱 하나의 웹컨트럴러의 클래스를 인자로 설정하므로써 해당 컨트럴러에 대해서만 테스트할 수 있다.
    ```java
    @WebMvcTest(EmployeeRESTController.class)
    public class TestEmployeeRESTController {
    
        @Autowired
        private MockMvc mvc;
    
        //
    }
    ```

### 3) `@WebFluxTest`
- 모든 자동설정을 해주지 않고, WebFlux test와 관련된 설정만 해준다.
- 기본적으로 `@WebFluxTest`가 달린 테스트들은 `WebTestClient`가 자동설정된다.
- 보통 컨트럴러 빈객체가 필요로 하는 객체를 생성하기 위해 `@MockBean`이나 `@Import` 어노테이션과 함께 사용된다.
    ```java
    @WebFluxTest(controllers = EmployeeController.class)
    @Import(EmployeeService.class)
    public class EmployeeControllerTest 
    {
        @MockBean
        EmployeeRepository repository;
    
        @Autowired
        private WebTestClient webClient;
    
        //tests
    }
    ```
- 메이븐 의존성 설정
    ```xml
    <dependency>
        <groupId>io.projectreactor</groupId>
        <artifactId>reactor-test</artifactId>
        <scope>test</scope>
    </dependency>
    ```
    or
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
    ```
- `WebTestClient`
  - reactive `WebClient`를 사용하는 **웹 서버**를 테스트하기 위한 non-blocking, reactive `WebClient`이다. (내부적으로 요청을 수행하고 응답을 검증하기 위한 api를 검증)
  - 이것은 HTTP를 기반으로 어떤 서버와도 연결할 수도 있고, HTTP 서버 없이 모킹된 요청/응답 객체를 사용해 웹플럭스와 직접적으로 연동될수도 있다.
- Webflux controller test 예시
    ```java
    @ExtendWith(SpringExtension.class)
    @WebFluxTest(controllers = EmployeeController.class)
    @Import(EmployeeService.class)
    public class EmployeeControllerTest 
    {
        @MockBean
        EmployeeRepository repository;
    
        @Autowired
        private WebTestClient webClient;
    
        @Test
        void testCreateEmployee() {
            Employee employee = new Employee();
            employee.setId(1);
            employee.setName("Test");
            employee.setSalary(1000);
    
            Mockito.when(repository.save(employee)).thenReturn(Mono.just(employee));
    
            webClient.post()
                .uri("/create")
                .contentType(MediaType.APPLICATION_JSON)
                .body(BodyInserters.fromObject(employee))
                .exchange()
                .expectStatus().isCreated();
    
            Mockito.verify(repository, times(1)).save(employee);
        }
    }
    ```
    - `@ExtendWith(SpringExtension.class)` : Junit5로 테스팅하기 위해 사용
    - `@RunWith(SpringRunner.class)` : Junit4로 테스팅하기 위해 사용
- contoller 예시
    ```java
    @RestController
    public class EmployeeController 
    {
        @Autowired
        private EmployeeService employeeService;
    
        @PostMapping(value = { "/create", "/" })
        @ResponseStatus(HttpStatus.CREATED)
        public void create(@RequestBody Employee e) {
            employeeService.create(e);
        }
    ```
##### MockMvc vs WebTestClient
- WebTestClient
  - HTTP를 사용하는 실웹서버 테스트에도 사용될 수 있다.
  - REST 방식을 테스트하기에 매우 용이하다.
  - asynchronous하게 동작하므로 요청을 보내고 기다리지 않는다.
  - 후에 응답이 오면, 콜백 이벤트를 실행할 수 있다.
  - 따라서, Test코드에서도 WebClient와 비슷한 API를 사용할 수 있다.
  - API가 restTemplate보다 가독성이 좋다. (추천)
- MockMvc
  - 내장 Tomcat을 생략한 테스트
  - 서블릿을 Mocking한 것이 구동된다.


### 4) `@DataJpaTest`
- JPA 애플리케이션을 테스트하기 위해 사용될 수 있다.
- 기본적으로 `@Entity` 클래스들을 스캔하고 Spring Data JPA Repository들를 설정한다.
- 만약 클래스패스에 내장 메모리가 있다면 이또한 설정한다.
- 기본적으로 data JPA tests는 `transactional`이고, 각 테스트의 끝에 롤백한다.
- 또한, `TestEntityManager` (test를 위해 디자인된 JPA `EntityManager`) 빈 객체를 주입한다.


### 5) `@RestClientTest`
- REST clients를 테스트하기 위해 사용된다.
- 기본적으로 `Jackson`, `GSON`, `Jsonb support`, `RestTemplateBuilder`, `MockRestServiceServer`를 자동 설정한다.



## V. Mocking

### With Mockito - `@Mock`
- `@Mock`은 목생성을 위해 사용된다.
- 테스트클래스에서 mockito 어노테이션들을 사용하기 우해서는 `MockitoAnnotations.initMocks(testClass)`가 최소한 한번 사용되어야한다. 단, **`@RunWith(MocktoJUnitRunner.class)`를 사용할 경우에는 사용할 필요가 없다.
- Mocks들은 각각의 테스트 메서드 전에 초기화한다.
- `Spring text context`가 필요 없을 때 `@Mock`을 사용해라

### Without Mockito - `@MockBean`
- `@MockBean`은 스프링 애플리케이션컨텍스트에 목을 추가할때 사용된다.
- `@MockBean`은 mockito의 `@Mock`과 비슷하지만 스프링의 support가 있다.
- 보통 `@WebMvcTest`sk `@WebFluxTest`와 함께 사용된다.
- 이 어노테이션들은 개별 컨트럴러에 한정된 슬라이싱 테스트에 사용된다.
- 예시
    ```java
    @WebFluxTest(controllers = EmployeeController.class)
    @Import(EmployeeService.class)
    public class EmployeeControllerTest
    {
        @MockBean
        EmployeeRepository repository;
    
        @Autowired
        private WebTestClient webClient;
    
        //tests
    }
    ```