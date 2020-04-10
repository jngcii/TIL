# Hoisting

###### 2020.04.10

- 자바스크립트는 프로그램이 실행되면 코드가 한 줄 한 줄 위에서부터 차례대로 해석되지 않는다.
- 자바스크립트 엔진이 코드를 인터프리팅(혹은 JIT 컴파일)하기 전에 컴파일하는 과정에서 **선언문만 따로 해당 스코프의 맨 앞으로 끌여올려진다.**

```javascript
a = 2;
var a;
console.log(a);
```
> 위의 코드는 `undefined`가 아닌 `2`를 출력한다.

```javascript
console.log(a);
var a = 2;
```
> 위의 코드는 `ReferenceError`가 아닌 `undefined`를 출력한다.

### 컴파일러는 두 번 공격한다.
- 자바스크립트는 `var a = 2;`를 두개의 구문으로 본다.
  - `var a;`
  - `a = 2;`
- 첫 번째 구문은 선언문으로 컴파일레이션 단계에서 처리된다.
- 두 번째 구문은 대입문으로 실행 단계까지 내버려둔다.

### 함수의 호이스팅

1. 함수 선언문
  ```javascript
  foo();

  function foo() {
    console.log("hi");
  }
  ```
  > 함수 foo읜 선언문이 끌어올려졌으므로 foo를 첫째 줄에서 호출할 수도 있다.
  > 
  > 이 경우에는 함수 전체가 모두 끌어올려진다.

2. 함수 표현식
  - 함수 표현식은 다르다.
  ```javascript
  foo();  // not ReferenceError, but TypeError!

  var foo = function bar() {
    // ...
  }
  ```
  > 위 코드에서 `foo();` 호출식은 `ReferenceError`가 아닌 `TypeError`를 던진다.
  > 
  > `var foo;`가 호이스팅되어 스코프의 맨 위에서 선언되고, 아직 `callable`객체는 아니기 때문에 TypeError를 던지게 되는 것이다.

### 함수가 먼저다.
- 함수와 변수 선언문 모두 끌어올려진다.
- 단, 함수가 끌어올려지고 다음으로 변수가 올라간다.
  ```javascript
  foo();  // 1
  var foo;

  function foo() {
    console.log(1);
  }

  foo = function() {
    console.log(2);
  };
  ```
- 위 실행문에서 `foo();`실행 결과 2가 아닌 1을 출력되는데, 그 이유는 엔진이 위의 코드를 아래와 같이 실행하기 때문이다.
  ```javascript
  function foo() {
    console.log(1);
  }

  foo();  // 1

  foo = function() {
    console.log(2);
  };
  ```
- `var foo`가 중복 선언문이라는 점을 보자. `var foo`는 `function foo()` 선언문보다 앞서 선언됐지만, 함수 선언문이 일반 변수 위로 끌어올려졌다. 많은 변수 선언문이 사실상 무시됐지만 중복 함수 선언문은 앞선 것들을 겹쳐 쓴다.