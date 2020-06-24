# 웹 프로젝트

###### 2020.06.24

## I. 웹 프로젝트로 변경
- 프로젝트 모델을 jar에서 war로 바꾸면 그냥 웹 프로젝트가 만들어진다.
- 자바 프로젝트에서 웹 프로젝트로 바꾸기 위한 모델의 변화르 메이븐이 알아서 해준다.
- `pom.xml`의 `<packaging>jar</packaging>`의 jar를 war로 변경하고 `Update Project`
- 그럼 웹개발을 위한 디렉터리 구조로 자동으로 바뀐다.
- 그리고 `web.xml`이 없다는 에러가 뜬다.
- `src\main\webapp\WEB-INF\web.xml` 생성 혹은 `톰캣디렉터리\webapps\ROOT\WEB-INF\web.xml` 복사
- 톰캣 서버 설정해주기

## II. 라이브러리 설정
1. `javax.servlet.http.HttpServlet`을 찾을 수 없다.
2. `pom.xml` 수정
    ```xml
    ...
    <dependencies>
      <dependency>
        ...
      </dependency>
      ...
    </dependencies>
    ```
    - 메이븐은 내가 필요한 라이브러리가 있다고 여기에 설정만 해 주면 알아서 다운로드 한다.
    - `http://search.maven.org/#browse`에서 라이브러리 검색 가능
    - 검색해서 붙여 넣기
    - 메이븐으로 설치된 라이브러리는 `C:\사용자\jngcii\.m2\repository\org\apache\tomcat`에 들어가면 볼 수 있다.

## III. 라이브러리 오류
- ClassNotFoundException이 발생했다고 하는데 라이브러리가 이미 다운로드 완료됐다고 하고 메이븐 업데이트해봐도 전혀 문제 없다고하고 그런데 문제가 발생하고...
- 이건 라이브러리를 다운받다가 깨진 현상인데 라이브러리 설치 경로로 가 보면 해당 jar 파일의 크기가 0~1kb면 깨진 것이다.
- 만약 깨진거면 `/Java Resources/Libraries/Maven Dependencies/`의 jar 파일의 화살표를 눌렀을 때 패키지가 나오지 않는다.
- 그럴 경우 해결 방안
  1. 이클립스를 닫는다.
  2. `.m2/repository/` 속의 모든 폴더를 지운다.
  3. 그리고 다시 이클립스 열고 다운받아지면 메이븐 업데이트하고 끝


## IV. 라이브러리 인덱싱 검색
- `pom.xml`의 아래 탭에서 Dependencies 클릭
- Add 누르고 tomcat 등 검색
- 원하는 라이브러리 선택 후 버전 골라서 추가

### 하는 방법
1. menu bar - Windows - Show View - Other - Maven - Maven Repositories - Open
2. Global Repositories - central - 우클릭 - Rebuild Index 클릭
3. 완료되는데 엄청 오래걸린다.