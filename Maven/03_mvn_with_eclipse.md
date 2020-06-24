# 메이븐 프로젝트 이클립스에서 로드(임포트)하기

###### 2020.06.24

## I. Maven 프로젝트 임포트 및 실행

1. [File] - [Import] - [Maven] - [Existing Maven Projects]
2. [Browse] - 만든 프로젝트 디렉터리 선택 - [Finish]
3. 실행

## II. 컴파일 플러그인과 JDK 버전 변경하기
1. `pom.xml` 편집
    ```xml
    ...
    <dependencies>
      ...
    </dependencies>

    <!-- 아래 추가 -->
    <!-- <properties>
      <maven.compiler.source>1.8</maven.compiler.source>
      <maven.compiler.target>1.8</maven.compiler.target>
    </properties> -->
    <build>
      <plugins>
        <plugin>
          <artifactId>maven-compiler-plugin</artifactId>
          <version>3.8.1</version>
          <configuration>
            <source>1.8</source>
            <target>1.8</target>
          </configuration>
        </plugin>
      </plugins>
    </build>
    ```
2. 프로젝트 폴더에서 우클릭 -> Maven -> Update Project