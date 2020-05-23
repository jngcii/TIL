# 프로토타입 (Prototype)

###### 2020.05.23

## I. [[Prototype]]
- 자바스크립트는 객체가 생성되면, 무조건 그 안에 `[[Prototype]]`이라는 다른 객체를 참조하는 프로퍼티를 생성한다.
```js
var anotherObject = {
  a: 2
};

var myObject = Object.create(anotherObject);

myObject.a;   // 2
```
- `myObject.a`처럼 객체 프로퍼티 참조시 `[[Get]]`이 호출되는데, 기본적으로 객체 자체의 해당 프로퍼티가 존재하는지 찾아보고 존재하면 그 프로퍼티를 사용한다.
- `myObject`에 `a`란 프로퍼티가 없으면 이 객체의 `[[Prototype]]` 링크를 따라가서 수색한다.
- 이 경우, `[[anotherObject]]`에서 2라는 값을 대신 찾아서 프로퍼티 접근의 결괏값을 반환한다.
- 만약 `anotherOBject`에서도 못찾으면 `[[Prototype]]` 연쇄를 다시 따라 올라가고 연쇄 끝에 이르러서도 프로퍼티가 발견되지 않으면 `[[Get]]`은 결괏값으로 `undefined`를 반환한다.
- `for ... in` 루프에서 객체를 순회할 때도 `[[Prototype]]` 연쇄의 검색 과정과 비슷한 방식으로 연쇄를 통해 손길이 닿는 프로퍼티라면 죄다 열거한다.

### 1. `Object.prototype`
- `[[Prototype]]` 연쇄는 결국 내장 프로토타입 `Object.prototype`에서 끝난다.
- 모든 자바스크랩트 객체는 `Object.prototype` 객체의 자손이므로 여기에는 자바스크립트에서 두루 쓰이는 다수의 공통 유틸리티가 포함되어 있다. (`toString()`, `valueOf()`, `hasOwnProperty()`, `isPrototypeOf()`, ...)

### 2. 프로퍼티 세팅과 가려짐
```js
myObject.foo = "bar";
```
- 객체 프로퍼티 세팅은 단지 어떤 객체에 프로퍼티를 새로 추가하거나 기존 프로퍼티 값을 바꾸는 것 이상의 의미가 있다.
- `foo`라는 이름의 평범한 데이터 접근 프로퍼티가 `myObject` 객체에 직속된 경우 이 할당문은 기존 프로퍼티 값을 고치는 단순한 기능을 할 뿐이다.
- `foo`라는 프로퍼티명이 `myObject` 객체와 이 객체를 기점으로 한 `[[Prototype]]` 연쇄의 상위 수준 두곳에서 동시에 발견될 때, 이를 **가려짐**이라 한다. (`myObject`의 직속 프로퍼티로 인한 상위 연쇄의 `foo`가 가려진다.)
- 직속이 아니라면 `[[Prototype]]` 연쇄를 순회하기 시작하고 그렇게 해도 `foo`가 발견되지 않으면 그제야 `foo`라는 프로퍼티를 `myObject` 객체에 추가한 후 주어진 값을 할당한다. 이럴 경우 사실 미묘한 일들이 벌어지는데 아래와 같다.
  1. `[[Prototype]]` 연쇄의 상위 수준에서 `foo`라는 이름의 일반 데이터 접근 프로퍼티가 존재하는데, 읽기전용이 아닐 경우(writable: true), **`myObject`의 직속 프로퍼티 `foo`가 새로 추가되어 결국 가려짐 프로퍼티가 된다.**
  2. `[[Prototype]]` 연쇄의 상위 수준에서 `foo`라는 이름의 일반 데이터 접근 프로퍼티가 존재하는데, 읽기전용일 경우(writable: false), 어떠한 일도 일어나지 않는다. (엄격모드에서는 에러를 뱉는다.) **어쨋든 가려짐은 발생하지 않는다.**
  3. `[[Prototype]]` 연쇄의 상위 단계에서 발견된 `foo`가 세터일 경우, 항상 이 세터가 호출된다. `myObject`에 가려짐 프로퍼티 `foo`를 추가하지 않으며 `foo` 세터를 재정의하는 일 또한 없다.
- `2`, `3`번에서 `foo`를 가리려면 `=` 할당 연산자를 쓰면 안되고 `Object.defineProperty()` 메서드를 사용하여 `myObject`에 `foo`를 추가해야 한다.
- 가려짐은 이용 가치에 비해 지나치게 복잡하고 애매한 구석이 있어서 될 수 있으면 사용하지 않는게 좋다.
- `작동 위임`(나중에 설명)이라는 대안적인 디자인 패턴을 통해 좀 더 깔끔하게 가려짐을 대체할 수 있다.
- 가려짐은 아래와 같은 혼란을 가져올 수 있다.
  ```js
  var anotherObject = {
    a: 2
  };
  var myObject = Object.create(anotherObject);
  anotherObject.a;                      // 2
  myObject.a;                           // 2
  anotherObject.hasOwnProperty("a");    // true
  myObject.hasOwnProperty("a");         // false
  myObject.a++;                         // 허걱, 암시적인 가려짐이 발생한다!
  anotherObject.a;                      // 2
  myObject.a;                           // 3
  myObject.hasOwnProperty("a");         // true
  ```
  - 겉보기엔 `myObject.a++`이 `anotherObject.a` 프로퍼티를 찾아 1만큼 증가시킬 것 같지만 `++` 연산자는 결국 `myObject.a = myObject.a + 1`을 의미해 의도와 다른 결과를 만들어낸다.
  - `anotherObject.a`를 1만큼 증가시킬 의도라면 `anotherObject.a++`이 유일한 정답이다.