# Native

###### 2020.03.20

## 네이티브 (= 내장함수)
- String()
- Number()
- Boolean()
- Array()
- Object()
- Function()
- RegExp()
- Date()
- Error()
- Symbol()

### 네이티브는 다음과 같이 사용할 수 있다.
```javascript
var s = new String("Hello World!");
```

### 네이티브는 생성자처럼 사용할 수 있지만 실제로 생성되는 결과물은 예상과 다르다.
```javascript
var a = new String("abc");

typeof a;                          // "object"..."String"이 아니다!

a instanceof String;               // true

Object.prototype.toString.call(a); // "[object String]"
```
- `new String("abc")`생성자의 결과는 **원시 값 "abc"를 감싼 객체 래퍼**이다. (원시 값 "abc"는 아니다.)
- `typeof` 연산자로 이 객체의 타입을 보면 자신을 감싼 원시 값의 타입이 아닌 object의 하위 타입에 가깝다.


## 내부 [[Class]]
- typeof가 'object'인 값에는 [[Class]]라는 내부 프로퍼티가 추가로 붇는다.
- 이 프로퍼티는 직접 접근할 수 없고 `Object.prototype.toString()`이라는 메서드에 값을 넣어 호출함으로써 존재를 엿볼 수 있다.
  ```javascript
  Object.prototype.toString.all([1, 2, 3]);
  // "[object Array]:

  Object.prototype.toString.call( /regex-literal/i );
  // "[object RegExp]"
  ```
  >내부 [[Class]] 값이 배열은 "Array", 정규식은 "RegExp"임을 알 수 있다.
- 대부분 내부 [[Class]]는 해당 값과 관련된 내장 네이티브 생성자를 가리키지만, 그렇지 않을 때도 있다. (i.e. null, undefined)
  ```javascript
  Object.prototype.toString.call(null);
  // "[object Null]"

  Object.prototype.toString.call(undefined);
  // "[object Undefined]"
  ```
  >Null(), Undefined() 같은 네이티브 생성자는 없지만 내부 [[Class]] 값은 있는것처럼 나온다.
- 하지만 그 밖의 문자열, 숫자, 불리언같은 단순 원시 값은 **박싱**과정을 거친다.
  ```javascript
  Object.prototype.toString.call("abc");
  // "[object String]"

  Object.prototype.toString.call(42);
  // "[object Number]"

  Object.prototype.toString.call(true);
  // "[object Boolean]"
  ```
  >내부 [[Class]] 값이 각각 String, Number, Boolean으로 표시된 것으로 보아 단순 원시 값은 해당 객체 래퍼로 자동 박싱됨을 알 수 있다.

## 래퍼 박싱하기
- 원시 값엔 프로퍼티나 메서드가 없어서 `.length`, `.toString()`으로 접근하려면 원시 값을 객체 래퍼로 감싸줘야 한다.
- 자바스크립트는 원시 값을 알아서 박싱한다.
- 그러므로 `a="abc"; a.length;`와 같은 코드가 가능하다.
- 자바스크립트 엔진이 암시적으로 사용할 수 없도록 처음부터 값을 객체로 갖고 있게 하는 **'선 최적화'는 프로그램을 더 느리게 만들 수 있다.**
- 즉 `new String("abc")`가 아닌 `"abc"`를 사용해야한다.
- 객체 래퍼로 직접 박싱하는건 비추지만, 수동으로 원시값을 박싱하려면 `Object()`함수를 이용하자. (*new 키워드는 없다.*)


## 언박싱
- 객체 래퍼의 원시 값은 `valueOf()`메서드로 추출한다.
  ```javascript
  var a = new String("abc");
  var b = new Number(42);
  var c = new Boolean(true);

  a.valueOf();    // "abc"
  b.valueOf();    // 42
  c.valueOf();    // true
  ```
  >다시 말하지만 이 방법은 전혀 추천하지 않는다. 알고만 있자.

## 네이티브와 생성자
- 배열, 객체, 함수, 정규식 값은 리터럴 형태로 생성하는 것이 일반적이지만, 리터럴은 생성자 형식으로 만든 것과 동일한 종류의 객체를 생성한다. (즉, 래핑되지 않은 값은 없다.)
- 그러던 말던 다시말하지만, 왠만하면 리터럴 방식을 사용하자.

### Array
```javascript
var a = new Array(1, 2, 3); // new 생략 가능
a;        // [1, 2, 3]

var b = [1, 2, 3];
b;        // [1, 2, 3]
```
- Array 생성자에는 인자로 숫자를 하나만 받으면, *그 숫자를 원소로 배열을 생성하지 않고*, ***배열의 크기를 미리 정하는 기능***이다.
- 이런 짓은 절대 하지 말자;;

### Object(), Function(), RegExp()
- 이 생성자들 역시 분명한 의도가 아니면 사용하지 않는게 좋다.

### Date(), Error()
- 이 네이티브 생성자들은 리터럴 형식이 없으므로 다른 네이티브에 비해 유용하다.
- date 객체 값은 `new Date()`로 생성한다. 이 생성자는 날짜/시각을 인자로 받는다. 인자를 생략하면 현재 날짜/시각으로 대신한다.
- date 객체는 유닉스 타임스탬프 값(1970년 1월 1일부터 현재까지 흐른 시간을 초단위로 환산)을 얻는 용도로 가장 많이 쓰인다. - data 객체의 인스턴스로부터 `getTime()`을 호출하면 된다.
- 하지만 왠만하면 `Date.now()`를 사용하자.
- Error() 생성자는 new 키워드를 생략할 수 있다.
- error 객체의 주 용도는 **현재의 실행 스택 콘텍스트를 포착하여 객체에 담는 것이다.**
- 이 실행 스택 콘텍스트는 함수 호출 스택, error 객체가 만들어진 줄 번호 등 디버깅에 필요한 정보들을 담고 있다.
- error 객체는 보통 throw 연산자와 함께 사용한다.

### Symbol()
- 심벌은 충돌 염려 없이 객체 프로퍼티로 사용 가능한, 특별한 **유일값이다.**
- 심벌은 프로퍼티명으로 사용할 수 있으나, 프로그램 코드나 개발자 콘솔 창에서 심벌의 실제 값을 보거나 접근하는건 불가능하다.
- ES6에는 심벌 몇 개가 미리 정의되어 있는데 Symbol.create, Symbol.iterator 식으로 Symbol 함수 객체의 정적 프로퍼티로 접근한다.
  ```javascript
  obj[Symbol.iterator] = function() { /*...*/ }
  ```
- 심벌을 직접 정의하려면 Symbol() 네이티브를 사용한다. Symbol()은 앞에 new를 붙이면 에러가 나는 유일한 네이티브 생성자이다.
  ```javascript
  var mysym = Symbol("my own symbol")
  mysym;                              // Symbol(my own symbol)
  mysym.toString();                   // "Symbol(my own symbol)"
  typeof mysym;                       // "symbol"

  var a = {};
  a[mysym] = "foobar";

  Object.getOwnPropertySymbols(a);
  //  [Symbol(my own symbol)]
  ```
- 건드리지마세요! 용도의 언더스코어(_)가 앞에 붙은 프로퍼티 명도 언젠가는 심벌에 의해 완전히 대체될 가능성이 높다.

## 네이티브 프로토타입
- 내장 네이티브 생성자는 각자의 `.prototype` 객체를 가진다.
- i.e. `Array.prototype`, `String.prototype`, ...
- prototype 객체에는 해당 객체의 하위 타입별로 고유한 로직이 담겨 있다.
- 문자열 원시 값을 박싱한 것까지 포함하여 모든 String 객체는 기본적으로 `String.prototype` 객체에 정의된 메서드에 접근할 수 있다.
  - `String.prototype.XYZ` 와 같은 것을 `String#XYZ` 처럼 줄여 쓰는 것이 관례
- i.e. String의 경우
  - `String#indexOf()`      : 문자열에서 특정 문자의 위치를 검색
  - `String#charAt()`       : 문자열에서 특정 위치의 문자를 반환
  - `String#substr()`       : 문자열의 일부를 새로운 문자열로 추출
  - `String#toUpperCase()`  : 대문자로 변환된 새로운 문자열을 생성
  - `String#trim()`         : 앞/뒤 공란이 제거된 새로운 문자열 생성
  > 프로토타입 위임 덕분에 모든 문자열이 이 메서드들을 사용할 수 있다.
  > 
  > 이 중 문자열 값을 변경하는 메서드는 없다. 수정이 일어나면 늘 기존 값으로부터 새로운 값을 생성한다.
- 모든 함수는 Function.prototype에 정의된 apply(), call(), bind() 메서드를 사용할 수 있다.

### 프로토타입은 디폴트다.
- 변수에 적잘한 타입의 값이 할당되지 않은 상태에서 Function.prototype (빈 함수), RegExp.prototype (빈 정규식), Array.prototype (빈 배열)은 모두 멋진 디폴트 값이다.
  ```javascript
  function isThisCool(vals, fn, rx) {
    vals = vals || Array.prototype;
    fn = fn || Function.prototype;
    rx = rx || RegExp.prototype;

    return rx.test(
      vals.map(fn).join("")
    );
  }

  isThisCool();     // true

  isThisCool(
    ["a", "b", "c"],
    function(v) {
      return v.toUpperCase();
    },
    /D/
  );                //false
  ```
  - .prototype는 이미 생성되어 내장된 상태이므로 단 한번만 생성된다.
  - 그러나 [], function() {}, /(?:)/를 디폴트 값으로 사용하면, (엔진 구현에 따라 조금씩 다르지만) isThisCool()을 호출할 때마다 디폴트 값을 다시 생성(그리고 나중에 가비지컬렉팅)하므로 그만큼 메모리/CPU가 낭비된다.
  - 그리고 이후에 변경될 디폴트 값으로 Array.prototype을 사용하는 일이 없도록 유의해야한다.


## 참고 : 프로토타입 바로 잡기
- 어떤 함수를 만들면 그 함수에 대한 prototype객체가 만들어진다. 아래와같이
  ```javascript
  var a = function() {
    return "abc";
  }

  // a.prototype이 생성됨
  ```
- 위에서 생성된 a.prototype 객체는 Function.prototype과는 다를 객체이다. 즉, 메모리에서 서로 다른곳에 자리 잡고 있는 객체들이다.
- Function.prototype은 스크립트가 엔진에 의해 시작되면 기본적으로 메모리에 올라가 있는 **기본 프로토타입 객체**이다.
- 그러므로 절대 이와 같은 네이티브 프토토타입 객체를 변경하지 않도록 유의하자!!