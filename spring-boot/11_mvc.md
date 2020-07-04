# Spring MVC

###### 2020.07.04


## I. 간단한 Controller와 Test 작성해보기

1. Spring Boot 프로젝트 시작
2. 간단한 테스트 만들기
    - `test/java/com/jngcii/user/UserControllerTest.java`
        ```java
        @RunWith(SpringRunner.class)
        @WebMvcTest(UserController.class)   // slicing test (웹 계층만 테스트하는 것)
        public class UserControllerTest {

            @Autowired
            MockMvc mockMvc;        // 웹 mvc test를 만들 때 주로 사용하는 객체
                                    // @WebMvcTest라는 어노테이션을 사용하면 자동으로 빈에 등록된다.

            @Test
            public void hello() throws Exception {
                mockMvc.perform(get("/hello")).andExpect(status().isOk()).andExpect(content().string("hello jngcii"));
            }

        }
        ```
        - 자동 import나 틀린 문장을 고치기 위한 명령 단축키 : `cmd + 1`
        - Run test : `ctrl + shift + r`
        - test code 작성 : `cmd + shift + t`
        - getter + setter 작성 : `ctrl + enter`


## II. HttpMessageConverters
- 스프링 프레임워크에서 제공하는 인터페이스
- spring mvc의 일부분
- HTTP 요청 본문으로 들어오는 것을 객체로 변환하거나, 객체를 HTTP 응답 본문으로 변환할 때 사용한다.
- 보통 `@RequestBody`, `@ResponseBody`와 함께 사용된다.
    ```java    
    @RestController
    public class UserController {

        @GetMapping("/hello")
        public String hello() {
            return "hello jngcii";
        }

        @PostMapping("/user")
        public @ResponseBody User create(@RequestBody User user) {
            return user;
        }

    }
    ```
    - 이럴 때 HttpMessageConverters가 사용된다.
    - HttpMessageConverters는 여러가지가 있는데, 그중에서 우리가 어떤 요청을 받았고 어떤 응답을 보내야하는지에 따라 사용되는 HttpMessageConverters가 달라진다.
    - 예를들어, 요청이 json 요청이고 (`ContentType`이 `application/json`) json 본문이 들어왔다면 json message converter가 사용이 돼서 json 메세지를 User라는 객체로 변환해준다.
    - 응담의 경우에도 위와같이 User(컴퍼지션 타입)일 경우에는 기본적으로 json message converter가 사용되지만, String으로 리턴하거나 간단할 경우에는 각 리턴 타입에 맞는 message converter가 사용된다.
    - `@RestController` 어노테이션을 붙일 경우에는 `@ResponseBody`를 생략할 수 있다. (`@RequestBody`는 생략 불가)

## III. 정적 리소스 지원
- 정적 리소스 매핑
  - 기본 리소스 위치
    - classpath: `/static`
    - classpath: `/public`
    - classpath: `/resources`
    - classpath: `/META-INF/resources`
    - spring.mvc.static-path-pattern: 매핑 설정 변경 가능
    - spring.mvc.static-locations: 리소스 찾을 위치 변경 가능

## IV. Cross Origin
- 다른 origin에서 오는 요청은 받을 수 없다.
- 이걸 가능하게 하는 방법
    1. 각 mapping method 혹은 controller class에 붙여주기
        - 원하는 자바 파일
            ```java
            @CrossOrigin(origins = "http://192.168.0.3:8088")
            @GetMapping("/hello")
            public String hello() {
                return "hello":
            }
            ```
    2. 모든 경로에 붙여주기
        - `WebConfig.java`
            ```java
            @Configuration
            public class WebConfig implements WebMvcConfigurer {

                @Override
                public void addCorsMapping(CorsRegistry registry) {
                    registry.addMapping("/**")
                        .allowedOrigins("*");
                }

            }
            ```