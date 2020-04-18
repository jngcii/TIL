# 스코프 클로저 (Closure)

###### 2020.04.18

## 스포일러

> 클로저 : 어떠한 함수를 어디에서 호출하던 그 함수는 자신의 렉시컬 스코프를 기억하고 해당 스코프에 접근할 수 있게 하는 기능

## 핵심
```javascript
function foo() {
  var a = 2;
  function bar() {
    console.log(a);
  }
  return bar;
}

var baz = foo();

baz();  // 2
```
- 함수 bar()는 foo()의 렉시컬 스코프에 접근할 수 있다.
- 함수 foo()는 bar를 참조하는 함수 객체 자체를 반환한다.
- foo()를 실행하여 반환한 값을 baz라 불리는 변수에 대입하고 실제로는 baz() 함수를 호출했다.
- 이는 당연하게도 그저 다른 변수를 통해 참조된 내부 함수인 bar()를 호출한 것이다.
- **그러나 이 경우에, 함수 bar()는 함수가 선언된 렉시컬 스코프 '밖'에서 실행됐다.**
- 일반적으로 foo()가 실행된 후에는 사용되지 않는 메모리인 foo()의 내부 스코프가 가비지 컬렉터에 의해 사라졌다고 생각할 것이다.
- **클로저**는 이렇게 이미 실행된 함수가 여전히 '사용 중'으로서 사라지지 않게 한다.
- bar()는 foo() 스코프에 대한 렉시컬 스코프 클로저를 가지고, foo()는 bar()가 나중에 참조할 수 있도록 스코프를 살려둔다.

## 자주 사용되는 예시
```javascript
function wait(message) {
  setTimeout(function timer() {
    console.log(message);
  }, 1000);
}

wait("Hello, closure!");
```
- 내부 함수 timer를 setTimeout()에 인자로 넘겼다.
- timer 함수는 wait() 함수의 스코프에 대한 스코프 클로저를 가지고 있으므로 변수 message에 대한 참조를 유지하고 사용할 수 있다.
- wait() 실행 1초 후, wait의 내부 스코프는 사라져야 하지만, 익명의 함수가 여전히 해당 스코프에 대한 클로저를 가지고 있다.
- 엔진 내부 깊숙한 곳의 내장 함수 setTimeout()에는 아마도 fn이나 func 정도로 불릴 인자의 참조가 존재한다.
- 엔진은 해당 함수를 호출하여 timer()를 호출하므로 timer의 렉시컬 스코프는 여전히 남아 있다.

## 반복문과 클로저
```javascript
for (var i=1; i<=5; i++) {
  setTimeout(function timer() {
    console.log(i);
  }, i*1000);
}
```
- 이 코드의 목적은 1 ~ 5를 일초에 하나씩 출력하는 것이다.
- 그러나 실제로 코드를 실행하면, 6만 일초에 하나씩 출력한다.
- timeout 함수 콜백은 반복문이 끝나고 나서야 작동한다. (setTimeout(..., 0)이었다 해도, 모든 함수 콜백은 반복문이 끝나고 실행된다. - 이벤트큐 뒷쪽에 붙기때문에)
- 무엇이 필요한가? **반복마다 하나의 새로운 닫힌 스코프**가 필요하다.
- 이 코드를 제대로 실행시키려면?
  ```javascript
  for (var i=1; i<=5; i++) {
    (function IIFE() {
      var j = i;
      setTimeout(function timer() {
        console.log(j);
      }, j*1000);
    })();
  }
  ```
  혹은
  ```javascript
  for (var i=1; i<=5; i++) {
    (function IIFE(j) {
      setTimeout(function timer() {
        console.log(j);
      }, j*1000);
    })(i);
  }
  ```
  **위의 것을 모두 해결해버리는 위대한 ES6**
  ```javascript
  for (let i=1; i<=5; i++) {
    setTimeout(function timer() {
      console.log(i);
    }, i*1000);
  }
  ```
  > 반복문 시작 부분에서 let으로 선언된 변수는 한 번만 선언되는 것이 아니라 반복할 때마다 선언된다.

## 모듈
- 클로저의 능력을 활용하면서 표면적으로는 콜백과 상관없는 코드 패턴중 가장 강력한 패턴
```javascript
function CoolModule() {
  var something = "cool";
  var another = [1, 2, 3];

  function doSomething() {
    console.log(something);
  }

  function doAnother() {
    console.log(another.join("!"));
  }

  return {
    doSomething: doSomething,
    doAnother: doAnother
  };
}

var foo = CoolModule();

foo.doSomething();  // cool
foo.doAnother();    // 1!2!3
```
- 이 코드와 같은 자바스크립트 패턴을 모듈이라고 부른다.
- 가장 흔한 모듈 패턴 구현 방법은 모듈 노출이고, 앞의 코드는 이것의 변형이다.
- CoolModule()은 그저 하나의 함수이지만, 모듈 인스턴스를 생성하려면 반드시 호출해야 한다.
- CoolModule() 함수는 객체를 반환한다.
- 해당 객체는 내장 함수들에 대한 참조를 가지지만, 내장 데이터 변수에 대한 참조는 가지지 않는다.
- 이 객체의 반환값은 본질적으로 모듈의 공개 API라고 생각할 수 있다.
- 객체의 반환 값은 최종적으로 외부 변수 foo에 대입되고, foo.doSomething()과 같은 방식으로 API의 속성 메서드에 접근할 수 있다.

### 싱글톤을 생성하는 모듈
```javascript
var foo = (function IIFE() {
  var something = "cool";
  var another = [1, 2, 3];

  function doSomething() {
    console.log(something);
  }

  function doAnother() {
    console.log(another.join("!"));
  }

  return {
    doSomething: doSomething,
    doAnother: doAnother
  };
})();

foo.doSomething();
foo.doAnother();
```