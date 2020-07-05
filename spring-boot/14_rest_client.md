# 스프링 Rest 클라이언트
> RestTemplate과 WebClient

###### 2020.07.05

- RestClient는 스프링에서 제공해주는 것이고, 스프링부트는 RestClient를 쉽게 사용할 수 있도록 빈을 등록해준다.
- 다만 아래 두타입의 빈을 등록해 주는 것이 아니고, RestTemplate builder, WebClient.builder를 등록해준다.

## I. RestTemplate
- Blocking I/O 기반의 Synchronous API
- RestTemplateAutoConfiguration
- 프로젝트에 spring-web 모듈이 있다면 RestTemplateBuilder를 빈으로 등록해준다.
### 1) 사용법
- `SampleController.java` 작성
    ```java
    @RestController
    public class SampleController {

        @GetMapping("/hello")
        public String hello() throws InterruptedException {
            Thread.sleep(5000l);
            return "hello";
        }

        @GetMapping("/world")
        public String world() throws InterruptedException {
            Thread.sleep(3000l);
            return "world";
        }
    }
    ```
- `RestRunner.java`
    ```java
    @Component
    public class RestRunner implements ApplicationRunner {

        @Autowired
        RestTemplateBuilder restTemplateBuilder;

        @Override
        public void run(ApplicationArguments args) throws Exception {
            RestTemplate restTemplate = restTemplateBuilder.build();

            StopWatch stopWatch = new StopWatch();
            stopWatch start();

            // TODO /hello
            String helloResult = restTemplate.getForObject("http://localhost:8080/hello", String.class);
            System.out.println(helloResult);

            // TODO /world
            String worldResult = restTemplate.getForObject("http://localhost:8080/world", String.class);
            System.out.println(worldResult);

            stopWatch.stop();
            System.out.println(stopWatch.prettyPrint());
        }

    }
    ```

### 2) 커스터마이징
- `SpringBootRestApplication.java`
    ```java
    public static void main(String[] args) {
        // ...
    }

    @Bean
    public WebClientCustomizer webClientCustomizer() {
        return new WebClientCustomizer() {
            @Override
            public void customize(WebClient.Builder webClientBuilder) {
               webClientBuilder.baseUrl("http://localhost:8080");
            }
        };
    }
    ```
- `

## II. WebClient
- Non-Blocking I/O 기반의 Asynchronous API
- WebClientAutoConfiguration
- 프로젝트에 spring-webflux 모듈이 있다면 WebClient.Builder를 빈으로 등록해준다.
- 자바스크립트랑 비슷하게 동작한다. (subscribe 함수를 사용해주면 콜백을 실행... ?)