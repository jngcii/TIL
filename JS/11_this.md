# this

###### 2020.04.24

### 요약
- 객체 레퍼런스를 함께 넘기는 **`this`**체계는 API 설계를 좀 더 깔끔하고 명확하며 재사용하기 쉽게 한다.
- 사용 패턴이 복잡해질수록 보통 명시적인 인자로 콘텍스트를 넘기는 방법이 `this` 콘텍스트를 사용하는 것보다 코드가 더 지저분해진다.
- `this`는 객체 및 프로토타입과 함께 사용할때 진가를 발휘한다.
- `this`는 호출부에서 함수를 호출할 때 바인딩된다.

## I. `this`에 대한 오해

### 1. 자기 자신
- `this`가 함수 그 자체를 가리킨다는 오해
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
  - `foo`를 함수 자기 자신이라고 생각했을 경우이다.
  - `foo.count = 0;`으로 `foo`라는 함수 객체에 `count`라는 프로퍼티와 함께 값 0을 넣어줬다.
  - 하지만 this는 `foo`를 가르키는게 아니므로 엉뚱한 `count`가 올라가고있다.
  - 결국 `foo.count`는 선언한 그대로가 출력된다.

### 2. 자신의 스코프
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


<br />

## II. `this`란 이런 것이다.

### 1. 호출부

- `this` 바인딩은 오직 호출부와 연관된다.
- 호출 스택에서 진짜 호출부를 찾아내려면 코드를 주의깊게 잘 봐야 한다.

### 2. 규칙에 따른 `this`
> 함수가 실행되는 동안 `this`가 무엇을 참조할지를 호출부가 어떻게 결정하는가?

#### 1) 기본 바인딩
- 단독 함수 실행에 관한 규칙
- 나머지 규칙에 대항하지 않을 경우 적용되는 `this`의 기본 규칙
  ```javascript
  function foo() {
    console.log(this.a);
  }

  var a = 2;
  foo();  // 2
  ```
  - `foo`를 호출한 것이 가장 바끝 스코프(전역 객체)이므로 전역 객체에 있는 변수 `a`에 바인딩된다.
  ```javascript
  function foo() {
    "use strict";
    console.log(this.a);
  }

  var a = 2;
  foo();  // TypeError: 'this' is 'undefined'
  ```
  - 단, **엄격모드에서는 전역 객체가 기본 바인딩 대상에서 제외된다. 그래서 `this`는 `undefined`가 된다.**

#### 2) 암시적 바인딩
- 호출부에 콘텍스트 객체가 있는지 확인하는 것이다.
  ```javascript
  function foo() {
    console.log(this.a);
  }

  var obj = {
    a: 2,
    foo: foo
  };

  obj.foo();  // 2
  ```
  - `foo` 호출 시점에 이미 obj 객체 레퍼런스는 준비된 상태이다.
  - 함수 레퍼런스에 대한 콘텍스트가 존재할 때 암시적 바인딩 규칙에 따르면 바로 이 콘텍스트 객체가 함수 호출 시 `this`에 바인딩된다.
  - 즉, `this.a`는 `obj.a`가 된다.
  
- 객체 프로퍼티 참조가 체이닝된 상태라면 다음과 같다.
  ```javascript
  function foo() {
    console.log(this.a);
  }

  var obj2 = {
    a: 42,
    foo: foo
  };

  var obj1 = {
    a: 2,
    obj2: obj2
  };

  obj1.obj2.foo(); // 42
  ```
  - 여기서 `this.a`는 `obj2.a`

- 암시적 소실
  ```javascript
  function foo() {
    console.log(this.a);
  }

  var obj = {
    a: 2,
    foo: foo
  };

  var bar = obj.foo;
  var a = "머지";
  bar();  // "머지"
  ```
  - `bar`는 `obj`의 `foo`를 참조하는 변수가 아니라 **`foo`를 직접 가리키는 또 다른 레퍼런스다!!!!!**
  - `bar()`를 호출하는 것은 `foo()`를 호출하는 것과 같으므로 **전역 객체로 기본 바인된다.**

- 콜백함수를 전달하는 경우엔 좀더 애매하다.
  ```javascript
  function foo() {
    console.log(this.a);
  }

  function doFoo(fn) {
    // 'fn'은 'foo'의 또 다른 레퍼런스일 뿐
    fn(); // 호출부
  }

  var obj = {
    a: 2,
    foo: foo
  };

  var a = "머지?";
  doFoo(obj.foo); // "머지?"
  ```
  - 여기서 `fn`로 `obj.foo`가 전달되었지만 `fn`은 역시 그냥 `foo`를 직접 가리키는 또 다른 레퍼런스이다.
  - 그러므로 호출부의 스코프인 `doFoo`에서 `a`를 찾지만 없으므로 전역객체에서 찾는다.
  - 콜백을 받아 처리하는 함수가 내장함수라도 마찬가지! i.e. `setTimeout`

#### 3) 명시적 바인딩
- 어떤 객체를 `this` 바인딩에 이용하겠다는 의지를 코드에 명확히 밝힐 방법
- `call()`과 `apply()`
- 두 메서드는 `this`에 바인딩 할 객체를 첫째 인자로 받아 함수 호출 시 이 객체를 `this`로 세팅한다.
- `this`를 지정한 객체로 직접 바인딩하므로 이를 **명시적 바인딩**이라 한다.
  ```javascript
  function foo() {
    console.log(this.a);
  }

  var obj = {
    a: 2
  };

  foo.call(obj);; // 2
  ```
  - `foo.call()`은 명시적으로 바인딩하여 함수를 호출! (호출하는것까지이다.)
  - 객체 대신 단순 원시값을 인자로 전달하면 원시 값에 대응하는 객체 (`new String()`, `new Boolean()`, new Number()`로 래핑된다.) - **박싱**
- **하드 바인딩**
  ```javascript
  function foo() {
    console.log(this.a);
  }

  var obj = {
    a: 2
  };

  var bar = function() {
    foo.call(obj);
  };

  bar();  // 2
  setTimeout(bar, 100); // 2

  // 하드 바인딩 된 'bar'에서 재정의된 'this'는 의미 없다.
  bar.call(window); // 2
  ```
  - 함수 `bar()`는 내부에서 `foo.call(obj)`로 `foo`를 호출하면서 `obj`를 `this`에 강제로 바인딩한다.
  - **`bar`를 어떻게 호출하든 이 함수는 항상 `obj`를 바인딩하여 `foo`를 실힝한다.**
  - 명시적이고 강력해서 **하드바인딩**이라고 한다.
  - 주로 인자를 넘기고 반환 값을 돌려받는 창구가 필요할 때 주로 쓰인다.
  ```javascript
  function foo(something) {
    console.log(this.a, something);
    return this.a + something;
  }

  // 간단한 'bind'헬퍼
  function bind(fn, obj) {
    return function() {
      return fn.apply(obj, arguments);
    }
  }

  var obj = {
    a: 2;
  };

  var obj = {
    a: 2
  };

  var bar = bind(foo, obj);
  var b = bar(3); // 2 3
  console.log(b); // 5
  ```
  - `bind`는 `fn`을 `obj`에 바인딩하는 함수를 리턴한다.
  - 그 함수를 실행시키면 바인딩됨!!
  - 하드 바인딩은 매우 자주쓰이는 패턴이라서 **ES5 내장 유틸리티 `Function.prototype.bind`도 비슷하게 구현되어있다.**
  - **API 호출 콘텍스트**
    - 많은 라이브러리 함수와 자바스크립트 언어 및 호스트 환경에서 내장된 여러 새로운 함수는 대게 콘텍스트라 불리는 선택적인 인자를 제공한다.
    - 이는 `bind()`를 써서 콜백 함수의 `this`를 지정할 수 없는 경우를 대비한 일종의 예비책이다.

#### 4) `new` 바인딩
- javascript의 `new`는 의미상 다른 언어의 클래스 지향적인 기능과 아무 상관이 없다.
- 클래스에 붙은 것도 아니고 인스턴스화기능도 없다.
- **단순히 `new`를 사용해 호출할때 자바스크립트만의 생성자 함수(평범함 함수)가 실행된다.**
- new 바인딩
  ```javascript
  function foo(a) {
    this.a = a;
  }

  var bar = new foo();
  console.log(bar.a); // 2
  ```
  > 앞에 `new`를 붙여 `foo()`를 호출했고 새로 생성된 객체는 `foo` 호출 시 `this`에 바인딩된다.
- `new`를 붙여 생성자 호출을 하면 다음과 같은 일들이 저절로 일어난다.
  1. 새 객체가 툭 만들어진다.
  2. 새로 생성된 객체의 [[prototype]]이 연결된다.
  3. 새로 생성된 객체는 해당 함수 호출 시 this로 바인딩된다.
  4. 이 함수가 자신의 또 다른 객체를 반환하지 않는 한 `new`와 함께 호출된 함수는 자동으로 새로 생성된 객체를 반환한다.

### 3. 우선순위
1. `new`로 함수를 호출했는가? - 맞으면 새로 생성된 객체가 `this`이다.
2. `call`과 `apply`로 함수를 호출(명시적 바인딩), 이를테면 `bind` 하드 바인딩 내부에 숨겨진 형태로 호출됐는가? - 맞으면 명시적으로 지정된 객체가 `this`다.
3. 함수 콘텍스트(암시적 바인딩), 즉 객체를 소유 또는 포함하는 형태로 호출했는가? - 맞으면 바로 이 콘텍스트 객체가 `this`다.
4. 그 외 경우에는 `this`는 기본값으로 세팅된다. (기본 바인딩)


<br />

## III. 바인딩 예외
> 특정 바인딩을 의도했는데 실제로는 기본 바인딩 규칙이 적용되는 예외 사례

### `this` 무시
- `call`, `apply`, `bind` 메서드에 첫 번째 인자로 `null` 또는 `undefined`를 넘기면 `this` 바인딩이 무시되고 기본 바인딩 규칙이 적용된다.

### 간접 레퍼런스
- 의도적이든 아니든 간접 레퍼런스가 생성되는 경우, 함수를 호출하면 무조건 기본 바인딩 규칙이 적용되어 버린다.
- 간접 레퍼런스는 할당문에서 가장 빈번하게 발생한다.
  ```javascript
  function foo() {
    console.log(this.a);
  }

  var a = 2;
  var o = { a: 3, foo: foo };
  var p = { a: 4 };

  o.foo();  // 3
  (p.foo = o.foo)();  // 2
  ```
  - 할당 표현식 `p.foo = o.foo`의 결괏값은 원 함수 객체의 레퍼런스이므로 실제로 호출부는 처음 예상과는 달리 `p.foo()`, `o.foo()`가 아니고 `foo()`이다. 그래서 기본 바인딩 규칙이 적용된다.

### 소프트 바인딩
- 하드 바인딩은 함수의 유연성을 크게 떨어뜨리기 때문에 `this`를 암시적 바인딩 하거나 나중에 다시 명시적 바인딩 하는 식으로 수동으로 오버라이드하는 것이 불가능하다.
- 암시적/명시적 바인딩 기법을 통해 원하는 대로 `this` 바인딩을 하는 동시에 전역 객체나 `undefined`가 아닌 다른 기본 바인딩 값을 세팅하는 방법
- `softBind() 유틸리티는 소프트 파인딩 로직을 제외하면 ES5의 `bind()` 유틸리티와 매우 비슷하다.
- 호출 시점에 `this`를 체크하는 부분에서 주어진 함수를 래핑하여 전역 색체는 `undefined`일 경우엔 미리 준비한 대체 기본 객체로 세팅한다.


<br />

## IV. ES6 화살표 함수에서의 `this`

- 일반적인 홤수는 지금까지 살펴본 4가지 규칙을 준수한다.
- **하지만 ES6 이후의 화살표 함수는 이 규칙들을 따르지 않는다.**
  ```javascript
  function foo() {
    // 화살표 함수를 반환한다.
    return a => {
      // 여기서 'this'는 어휘적으로 'foo()'에서 상속된다.
      console.log(this.a);
    };
  }

  var obj1 = {
    a: 2
  };

  var obj2 = {
    a: 3
  };

  var bar = foo.call(obj1);
  bar.call(obj2); // 2 (3이 아니다.)
  ```
- `foo()` 내부에서 생성된 화살표 함수는 `foo()` 호출 당시 `this`를 무조건 어휘적으로 포착한다.
- `foo()`는 `obj1`에 `this`가 바인딩되므로 `bar`의 `this` 역시 `obj1`로 바인딩된다.
- **화살표 함수의 어휘적 바인딩은 절대로 (심지오 new로도!) 오버라이드할 수 없다.**
- **화살표 함수는 이벤트 처리기나 타이머 등의 콜백에 가장 널리 쓰인다.**
  > 화살표 함수는 `this`를 확실히 보장하는 수단으로 `bind()`를 대체할 수 있고 겉보기에도 끌리는 구석이 있지만, 결과적으로 더 잘 알려진 렉시컬 스코프를 쓰겠다고 기존의 `this` 체계를 포기하는 형국이란 점을 간과하면 안된다.