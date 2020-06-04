# 개발환경 및 라이브러리

###### 2020.06.04

## I. 개발 환경 설정
- npm & yarn 설치
- react-native 환경 설치
  1. homebrew 없으면 설치해주기 (권장)
  2. watchman 설치 (권장)
  3. `npm install -g react-native-cli`
- 프로젝트 시작
  - `react-native init [프로젝트명]`
  - cocoapod 깔아야 하면 gem으로 까는것 선택
  - (cocoa pod dependencies 에러날 경우)
    - (필요할 경우 sudo gem install cocoapod)
    - 이 경우 맥에 여러 버전의 Xcode가 깔려있을 수 있다.
    - `sudo xcode-select --switch /Applications/Xcode.app` 를 쳐준다.
    - 그리고 다시 프로젝트를 생성하면 정상적으로 생성된다.
  - `cd [프로젝트명]`
  - `npx react-native run-ios`
    - `react-native run-ios`는 에러가 뜬다. 왜...?
  - `__tests__` 디렉터리 이름 변경 -> `tests`
  - `tests/App-test.js`를 `tests/App.spec.js`로 변경
  - `/src` 디렉터리 만들고 그 안에 `App.js` 넣기
  - `index.js` 에서 `App.js` 경로 변경

## II. 사용할 라이브러리

### 1) Jest
- 여러가지 익스펙테이션, 매치 등이 포함된 통합 라이브러리
- 여러가지 라이브러리와 연동이 가능
- React Native에는 기본적으로 포함되어 있다.

### 2) Enzyme
- Airbnb에서 개발해서 배포하고 있다.
- 리액트 컴퍼넌트를 테스트할 때 사용하는 라이브러리
- 컴퍼넌트를 렌더링하거나 탐색할 수 있는 기능 제공
- Shallow rendering 제공, Shallow Rendering을 통해서 다양하게 탐색을 할 수 있다.

### 3) Detox
- e2e (end to end)
- 컴퍼넌트가 아니라 사용자관점에서 사용자의 입력을 받았을 때 앱이 어떻게 동작한다라는 방식의 테스트를 위한 라이브러리
- 기본적으로 모바일 앱을 위해 개발된 라이브러리 (ios만 지원)

## III. Jest 설정 및 동작 확인
- `tests/App.spec.js`에 아래 코드 작성으로 동작 확인
  ```js
  /**
   * @format
   */

  import "react-native";
  import React from "react";
  import App from "../src/App";

  describe("Jest", () => {
    it("is it working?", () => {
      const a = 1;
      expect(a + 1).toBe(2);
    })
  })
  ```
  > Jest를 discribe하는 것이고 'is it working?' 기능을 확인하겠다. a+1이 2가 되어야 한다고 expect한다.

## IV. Enzyme 설치 / 설정 및 동작 확인

### 1) 설치
> enzyme은 기본적으로 컴퍼넌트를 렌더링하는 툴인데 이 렌더링 툴이 리엑트 렌더링을 정확히 이해하기 위해서 어뎁터(enzyme-adapter-react-16, react-dom@16)가 필요하다.
- `npm i --save-dev enzyme enzyme-adapter-react-16`
- `npm i --save react-dom@16`

### 2) 설정
> 엔자임과 리엑트를 연결해주는 셋업파일이 필요하다.
- `tests/setup.js` 생성
  ```js
  import { configure } from "enzyme";
  import Adapter from "enzyme-adapter-react-16";

  configure({ adapter: new Adapter() });
  ```
- `package.json` 파일의 jest 부분에 위 셋업 파일을 불러오도록 선언
  ```json
  {
    // ...
    "jest": {
      "preset": "react-native",
      "setupFiles": [
        "./tests/setup.js"
      ]
    }
  }
  ```

- `tests/App.spec.js`에 아래 코드 작성으로 동작 확인
  ```js
  // ...
  import { Text } from "react-native";
  import { shallow } from "enzyme";

  // ...

  describe("Enzyme", () => {
    it("is it working?", () => {
      const txt = "hello";
      const wrapper = shallow(<Text>{ txt }</Text>);
      expect(wrapper.text()).toBe(txt)
    })
  })
  ```

## V. Detox 설치 / 설정 및 동작 확인

### 1) 설치
- `brew tap wix/brew` (applesimutils를 설치하기 위해 brew lib 디렉터리에 클론받는것)
- `brew install applesimutils`
- `npm install -g detox-cli`
- `npm install --save-dev detox` or `yarn add --dev detox`
- `detox --version`으로 확인

### 2) detox initialize
- `detox init -r jest`
- `.detoxrc.json` 파일에 아래 붙여 넣기
  ```json
  {
    "testRunner": "jest",
    "runnerConfig": "e2e/config.json",
    "configurations": {
      "ios.sim.debug": {
        "binaryPath": "./ios/build/Build/Products/Release-iphonesimulator/프로젝트명.app",
        "build": "xcodebuild -workspace ios/프로젝트명.xcworkspace -configuration release -scheme 프로젝트명 -sdk iphonesimulator -derivedDataPath ios/build",
        "type": "ios.simulator",
        "name": "iPhone 11 Pro"
      }
    }
  }
  ```
  - `"binaryPath"`가 실제로 앱을 테스트할 때 사용하는 경로이다.
- 첫번째 테스트 진행을 위해 `detox build`
- `e2e/firstTest.spec.js` 수정
  ```js
  describe('Example', () => {
    beforeEach(async () => {
      await device.reloadReactNative();
    });

    it('should have "Step One" section', async () => {
      await expect(element(by.text('Step One'))).toBeVisible();
    });

    it('should have "See Your Changes" section', async () => {
      await expect(element(by.text('See Your Changes'))).toBeVisible();
    });
  });
  ```
- `detox test` 실행
> 다른 엘레먼트를 실험하고 싶으면 먼저 테스트를 쓰고 -> 실패 -> 수정 -> 빌드 -> 테스트 -> 성공
  
> detox의 가장 큰 차이점 : `async await` 를 지원한다.

### detox init, detox build, detox test 에서 어어어어어어어어어엄청 애먹었다.
- 결국 detox build를 먼저 하고 detox test를 하면 되는 것이었다..... ㅠㅠ ( 테스트 할때마다 detox build 해야함 )