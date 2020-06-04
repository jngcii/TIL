# TDD & React Native 기본 개념

###### 2020.06.04

## I. TDD
> Test Driven Development
- 테스트를 많이하는 개발 방법? X
- 테스트를 통해서 개발이 이끌어지는 방법!!
- 테스트를 먼저 작성하고 테스트가 요구하는 만큼의 개발을 진행
- 테스트를 작성하지 않은 부분은 구현하지 않는게 원칙

### 방법
1. Describe it (RDD)
  - README Driven Development
  - 어떤 요구사항이고 어떤 결과가 나와야하는지 기술하는단계
2. Make it fail
  - test code만 작성하고 실제로 개발을 진행하지 않는 단계
  - test code를 돌리면 당연히 실패가 나온다.
3. Make if green
  - test code에 기반해 (정상적으로 실행되도록) 실제로 개발을 진행하는 단계
4. Refactoring
  - 개발 전반에 필요한 단계

## II. React Native 기초
> 해외에서 널리 사용되고 개발자들이 선호한다. 너무 잦은 업데이트가 단점
- React는 Web page, Web app을 만들기 위한 언어이다.
- 이를 Native app을 만들기 위해 React Native 개발
- React-core를 사용하기 때문에 개발 방법이나 문법은 동일
- View(화면 표시)가 다르다.
  - React는 브라우저를 대상으로 하기 때문에 html 컴퍼넌트를 사용 (div, ul)
  - React Native는 Native를 대상으로 하기 때문에 별도의 컴퍼넌트 사용 (View, FlatList)

## III. 개발 옵션
- Expo
  - 순수 javascript만으로 Native App을 개발 가능
  - 개발환경셋업이 쉬움
  - E2E 라이브러리 Detox와 매치가 안된다는 단점
  - Detox가 앱의 구동을 확인하고 테스트를 진행해나가는데 Expo Launcher라는 중간단계 레이어가 있어서 실제로 Detox가 앱의 구동을 인지하지 못해 테스트가 진행되지않는다.
- React-Native-Cli