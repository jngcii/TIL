# 의존성 관리

###### 2020.07.02

## I. 의존성을 추가하는 방법
> spring-data-jpa를 추가해보자
- `pom.xml
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    ```
    > version은 명시해줄 필요가 없다. (parent로 상속받은 것이기 때문이다.)
- IntelliJ 오른쪽 탭의 `Maven`에서 확인 가능