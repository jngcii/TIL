# 객체 (Object)

###### 2020.04.30

## 구문

- 객체는 **선언적(리터럴) 형식**과 **생성자 형식** 두 가지로 정의한다.
- 리터럴 형식
  ```javascript
  var myObj = {
    key: value
    // ...
  }
  ```
- 생성자 형식
  ```javascript
  var myObj = new Object();
  myObj.key = value;
  ```

## 타입
- 자바스크립트 객체의 7개 주요 타입은 다음과 같다.
  - null
  - undefined
  - boolean
  - number
  - string
  - object
  - symbol
- *자바스크립트는 모든 것이 객체다* 라는 말은 옳지 않다.
- 단순 원시 타입(string, number, boolean, null, undefined)은 객체가 아니다.
- **복합원시타입**이라는 독특한 객체 하위 타입이 있다. (function, array)

### 내장 객체
- 객체 하위 타입
- 일부는 이름만 보면 대응되는 단순 원시 타입과 직접 연관되어 보이지만 실제 관계는 복잡하다.
  - String
  - Number
  - Boolean
  - Object
  - Function
  - Array
  - Date
  - RegExp
  - Error
- 내장 객체는 진짜 타입처럼 보이는 데다 자바의 String 클래스처럼 타 언어와 유사한 겉모습 때문에 클래스처럼 느껴진다.
- 하지만 단지 자바스크립트의 **내장 함수**일 뿐이다.
  ```javascript
  var strPrimitive = "나는 문자열아야!";
  typeof strPrimitive;                          // "string"
  strPrimitive instanceof String                // false

  var strObject  = new String("나는 문자열이야!");
  typeof strObject;                             // "object"
  strObject instanceof String;                  // true

  // 객체 하위 타입을 확인한다.
  Object.prototype.toString.call(strObject);    // [object String]
  ```
  - `Object.prototype.toString` 부분은 `toString()` 메서드의 기본 구현체를 빌려서 내부 하위 타입을 조사한다.
  - 그 결과 `strObject`가 `String` 생성자에 의해 만들어진 객체임을 알 수 있다.
  - `"나는 문자열아야!"`라는 원시 값은 객체가 아닌 원시 리터럴이며 불변값이다.
  - 문자 개수를 세는 등 문자별로 접근할 때엔 String 객체가 필요하다.
  - 자바스크립트 엔진은 상황에 맞게 문자열 원시 값을 String 객체로 자동 강제변환한다. (박싱)

## 내용
- 객체는 특정한 위치에 저장된 모든 타입의 값(프로퍼티)로 내용이 채워진다.
- 객체 컨테이너에는 프로퍼티 값이 있는 곳을 가리키는 포인터 역할을 하는 프로퍼티 명이 담겨있다.
  ```javascript
  var myObject = {
    a: 2
  };
  myObject.a;       // 2
  myObject["a"];    // 2
  ```
  > `myObject` 객체에서 `a` 위치의 값에 접근하려면 `.`(프로퍼티 접근) 연산자 또는 `[]`(키 접근) 연산자를 사용한다.

### 계산된 프로퍼티명
```javascript
var prefix = "foo";
var myObject = {
  [prefix + "bar"]: "hello",
  [prefix + "baz"]: "world",
};

myObject["foobar"]; // hello
myObject["foobaz"]; // world
```

### 프로퍼티 vs 메서드
- 어떤 개발자는 접근하려는 객체 프로퍼티 값이 함수면 어떤 식으로든 구별하려고 한다.
- 하지만 엄밀히 말해 함수는 결코 객체에 속하는 것이 아니다.
- `this` 레퍼런스를 스스로 지닌 함수도 있고 호출부의 객체 레퍼런스를 가리킬 때도 있지만 그렇다고 이렇게 사용되는 함수가 다른 함수들보다 메서드답다라고 말하는건 이상하다.
  ```javascript
  function foo() {
    console.log("foo");
  }

  var someFoo = foo;    // 'foo'에 대한 변수 레퍼런스
  var myObject = {
    someFoo: foo
  };
  foo;                  // function foo() { ... }
  someFoo;              // function foo() { ... }
  myObject.someFoo;     // function foo() { ... }
  ```
  > `someFoo`나 `myObject.someFoo` 모두 같은 함수를 가리키는 개별 레퍼런스일 뿐, 뭔가 특별한 다른 객체가 소유한 함수라는 의미는 아니다.
  > 
  > `foo()` 안에 `this` 레퍼런스가 정의되어 있다면 `myObject.someFoo`에서 발생할 암시적 바인딩이 두 레퍼런스의 유일한 차이점이다.

### 배열
- 배열도 `[]`로 접근하는 형태이지만 이미 언급한 대로 값을 저장하는 방법과 장소가 더 체계적이다.
- 배열은 인덱스로 표기된 위치에 값을 저장한다.
- **배열은 그냥 우리가 아는 것처럼 쓰는게 가장 바람직하고 쓸데없는 짓은 하지말자**

### 객체 복사
```javascript
function anotherFunction() { /* ... */ }

var anotherObject = {
  c: true
};

var anotherArray = [];

var myObject = {
  a: 2,
  b: anotherObject,   // 사본이 아닌 레퍼런스!
  c: anotherArray,    // 역시 레퍼런스!
  d: anotherFunction
};
```
- 얕은 복사 : 복사 후 생성된 새 객체의 a 프로퍼티는 원래 값 2가 그대로 복사되지만 b, c, d 프로퍼티는 원 객체의 레퍼런스와 같은 대상을 가리키는 또 다른 레퍼런스다. 
- 깊은 복사 : `myObject`는 물론이고 `anotherObject`와 `anotherArray`까지 모조리 복사한다.
- 얕은 복사는 이해하기 쉽고 별다른 이슈가 없기에 ES6부터는 `Object.assign()` 메서드를 제공한다.
- 깊은 복사는자바스크립트의 난관이다. ㅠ

### 프로퍼티 서술자
- ES5 부터 모든 프로퍼티는 프로퍼티 서술자로 표현된다.
  ```javascript
  var myObject = {
    a: 2
  };

  Object.getOwnPropertyDescriptor(myObject, "a");
  // {
  //   value: 2,
  //   writable: true,
  //   enumerable: true,
  //   configurable: true
  // }
  }
  ```
  - 평범한 객체 프로퍼티 `a`의 프로퍼티 서술자를 조회해보니 2 말고도 `writable`, `enumerable`, `configurable` 세 가지 특성이 더 있다.
- `Object.defineProperty()`로 새로운 프로퍼티를 추가하거나 기존 프로퍼티의 특성을 원하느 대로 수정할 수 있다.
  ```javascript
  var myObject = {};
  Object.defineProperty(myObject, "a", {
    value: 2,
    writable: true,
    configurable: true,
    enumerable: true
  });

  myObject.a; // 2
  ```
- **`writable`**
  - 쓰기 가능은 `writable`로 조정한다.
  - 쓰기금지된 값을 수정하려면 조용히 실패하고 엄격모드에선 에러가 난다(`TypeError`).
- **`configurable`**
  - 설정 가능은 `configurable`로 조정한다.
  - 설정 불가한 프로퍼티의 서술자를 변경하려고 하면 (`defineProperty()` 메서드 호출 시) 엄격모드와 상관없이 `TypeError`가 발생한다.
  - **`configurable`은 일단 false가 되면 돌아올수 없는 강을 건너게 되어 절대로 복구되지 않으니 유의하자**
  - `configurable: false`로 설정하면 이미 `delete` 연산자로 존재하는 프로퍼티 삭제도 금지된다. (이건 조용히 실패)
- **`enumerable`**
  - `for ... in` 루프처럼 객체 프로퍼티를 열거하는 구문에서 해당 프로퍼티의 표출 여부를 나타낸다.
  - `enumerable: false`로 지정된 프로퍼티는 접근할 수는 있지만 루프 구문에서 감춰진다.
  - 보통 사용자 정의 프로퍼티는 `enumerable: true`가 기본값이어서 열거할 수 있다.

### 불변성
> 프로퍼티/객체가 우연이든 의도적이든 변경되지 않게 해야 할 경우가 있다.

1. 객체 상수
  - `writable: false`와 `configurable: false`를 같이 쓰면 객체 프로퍼티를 상수처럼 쓸 수 있다.
  ```javascript
  var myObject = {};
  Object.defineProperty(myObject, "FAVORITE_NUMBER", {
    value: 42,
    writable: false,
    configrable: false
  })
  ```  
2. 확장 금지
  - 객체에 더는 프로퍼티를 추가할 수 없게 차단하고 현재 프로퍼티는 있는 그대로 놔두고 싶을때 `Object.preventExtension()`을 호출한다.
  ```javascript
  var myObject = {
    a: 2
  };
  Object.preventExtensions(myObject);
  myObject.b = 3;
  myObject.b; // undefined
  ```  
  > 비엄격 모드에선 조용히 실패하고 엄격 모드에선 `TypeError`가 발생한다.
3. 봉인
  - `Object.seal()`은 봉인된 객체를 생성한다.
  - 즉, 어떤 객체에 대해 `Object.preventExtensions()`를 실행하고 프로퍼티를 전부 `configurable: false` 처리한다.
4. 동결
  - `Object.freeze()`은 객체를 모두 꽁꽁 얼린다.
  - 즉, 앞서 설명한 `Object.seal()`을 적용하고 데이터 접근자 프로퍼티를 모두 `writable: false` 처리해서 값도 못바꾸게 한다.
  ```javascript
  var myObject = {
    a: 2
  };
  Object.preventExtensions(myObject);
  myObject.b = 3;
  myObject.b; // undefined
  ```

### [[Get]]
```javascript
var myObject = {
  a: 2
};

myObject.a;     // 2
```
- 프로퍼티에 접근하기까지 세부 과정은 미묘하면서 중요하다.
- `myObject.a`는 누가 봐도 프로퍼티 접근이지만 보이는 것처럼 a란 이름의 프로퍼티를 myObject에서 찾지 않는다.
- 명세에 따르면 실제로 이 코드는 `myObject`에 대해 `[[Get]]` 연산을 한다. (`[[Get]]()` 같은 함수 호출)
- 기본적으로 `[[Get]]` 연산은 주어진 이름의 프로퍼티를 먼저 찾아보고 있으면 그 값을 반환한다.
- 프로퍼티를 찾아보고 없으면 `[[Prototype]]` 연쇄 순회를 시작한다.
- 어떻게해도 찾을 수 없으면 `[[Get]]` 연산은 `undefined`를 반환한다.

### [[Put]]
- 언뜻 보기에 객체 프로퍼티에 값을 할당하는 일은 그저 `[[Put]]`을 호출하여 주어진 객체에 프로퍼티를 세팅/생성하는 일이 전부일 것 같지만, 실제로는 좀 더 복잡하다.
  1. 프로퍼티가 접근 서술자인가? 맞으면 세터를 호출한다.
  2. 프로퍼티가 `writable: false`인데 데이터 서술자인가? 맞으면 비엄격 모드에선 조용히 실패하고 엄격 모드는 `TypeError`를 낸다.
  3. 이 외에는 프로퍼티에 해당 값을 세팅한다.

### 게터와 세터
- `[[Put]]`과 `[[Get]]` 기본 연산은 이미 존재하거나 전혀 새로운 프로퍼티에 값을 세팅하거나 기존 프로퍼티로부터 값을 조회하는 역할을 각각 담당한다.
- ES5 부터는 게터/세터를 통해 프로퍼티 수준에서 이러한 기본 로직을 오버라이드할 수 있다.
- **게터/세터는 각각 실제로 값을 가져오는/세팅하는 감춰진 함수를 호출하는 프로퍼티다.**
- 프로퍼티가 게터 또는 세터 어느 한쪽이거나 동시에 게터/세터가 될 수 있게 정의한 것을 **접근서술자**라고 한다.
  ```javascript
  var myObject = {
    // 'a'의 게터를 정의한다.
    get a() {
      return 2;
    }
  };

  Object.defineProperty(
    myObject,
    "b",
    {
      // 'b'의 게터를 정의한다.
      get: function() { return this.a * 2 },

      // 'b'가 객체 프로퍼티로 확실히 표시되게 한다.
      enumerable: true
    }
  );

  myObject.a = 3;

  myObject.a;   // 2
  myObject.b;   // 4
  ```
  > a의 게터가 정의되어 있으므로 할당문으로 값을 세팅하려고 하면 에러 없이 조용히 무시된다.
  > 
  > 세터가 있어도 커스텀 게터가 2만 반환하게 하드 코딩되어 있어서 세팅은 있으나 마나다.
- 게터와 세터는 항상 둘 다 선언하는 것이 좋다.
- 한쪽만 선언하면 예외의 결과가 나올 수 있다.
  ```javascript
  var myObject = {
    get a() {
      return this._a_;
    },

    set a(val) {
      this._a_ = val * 2;
    }
  };

  myObject.a = 2;
  myObject.a;       // 4
  ```

### 존재 확인
- 객체에 어떤 프로퍼티가 존재하는지 굳이 프로퍼티 값을 얻지 않고도 확인하는 방법!
- `Object.prototype.hasOwnProperty.call(myObject, "a")`

### 열거 가능확인
- `propertyIsEnumerable()`은 어떤 프로퍼티가 해당 객체의 직속 프로퍼티인 동시에 `enumerable: true`인지 검사한다.
- `myObject.propertyIsEnumerable("a");`


## 순회
- `for ... in` 루프는 열거 가능한 객체 프로퍼티를 (`[[Prototype]]` 연쇄도 포함하여) 차례로 순회한다.
```javascript
var mayArray = [1, 2, 3];
for (var i=0; i<myArray.length; i++) {
  console.log(myArray[i]);
}
// 1 2 3
```
- 이 코드는 인덱스를 순회하면서 해당 값(myArray[i])을 사용할 뿐 값 자체를 순회하는 것은 아니다.
- ES5 부터는 `forEach()`, `every()`, `some()` 등의 배열 관련 순회 헬퍼가 도입됐다.
- 이 함수들은 배열의 각 원소에 적용할 콜백 함수를 인자로 받으며, 원소별로 반환값을 처리하는 로직만 다르다.
  - `forEach()`는 배열 전체 값을 순회하지만 콜백 함수의 반환 값은 무시한다.
  - `every()`는 배열 끝까지 또는 콜백 함수가 false(또는 falsy한 값)을 반환할 때까지 순회한다.
  - `some()`은이와 정반대로 배열 끝까지 또는 콜백 함수가 true(또는 truthy한 값)를 반환할 때까지 순회한다.
- ES6부터 배열 순회용 `for ... of`구문을 제공한다.
  ```javascript
  var myArray = [1, 2, 3];
  for (var v of myArray) {
    console.log(v);
  }
  // 1
  // 2
  // 3
  ```
  - `for ... of` 루프는 순회할 원소의 순회자 객체 (`@@iterator`라는 기본 내부 함수)가 있어야 한다.
  - 순회당 한 번씩 이 순회자 객체의 `next()` 메서드를 호출하여 연속적으로 반환 값을 순회한다.
  - 배열은 `@@iterator`가 내장된 덕분에 손쉽게 `for ... of` 로푸를 사용할 수 있다.
    ```javascript
    var myArray = [1, 2, 3];
    var it = myArray[Symbol.iterator]();

    it.next();  // { value: 1, done: false }
    it.next();  // { value: 2, done: false }
    it.next();  // { value: 3, done: false }
    it.next();  // { done: true }
    ```