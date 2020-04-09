# Functional Scope VS Block Scope

- 스코프는 컨테이너 또는 바구니 구실을 하는 일련의 **버블**이고 변수나 함수 같은 확인자가 그 안에서 선언된다.
- 이 버블은 경계갸 분명하게 중첩되고, 그 경계는 프로그래머가 코드르 작성할 때 결정된다.

## I. 함수 기반 스코프

- 자바스크립트는 함수 기반 스코프 사용

## II. 일반 스코프에 숨기기

- 함수에 대한 전통적인 개념
  - 함수를 선언하고 그 안에 코드를 넣는다.
  - 작성한 코드에서 임의 부분을 함수 선언문으로 감싼다. 이는 해당 코드를 **숨기는** 효과가 있다.
- 이렇게 하면 해당 코드 주위에 새로운 스코프 버블이 생성된다. 즉, 감싸진 코드 안에 있는 모든 변수가 이전 코드에 포함됐던 스코프가 아니라 새로이 코드를 감싼 함수의 스코프에 묶인다.
- **최소 권한의 법칙** : 소프트웨어 디자인 원칙, 모듈/객체의 API와 같은 소프트웨어를 설계할 때 필요한 것만 최소한으로 남기고 나머지는 *숨겨야*하는 것
- i.e
  ```javascript
  function doSomething(a) {
    b = a + doSomethingElse(a*2);
    console.log(b*3);
  }

  function doSomethingElse(a) {
    return a - 1;
  }

  var b;
  doSomething(2); // 15
  ```
  > 이 코드에서 변수 b와 함수 doSomethingElse()는 doSomething()이 어떤 작업을 하는지 보여주는 '비공개' 부분이라고 할 수 있다. 변수 b와 doSomethingElse()에 '접근'할 수 있도록 내버려 두는 것은 불필요할 뿐 아니라 '위험'할 수 있다.
  ```javascript
  function doSomething(a) {
    function doSomethingElse(a) {
      return a - 1;
    }
    var b;
    b = a + doSomethingElse(a*2);
    console.log(b*3);
  }

  doSomething(2); //
  ```
  > 이제 b와 doSomethingElse()는 외부에서 접근할 수 없어서 더는 바깥의 영향을 받지 않고, 오직 doSomething()만이 이들을 통제한다.
  > 
  > 또한 위와 같이 숨기는 것은 예상치 못한 변숫값의 겹쳐쓰기를 방지한다.

## III. 스코프 역할을 하는 함수
```javascript
var = 2;

(function foo() {
  var a = 3;
  console.log(a);   // 3
})();
console.log(a);     // 2
```
> 위 코드는 별다를 바 없어 보일 수 있지만, 이 코드에서 함수는 보통의 선언문이 아니라 함수 표현식으로 취급된다.
- 위 함수는 익명함수로 사용할 수 있지만, 몇가지 단점이 있다.
  - 익명 함수는 스택 추적 시 표시할 이름이 없어서 디버깅이 어려울 수 있다.
  - 이름 없이 함수 스스로 재귀 호출을 하려면 불행히도 폐기 예정인 arguments.callee 참조가 필요하다.
  - 이름은 보통 쉽게 이해하고 읽을 수 있는 코드 작성에 도움이 되는데, 익명 함수는 이런 이름을 생략한다.
- 그래서 보통 사용되는 함수 이름이 **IIFE**
  - Immediately, Invokely, Function, Expression

## IV. 스코프 역할을 하는 블록
- 자바스크립트를 제외하고도 많은 언어가 블록 스코프를 지원한다. 그래서 자바스크립트만을 써왔던 개발자에게는 이 개념이 약간 어색할 수도 있다.
- 그러나 블록 스코프 방식으로 코딩해 본 적이 없더라도 다음과 같은 자바스크립트 코드는 매우 익숙할 수 있다.
  ```javascript
  for (var i=0; i<10; i++) {
    console.log(i);
  }
  ```
  - 변수 i를 for 반복문의 시작부에 선언하는 이유는 보통 i를 오직 for 반복문과 관련해서 사용하려 하기 때문이다.
  - 여기서 i는 for문 밖에서는 사용하지 못하고 for 블록 안에서만 사용가능하다.

  ```javascript
  var foo = true;

  if (foo) {
    var bar = foo * 2;
    bar = something(bar);
    console.log(bar);
  }
  ```
  - 위 코드는 보기에만 스코프처럼 보이는 **가짜 블록 스코프**로, bar를 의도치 않게 다른 곳에서 사용하지 않도록 상기시키는 역할을 할 뿐이다.
  - 진짜 블록 스코프는 **최소 권한 노출의 원칙**을 확장하여 정보를 함수 안에 숨기고, 나아가 저보를 코드 블록 안에 숨기기 위한 도구이다.
  - 다시 for문을 보자
    ```javascript
    for (var i=0; i<10; i++) {
      console.log(i);
    }

    console.log(i);
    ```
    - 만약 블록 스코프가 존재한다면, for문 밖의 i는 ReferenceError를 내야한다.
    - 하지만 외견상으로 자바스크립트는 블록 스코프를 지원하지 않는다. 즉 i는 for문에서 선언돼었으므로 보인의 스코프내에서 발견되어진다.

### 자바스크립트에서 블록 스코프를 선언하는 방법

#### 1) with 키워드
- 이 키워드는 성능을 위해 쓰지않기로 했으니 패스!

#### 2) try/catch
- try/catch의 catch 부분에서 선언된 변수는 catch 블록 스코프에 속한다.
  ```javascript
  try {
    undefined();  // illegal operation to force an exception!
  }
  catch (err) {
    console.log(err);   // work!
  }
  console.err(err); // ReferenceError: `err` not found
  ```
  > 예제에서 보듯, 변수 err은 오직 catch 문 안에서만 존재하므로 다른 곳에서 참조하면 오류가 발생한다.
  
#### 3) let
- ES6에서 새로운 키워드 let이 채택됐다.
- let은 var 같이 변수를 선언하는 다른 방식이다.
- 명시적이지 않지만 **let은 선언한 변수를 위해 해당 블록 스코프를 이용한다.**
  ```javascript
  var foo = true;

  if (foo) {
    let bar = foo * 2;
    bar = something(bar);
    console.log(bar);
  }

  console.log(bar);   // ReferenceError
  ```
  - let이 아닌 var를 사용했다면 bar 변수는 if문의 블록 스코프속에만 속해지지 않은 변수였을 것이다.
  - 호이스팅은 선언문이 어디에서 선언됐든 속하는 스코프의 맨 앞으로 변수 선언을 끌어 올리는 것을 말하는데, **`let`을 사용한 선언문은 속하는 스코프에서 호이스팅 효과를 받지 않는다.**
  - 또한 호이스팅이 안되므로 인해 해당 블록 안에서만 존재하므로, **블록이 끝나는과 동시에 가비지컬렉팅되므로 성능을 올리는데에도 도움이 된다.**

#### 4) const
- ES6에서는 키워드 let과 함께 const도 추가됐다.
- let과 같이 블록 스코프를 생성하고, **선언된 값은 고정된다.(상수)**
- 언언된 후 const로 선언된 변수의 값을 변경하려고 하면 오류가 발생한다.