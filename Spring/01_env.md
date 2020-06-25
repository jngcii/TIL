# 개발 환경 구축

###### 2020.06.25

## I. 프로젝트 생성
1. 이클립스 실행
2. Project Explorer에서 우클릭 New
3. Project
4. Maven - Maven Project
5. Create a simple project, Use default Workspace Location 체크하고 Next
6. groupId : 내가 만들고 있는 프로젝트를 감싸는 큰 프로젝트 (ex. com.javastudy)
7. artifactId : 현재 프로젝트 이름 (ex. testPRJ)
8. packaging : jar / war (자바프로젝트 / 웹프로젝트)

## II. `pom.xml` 작성
> 필요한 모듈을 가져오기 위한 파일
```xml
<dependencies>
  <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>4.1.0.RELEASE</version>
  </dependency>
</dependencies>
```
```xml
<build>
  <plugins>
    <plugin>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>3.1</version>
      <configuration>
        <source>1.8</source>
        <target>1.8</target>
        <encoding>utf-8</encoding>
      </configuration>
    </plugin>
  </plugins>
</build>
```
- 여기에 적어놓은 라이브러리와 의존관계에 있는 라이브러리 모두 Maven Dependencies 디렉터리에서 확인할 수 있다.

## III. Spring 프로젝트의 구조
- `src/main/java`
  - 실제 자바 언어를 통해 프로그래밍, 기능구현을 하는 부분
- `src/main/resources`
  - 자바 프로그래밍에 있어서 보조적인 역할의 파일들이 모여있는 부분
  - 스프링 설정 파일(XML) 또는 프로퍼티 파일 등