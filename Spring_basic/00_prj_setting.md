# 프로젝트 세팅

###### 2020.06.23

### 1) JDK version
- 1.8 (9, 10은 x)

### 2) 소스 코드
- https://github.com/spring-projects/spring-petclinic

### 3) IDE
- IntelliJ (커뮤니티 버전도 OK)
  - open으로 프로젝트 열기
  - 처음엔 자바 버전을 확인하고 바꿔야 한다.
  - `cmd + ;` -> jdk1.8 + 8 - lambdas ... 으로 변경
  - modules -> dependencies -> module sdk를 jdk1.8로 변경

### 4) 주의할 점
- 현재 wro4j 메이븐 플러그인이 Java9 이상을 지원하지 않는다.

### 5) 실행 방법
- mvnw spring-boot:run 또는 IDE에서 메인 애플리케이션 실행

### 6) 프로젝트 구조
- 일반적인 메이븐 프로젝트
- 스프링 부트 기반 프로젝트