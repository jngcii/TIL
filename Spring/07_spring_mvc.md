# 스프링 MVC 웹서비스

###### 2020.06.27

## I. 웹서버(톰캣) 다운로드
- `http://tomcat.apache.org/`에서 다운로드

## II. 웹서버(톰캣)와 이클립스 연동
- [Preferences] - [Server] - [Runtime Environment]
- Servers 탭에서 이용중인 서버 더블클릭 - Server Location에서 Use Tomcat installation 선택 - Server Options에서 public module contexts to separate XML files 선택 - Ports에서 HTTP 포트를 8090으로 수정 (나중에 다른 것들과 충돌날까봐) - 저장
- 아래 탭쪽 퍼스팩티브 오른쪽에서 Publish to the server 누르고 Start the server

## III. 이클립스에 STS 설치
- 서버를 만들었으면 웹서비스 기능구현을 해야한다.
- 그러려면 web.xml을 만들고 servlet(dispatcherServlet)등록도 하고 해야한다.
- STS (Spring Tool Suit) : 이런것들을 일일이 하지않아도, 기본적으로 자동으로 설정해주는 플러그인
- 방법 (두가지 방법)
  - [Menu Bar] - [Help] - [Eclipse MarketPlace] - sts검색 - 모두 체크 후 설치
  - [Menu Bar] - [Help] - [Install New Software] - 직접 사이트 입력
    - 자세한 버전 확인 : http://dist.springsource.com/snapshot/STS/nightly-distributions.html
- 그러면 Spring MVC Project를 이클립스를 이용해 생성할 수 있다.

## IV. STS를 이용한 웹프로젝트 생성
- [New] - [Other...] - [Spring] - [Spring Legacy Project] - Project name 입력 - [Spring MVC Project] - [Next] - package명 작성 - 끝
> Legacy : 하위 호환을 위해 신규 프로그램 속에 남겨두는 기존 프로그램의 소스 코드