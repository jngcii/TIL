# Build LifeCycle과 Phase들

###### 2020.06.24

## I. Maven 명령어들
- `mvn compile`
- `mvn test`
- `mvn package`

## II. Maven 수행 단계 (Phase)
```xml
<phases>
  <phase>validate</phase>
  <phase>initialize</phase>
  <phase>generate-sources</phase>
  <phase>process-sources</phase>
  <phase>generate-resources</phase>
  <phase>compile</phase>
  <phase>process-classes</phase>
  <phase>generate-test-sources</phase>
  <phase>process-test-sources</phase>
  <phase>generate-test-resources</phase>
  <phase>process-test-resources</phase>
  <phase>test-compile</phase>
  <phase>process-test-classes</phase>
  <phase>test</phase>
  <phase>prepare-package</phase>
  <phase>package</phase>
  <phase>pre-integration-test</phase>
  <phase>integration-test</phase>
  <phase>post-integration-test</phase>
  <phase>verify</phase>
  <phase>install</phase>
  <phase>deploy</phase>
</phases>
```
- 위 단계가 메이븐의 수행 단계이다.
- 특정 단계를 실행하면 처음부터 해당 단계까지 수행된다.
- compile를 실행하면 처음부터 compile 단계까지 수행되고, package를 수행하면 처음부터 package 단계까지 수행된다.
- 위 단계는 처음 프로젝트를 시작할 때, 웹 개발을 할지 / 자바 개발을 할지 등에 따라 조금씩 다를 수 있지만 일반적으로 대부분 비슷하다.
- packaging할 때 `pom.xml`에 정의되어 있는 형식으로 패키징한다.
- 모든 단계는 각기 다른 프로그램(**플러그인**)이 실행한다.
- 처음 (jar를 만드는) 자바프로젝트를 메이븐으로 만들면 기본적으로 (아무 설정을 안해도) 아래 단계에 대한 플러그인이 매핑이 된다.
  - process-resources
  - compile
  - process-test-resources
  - test-compile
  - test
  - package
- 각 단계마다 설정되어 있는 플러그인을 교체하거나 설정하거나 뺄 수도 있다.
- 각 단계의 플러그인을 내부적으로 구성하고 있는 프로그램들이 작게 나뉘어져 있는데 그 것을 **골**이라고 한다.
- 어떠한 단계를 실행하면서 플러그인을 기술할 수 있도록 할 수 있다.
  - `mvn help:describe -Dcmd=compile`
  - `https://maven.apache.org/plugins/index.html`에 접속하면 각 단계에서 사용될 수 있는 플러그인을 볼 수 있다.