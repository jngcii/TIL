# 값 (Value)

###### 2020.03.18

## 배열

- 자바스크립트의 배열은 타입이 엄격한 다른 언어와 달리 문자열, 숫자, 객체 심지어 다른 배열이나 어떤 타입의 값이라도 담을 수 있는 그릇이다.
- 배열 크기는 미리 정하지 않고도 선언할 수 있으며 원하는 값을 추가하면 된다.
- 자바스크립트 배열에는 이상한 짓을 할 수 있다. (이런 짓은 하지 말자)

  - 빈 슬롯을 만들 수 있다.

    ```javascript
    var a = [];

    a[0] = 1;
    // a[1]은 건너 뛰고
    a[2] = [3];

    a[1]; // undefined;

    a.length; // 3
    ```

  - 매열에 문자열 타입의 키/프로퍼티를 둘 수 있다.
    ```javascript
    var a = [];
    a["13"] = 42;
    a.length; // 14
    ```

### 유사 배열

- 유사 배열 값을 진짜 배열로 바꾸고 싶을 때가 있는데, 이럴때는 배열 유틸리티 함수를 사용하여 해결하는 것이 일반적이다.
- i.e.
  - DOM 쿼리 작업을 수행하면, 배열은 아니지만 변환 용도로는 충분한 **유사배열**형태의 DOM 원소 리스트가 반환된다.
- i.e.
  - 함수에서 arguments 객체를 사용하여 인자를 리스트로 가져오는 것 (ES6부터 비추)
- 이런 변환은 slice() 함수의 기능을 가장 많이 사용
  ```javascript
  function foo() {
    // ES6 이전의 코드
    var arr = Array.prototype.slice.call(arguments);
    // ES6 부터의 코드
    var arr = Array.from(arguments);
    arr.push("bam");
    console.log(arr);
  }

  foo("bar", "baz");  // ["bar", "baz", "bam"]
  ```

## 문자열
- 자바스크립트 문자열은 실제로 생김새만 비슷할뿐, 문자 배열과 같지 않다!!!
- 문자열 vs 문자 배열
  - 문자열은 불변 값 (**Immutable**) : 문자열의 메서드는 그 내용을 바로 변경하지 않고 항상 새로운 문자열을 생성한 후 반환
  - 배열은 가변 값 (**Mutable**) : 대부분의 배열 메서드는 그 자리에서 곧바로 원소를 수정
  ```javascript
  var a = "foo";
  var b = ["f", "o", "o"];

  c = a.toUpperCase();
  a === c;              // false
  a;                    // "foo"
  c;                    // "FOO"

  b.push("!");
  b;                    // ["f", "o", "o", "!"]
  ```
- 문자열에 사실 대부분의 배열 메서드는 사용할 수 없지만, 불변 배열 메서드는 빌려쓸 수 있다.
  > 불변 배열 메서드 : 사용해도 배열이 변하지 않는 메서드
  ```javascript
  a.join;       // undefined
  a.map;        // undefined

  var c = Array.prototype.join.call(a, "-");
  var d = Array.prototype.map.call(a, function(v) {
    return v.toUpperCase() + ".";
  })

  c;            // "f-o-o"
  d;            // "F.O.O"

  // a 자체가 변한게 아니라는 점에 주목하자!!

  a.reverse;    // undefined
  b.reverse();  // ["!", "o", "O", "f"] (변한 값을 리턴)
  b;            // ["!", "o", "O", "f"] (배열 자체가 변함)

  // reverse는 가변 메서드라서 빌려쓰는것조차 불가능!!!
  Array.prototype.reverse.call(a);
  ```

## 숫자
- 자바스크립트의 숫자 타입은 number가 유일하며 '정수', '부동소수점 숫자'를 모두 아우른다.
- 아주 크거나 작은 숫자는 지수형으로 표시하며, `toExponential()` 메서드의 결과값과 같다.
  ```javascript
  var a = 5E10;
  a;                  // 50000000000
  a.toExponential();  // "5e+10"

  var b = a * a;
  b;                  // 2.5e+21

  var c = 1 / a;
  c;                  // 2e-11
  ```
- 숫자 값은 Number 객체 래퍼로 박싱할 수 있기 때문에 `Number.porototype` 메서드로 접근할 수도 있다. 
- i.e. `toFixed()` 메서드 (지정한 소수점 이하 자릿수까지 나타냄)
  ```javascript
  var a = 42.59;

  a.toFixed(0);   // "43"
  a.toFixed(1);   // "42.6"
  a.toFixed(2);   // "42.59"
  a.toFixed(3);   // "42.590"
  ```

### 작은 소수 값
- 이진 부동 소수점 숫자의 부작용
  ```javascript
  0.1 + 0.2 === 0.3;    // false
  ```
- 이진 부동 소수점으로 나타낸 0.1과 0.2는 원래의 숫자와 일치하지 않는다.
- 결과 역시 정확한 0.3이 아니고 실제로는 0.30000000000000004에 가깝다.
- 비교하는 방법 : **Number.EPSILON 사용하기**(ES6 이후부터만 기본 적용)
  ```javascript
  // Number.EPSILON 폴리필
  if (!Number.EPSILON) {
    Number.EPSILON = Math.pow(2, -52);
  }

  // 동등함 비교
  function numbersCloseEnoughToEqual(n1, n2) {
    return Math.abs(n1 - n2) < Number.EPSILON;
  }

  var a = 0.1 + 0.2;
  var b = 0.3;

  numbersCloseEnoughToEqual(a, b);                  // true
  numbersCloseEnoughToEqual(0.0000001, 0.0000002);  // false
  ```

### 안전한 정수 범위
- 정수는 `Number.MAX_VALUE`(1.798e+308)보다 훨씬 작은 수준에서 안전 값의 범위가 정해져 있다.
- 안전하게 표현할 수 있는 최대 정수는 2^53-1이다. (약 9천 조)
- ES6 에서는 `Number.MAX_SAFE_INTEGER`로 정의한다.
- 정수인지 확인하는 방법
  ```javascript
  // Number.isInteger() 사용 (ES6부터만 지원)
  // 아래는 폴리필
  if (!Number.isInteger) {
    Number.isInteger = function(num) {
      return typeof num == "number" && num % 1 == 0;
    };
  }

  Number.isInteger(42);   //
  ```

## 특수 값

### 값 아닌 값
- Undefined 타입의 값은 undefined 뿐이다.
- null 타입도 값은 null 뿐이다.

### void 연산자
- undefined는 내장 식별자로, 값은 undefined지만, 이 값은 void 연산자로도 얻을 수 있다.
- 표현식 `void __`는 어떤 값이든 무효로 만들어, 항상 결과값을 undefined로 만든다.
  ```javascript
  var a = 42;
  console.log(void a, a);   // undefined 42
  ```
- void 연산자는 어떤 표현식의 결괏값이 없다는 걸 확실히 밝혀야 할때 긴요하다.
  ```javascript
  function doSomething() {
    // 'APP.ready'는 이 애플리케이션에서 제공한 값이다.
    if (!APP.ready) {
      // 나중에 다시해라!!
      return void setTimeout(doSomething, 100);
    }

    var result;
    // 별더 처리 수행
    return result;
  }

  // 제대로 처리 했나?
  if (doSomething()) {
    // 다음 작업 바로 실행
  }
  ```
  - setTimeout() 함수는 숫자값을 반환하지만, 예제에서는 숫자 값을 무효로 만들어 doSomething() 함수의 결괏값이 if 문에서 false로 인식하게 된다.
  - 함수를 실행시키고 null을 리턴하는것과 같다.
  - 보통은 아래와 같이 사용한다 ;;;
  ```javascript
  if (!APP.ready) {
    // 나중에 다시해라!!
    setTimeout(doSomething, 100);
    return;
  }
  ```
  
### 특수 숫자
- NaN (**N*ot *a* *N*umber)
  ```javascript
  var a = 2 / "foo";      // NaN
  typeof a === "number"   // true
  ```
  >ㅋㅋㅋㅋㅋ 숫자가 아님은 숫자다 ㅋㅋㅋ
  ```javascript
  var a = 2 / "foo";

  a == NaN;     // false
  a === NaN;    // false
  ```
  >NaN은 너무 귀하신 몸이라 다른 어떤 NaN과도 동등하지 않다. ( 자기 자신과도 같지 않다;; )

  - `isNaN()`이라는 함수로 NaN 여부를 구별할 수 있으나, 진짜 숫자가 아니면 전부 true를 반환해버린다 ;; ㅠㅠ
    ```javascript
    a = 2 / "foo";
    b = "foo";

    a;                  // NaN
    b;                  // "foo"

    window.isNaN(a);    // true
    window.isNaN(b);    // true ;;;;;;
    ```
  - ES6부터 사용 가능한 `Number.isNaN()`을 사용하면 된다.
    ```javascript
    // ES6이전 버전 - Number.isNaN() 폴리필
    if (!Number.isNaN) {
      Number.isNaN = function(n) {
        return (
          typeof n === "number" && window.isNaN(n)
        );
      };
    }
    ```

### 무한대
- 자바스크립트에는 ZeroDivisionError같은 에러가 없다.
- 대신 0으로 나누면 Infinity(Number.POSITIVE_INFINITY)라는 결과값이 나온다.
- 분자가 음수면 -Infinity가 나옴
- 무한으로 무한을 나누면? **NaN**

### 특이한 동등 배교
- ES6부터는 잡다한 예외를 걱정하지 않아도 두 값이 절대적으로 동등한지를 확인하는 새로운 유틸리티를 지원한다. 
- `Object.is()`
  ```javascript
  // Ojbect.is() 폴리필
  if (!Object.is) {
    Object.is = function (v1, v2) {
      // "-0" 테스트
      if (v1 === 0 && v2 === 0) {
        return 1 / v1 === 1 / v2;
      }

      // "NaN" 테스트
      if (v1 !== v1) {
        return v2 !== v2;
      }

      // 기타
      return v1 === v2;
    };
  }


  var a = 2/ "foo";
  var b = -3 * 0;

  Object.is(a, NaN);    // true
  Object.is(b, -0);     // true
  Object.is(b, 0);      // false
  ```

## 값 vs 레퍼런스
- 자바스크립트에서는 어떤 변수가 다른 변수를 참조할 수 없다. **그냥 안된다.**
- 자바스크립트에서 레퍼런스는 (공유된) 값을 가리키므로 서로 다른 10개의 레퍼런스가 있다면 저마다 항상 공유된 단일 값을개별적으로 참조한다.
- null, undefined, string, number, boolean, symbol 같은 단순 스칼라 원시 값은 언제나 값-복사 방식으로 할당/전달된다.
- 나머지는 모두 합성값으로 동일한 공유 값을 참조(레퍼런스)한다.
- 합성 값을 값-복사에 의해 효과적으로 전달하려면, 손수 값의 사본을 만들어 전달한 레퍼런스가 원본을 가리키지 않게 하면 된다.
- 2와 같은 스칼라 원시 값을 레퍼런스 형태로 넘기려면 Number 객체 래퍼로 원시 값을 박싱하면 된다. 하지만, Number 객체의 레퍼런스 사본이 함수에 전달되는 것은 맞지만, 공유된 객체를 가리키는 레퍼런스가 있다고 자동으로 공유된 원시 값을 변경할 권한이 주어지는 것은 아니다.
  ```javascript
  function foo() {
    x = x + 1;    // 이 과정에서 다시 언박싱되어서 더이상 Number로 박싱된 객체가 아님
    x;            // 3
  }

  var a = 2;
  var b = new Number(a);

  foo(b);
  console.log(b); // 3이 아닌 2
  ```
  - 이렇게 객체 래퍼 Number를 사용하기보단 차라리 처음부터 손수 객체래퍼(obj)를 쓰는 편이 훨씬 낫다.