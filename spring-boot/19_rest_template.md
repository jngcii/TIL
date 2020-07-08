# RestTemplate

###### 2020.07.06

- Spring 3 부터 지원 되는 REST API 호출 이후 응답을 받을 때까지 기다리는 프레임워크

## I. 주요 메서드
| 메서드 | HTTP | 설명 |
| --- | --- | --- |
|getForObject | GET | 주어진 URL 주소로 GET 요청을 보내고, 결과를 객체로 반환받는다. |
|getForEntity | GET | 주어진 URL 주소로 GET 요청을 보내고, 결과를 ResponseEntity로 반환받는다. |
|postForLocation | POST | 주어진 URL 주소로 POST 요청을 보내고, 결과를 헤더에 지정된 URI로 반환받는다. |
|postForObject | POST | 주어진 URL 주소로 POST 요청을 보내고, 결과를 객체로 반환받는다. |
|postForEntity | POST |  주어진 URL 주소로 POST 요청을 보내고, 결과를 ResponseEntity로 반환받는다. |
|delete | DELETE | 주어진 URL 주소로 DELETE 요청을 보낸다. |
|headForHeaders | HEADER | 헤더의 모든 정보를 얻을 수 있다면 HTTP HEAD 메서드를 사용한다. |

## II. 개발 환경
- 스프링 부트 환경에서 `pom.xml`에 `spring-boot-starter-web`이 추가 되어있으면 자동 설정 완료

## III. Shortcut
```java
MultiValueMap<String, String> headers = new LinkedMultiValueMap<String, String>();
Map map = new HashMap<String, String>();
map.put("Content-Type", "application/json");

headers.setAll(map);

Map req_payload = new HashMap();
req_payload.put("name", "piyush");

HttpEntity<?> request = new HttpEntity<>(req_payload, headers);
String url = "http://localhost:8080/xxx/xxx/";

ResponseEntity<?> response = new RestTemplate().postForEntity(url, request, String.class);
ServiceResponse entityResponse = (ServiceResponse) response.getBody();
System.out.println(entityResponse.getData());
```