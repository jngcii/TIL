# 타입 (Type)

###### 2020.03.18

## 타입의 실체
- 타입별로 내재된 특성을 제대로 알고 있어야 값을 다른 타입으로 변환하는 방법을 정확히 이해할 수 있다.
- 어떤 형태로든 거의 모든 자바스크립트 프로그램에서 강제변환이 일어나므로, 타입을 화실하게 인지하고 있어햔다.

## 내장 타입

- 자바스크립트에는 다음 7가지 내장 타입이 있다.
  - null
  - undefined
  - boolean
  - number
  - string
  - object
  - symbol(ES6부터 추가)
- 값 타입은 `typeof`연산자로 알 수 있다.
- 하지만 `typeof` 반환 값은 항상 7가지 내장 타입과 1:1로 정확히 매치되지 않는다.
  ```javascript
  typeof undefined === "undefined"; // true
  typeof true === "boolean";        // true
  typeof 42 === "number";           // true
  typeof "42" === "string";         // true
  typeof { life: 42 } === "object"; // true
  
  // ES6부터 추가
  typeof Symbol() === "symbol";     // true

  // 자바스크립트의 20년지기 버그
  typeof null === "object";         // true
  // "null"을 반환하지 않고 "object"를 반환한다!
  // ------ 타입으로 null 값을 정확히 확인하는 방법
  var a = null;
  (!a && typeof a === "object");    // true
  ```
  >null은 **falsy**한 유일한 원시 값이지만, 타입은 `object`인 특별한 존재이다.
- `typeof`가 반환하는 또다른 문자열 : `function`
  ```javascript
  typeof funciton a(){ /*...*/ } === "function" //true
  ```
  - `typeof` 반환 값을 보면 `function`이 최상위 레벨의 내장 타입처럼 보이지만, 실제로는 `object`의 **하위타입!**
  - 함수에 선언된 인자의 개수를 보는 방법
    ```javascript
    function a(b, c) {
        /* ... */
    }

    a.length; // 2
    ```
- 배열은? 
  ```javascript
  typeof [1, 2, 3] === "object";    // true
  ```
  - 그냥 객체이다.
  - 키가 문자열인 객체와 반대로, 숫자 인덱스를 가지며, length 프로퍼티가 자동으로 관리되는 등의 추가 특성을 가진 객체의 **하위 타입**

## 값은 타입을 가진다.
- 값에는 타입이 있지만 변수에는 타입이 따로 없다.
- 자바스크립트는 타입강제를 하지 않는다.
- 변수에 `typeof` 연산자를 대어보는 건
  - 이 변수의 타입이 뭐니? (X)
  - 이 변수에 들어있는 값의 타입이 뭐니? (O)
- `typeof` 연산자의 반환 값은 언제난 문자열
  - `typeof 42`는 "number"를 반환
  - `typeof typeof 42`는 "string"을 반환

### 값이 없는 vs 선언되지 않은
- 값이 없는 변수의 값은 `undefined`이며, `typeof` 결과는 "undefined"이다.
- **값이 없는**과 **선언되지 않은**
  - 값이 없는(undefined) : 접근 가능한 스코프에 변수가 선언되었으나 현재 아무런 값도 할당되지 않은 상태
  - 선언되지 않은 : 접근 가능한 스코프에 변수 자체가 선언조차 되이 않은 상태
  ```javascript
  var a;

  a;    // undefined;
  b;    // ReferenceError; b is not defined
  ```
  - **`"b is not defined"`과 `"undefined"`는 완전히 다르다!!!!!**
  - `typeof` 연산 결과는 더 헷갈림 (typeof만의 독특한 안전가드)
  ```javascript
  var a;
  typeof a; // "undefined"
  typeof b; // "undefined"
  ```
  >`typeof b`를 해도 브라우저는 오류 처리를 하지 않는다.

### 선언되지 않은 변수
- 하지만 브라우저에서 자바스크립트 코드를 처리할 때, 여러 스크립트 파일이 변수들의 전역 네임스페이스를 공유할 때, `typeof 안전가드`는 쓸만하다.
- i.e. `DEBUG` 플래그
  - 콘솔 창에 메세지 로깅 등 디버깅 작업을 수행하기 전, 이 변수의 선언 여부를 체크해야 한다.
  - 최상위 전역 스코프에 `var DEBUG = true;`라고 debug.js 파일에만 선언하고, 개발/테스트 단계에서 이 파일을 브라우저가 로딩할때
  - 나머지 애플리케이션코드에서 `ReferenceError`가 나지 않게 하려면, 조심해서 `DEBUG` 전역변수를 체크해야 한다.
  ```javascript
  // 이건 에러가 난다!
  if (DEBUG) {
      console.log("디버깅을 시작합니다.")
  }

  // 이렇게 해야 한다.
  if (typeof DEBUG !== "undefined") {
  }
      console.log("디버깅을 시작합니다.")
  
  // 내장 API 기능을 체크할 때 역시 에러가 나지 않게 도와준다.
  if (typeof atob === "undefined") {
      atob = function() { /* ... */ };
  }
  ```

- `typeof` 안전가드 없이 전역 변수를 체크하는 다른 방법은 전역 변수가 모두 전역 객체의 프로퍼티라는 점을 이용하는 것
  ```javascript
  if (window.DEBUG) {
      // ...
  }
  
  if (window.atob) {
      // ...
  }
  ```
  - 하지만 이 파일이 `node.js`에서 쓰이는 다중 자바스크립트 환경이라면 문제가 되기에, `window` 객체를 통한 전역 변수 참조는 가급적 삼가는 것이 좋다.