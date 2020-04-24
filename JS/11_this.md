# this

###### 2020.04.24

### 요약
- 객체 레퍼런스를 함께 넘기는 **`this`**체계는 API 설계를 좀 더 깔끔하고 명확하며 재사용하기 쉽게 한다.
- 사용 패턴이 복잡해질수록 보통 명시적인 인자로 콘텍스트를 넘기는 방법이 this 콘텍스트를 사용하는 것보다 코드가 더 지저분해진다.
- this는 객체 및 프로토타입과 함께 사용할때 진가를 발휘한다.

## `this`에 대한 오해

### 1) 자기 자신
- this가 함수 그 자체를 가리킨다는 오해
  ```javascript
  function foo(num) {
    console.log("foo: " + num);
    this.count++;
  }

  foo.count = 0;
  var i;
  for (i=0; i<10; i++) {
    if (i>5) {
      foo(i);
    }
  }
  
  // foo: 6
  // foo: 7
  // foo: 8
  // foo: 9

  console.log(foo.count); // 0 ....???
  ```
  - foo를 함수 자기 자신이라고 생각했을 경우이다.
  - `foo.count = 0;`으로 foo라는 함수 객체에 count라는 프로퍼티와 함께 값 0을 넣어줬다.
  - 하지만 this는 foo를 가르키는게 아니므로 엉뚱한 count가 올라가고있다.
  - 결국 foo.count는 선언한 그대로가 출력된다.

### 2) 자신의 스코프
- 아주 흔한 오해
- 어떤면에서는 맞지만 잘못 이해한 것
- `this`는 어떤 식으로도 함수의 렉시컬 스코프를 참조하지 않는다.
- 스코프**객체**는 자바스크립트 엔진의 내부 부품이기 때문에 일반 자바스크립트 코드로는 접근하지 못한다.
- 넘지 말아야 할 선을 넘어 `this`가 암시적으로 함수의 렉시컬 스코프를 가리키도록 해보자
  ```javascript
  function foo() {
    var a = 2;
    this.bar();
  }

  function bar() {
    console.log(this.a);
  }

  foo();  // ReferenceError: a is not defined.
  ```
  - `foo`를 통해 `bar`가 호출되면 `bar`의 스코프는 `foo`와 전역스코프이다.
  - `foo` 함수 블록에는 `a`가 선언되어있으므로 `a`는 `bar`의 스코프 안에 있다.
  - `a`가 선언되지 않았다고 나온다!
  - 이유는? `this`는 함수의 스코프를 의미하지 않기 때문!
  - 실제로 `this.a`의 `this`는 `foo`의 `this`에 의해 실행되었고 그 `this`는 전역 객체이므로 `this.a`의 `this`는 호출부인 전역 객체이다.
  - 전역객체의 스코프에는 `a`라는 확인자가 선언되지 않았으므로 ReferenceError를 뱉는다.