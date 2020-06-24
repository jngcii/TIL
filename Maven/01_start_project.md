# Start Project

###### 2020.06.24

## I. 프로젝트 생성

1. 작업 디렉터리로 이동
2. 프로젝트 시작
    - `mvn archetype:generate -DgroupId=com.jngcii -DartifactId=testprj -DarchetypeArtifactId=maven-archetype-quickstart`
    - 이클립스로 프로젝트를 시작하면 빈 프로젝트(맨 땅)에서 시작하는 반면 메이븐으로 프로젝트를 시작하면 기본 골격을 가진 상태로 만들 수 있다.
    - 그 골격의 종류를 정할때 `-DarchetypeArtifactId`를 사용한다.
      > - DarchetypeArtifactId 종류
      >   - maven-archetype-quickstart
      >   - maven-archetype-webapp
    - `-DartifactId`에는 생성할 프로젝트 이름을 입력한다.
    - `-DgroupId` : 프로젝트의 이름이 많이 겹칠수 있기 때문에 그걸 구분하기 위해 자신만의 고유한 패키지와 같은 groupId를 사용한다.
3. 여기까지 하면 프로젝트 폴더 및 구조 생성완료

## II. 컴파일과 실행
> 이클립스 없이 메이븐으로 컴파일도 하고 실행도 할 수 있다.
1. 컴파일
     - `src/`와 `pom.xml`이 있는 루트 디렉터리에서 `mvn compile` 입력하면 컴파일이 실행됨
     - 여기서 `Source option 5 is no longer supperted. Use 7 or later`라는 에러가 발생한다.
2. `pom.xml` 편집
    ```xml
    ...
    <dependencies>
      ...
    </dependencies>

    <!-- 아래 추가 -->
    <properties>
      <maven.compiler.source>1.8</maven.compiler.source>
      <maven.compiler.target>1.8</maven.compiler.target>
    </properties>
    ```
    > source : 우리가 컴파일하는 것이 1.8 버전으로 컴파일됐으면 좋겠다.
    > target : 대상을 최소 1.8 이상 버전에서 컴파일되도록 수행하겠다.
3. 다시 컴파일 하면 성공
4. `/target/classes/com/jngcii/App.class`가 생성된 것을 확인할 수 있다. 
5. ( 패키지화 하는 법 : `mvn package` )
6. ( 패키지화된 jar 파일로 실행하기 : `java -cp target\testprj-1.0-SNAPSHOT.jar com.jngcii.App` )