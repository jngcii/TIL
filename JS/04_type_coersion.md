# 강제 변환 (Type Coersion)

###### 2020.03.20

## 값 변환
- 어떤 값을 다른 타입의 값으로 바꾸는 과정이 명시적이면 **타입캐스팅**, 암시적이면 **강제변환**이라고 한다.
- 자바스크립트에는 암시적 강제변환과 명시적 강제변환이 있다.
- 명시적 강제변환은 코드만 봐도 의도적으로 타입변환을 일으킨다는 사실이 명백하다.
- 암시적 강제변환은 다른 작업 도중 불분명한 부수 효과로부터 발생하는 타입변환이다.
  ```javascript
  var a = 42;
  var b = a + "";     // 암시적 강제변환
  var c = String(a);  // 명시적 강제변환
  ```

## 추상 연산
> 어떻게 값이 문자열, 숫자, 불리언 등의 타입이 되는지 그 기본 규칙!!
### ToString
- '문자열이 아닌 값 -> 문자열' 변환 작업은 ToString 추상 연산 로직이 담당한다. 내장 원시 값은 본연의 문자열화 방법이 정해져 있다.
- 일반 객체는 특별히 지정하지 않으면, 기본적으로 Object.prototype.toStirng() 메서드가 내부 [[Class]]를 반환한다. ("[object Object]")
- 자신의 toString() 메서드를 가진 객체는 prototype연쇄를 따라기 전에 먼저 자신의 toString()메서드를 사용하므로, 이 메서드가 기본 호출되어 toString()을 대체한다.
- 배열은 기본적으로 재정의된 toString()이 있다. 문자열 변환 시 모든 원소 값이 콤마(,)로 분리된 형태로 이어진다.
  ```javascript
  var a = [1, 2, 3];
  a.toString();   // "1, 2, 3"
  ```

### JSON.stringify()
- ToString은 JSON.stringify() 유틸리티를 사용하여 어떤 값을 JSON 문자열로 직렬화하는 문제와도 연관된다.
- JSON.stringify()는 인자가 undefined, 함수, 심벌 값이면 자동으로 누락시키며 이런 값들이 만약 배열에 포함되어 있으면, (인덱스 정보가 바뀌지 않도록) null로 바꿔준다. 객체 프로퍼티에 있으면 간단히 지워버린다.
  ```javascript
  JSON.stringify(undefined);    // undefined
  JSON.stringify(function(){}); // undefined

  JSON.stringify(
    [1, undefined, function(){}, 4]
  );                            // "[1, null, null, 4]"

  JSON.stringify(
    { a: 2, b: function(){} }
  );                            // "{"a":2}"
  ```
- toJSON() 메서드가 정의되어 있다면, 먼저 이 메서드를 호출하여 직렬화한 값을 반환한다.
  ```javascript
  var o = {};

  var a = {
    b: 42,
    c: o,
    d: function(){}
  };

  // 'a'를 환형 참조 객체로 만든다.
  // a.c.e === a
  o.e = a;

  // 환형 참조 객체는 JSON 문자열화 시 에러가 난다.
  // JSON.stringify(a);

  // toJSON 함수가 호출되는 호출부가 a이므로 this는 a
  a.toJSON = function() {
    // 직렬화에 프로퍼티 'b'만 포함시킨다.
    return { b: this.b };
  };

  JSON.stringify(a);   // "{"b":42}"
  ```
- JSON.stringify()가 직접적인 강제변환 형식은 아니지만, 두가지 이유로 ToString강제 변환과 연관된다.
  1. 문자열, 숫자, 불리언, null 값이 JSON으로 문자열화하는 방식은 ToString 추상 연산의 규칙에 따른 문자열 값으로 강제변환되는 방식과 동일하다.
  2. JSON.stringify()에 전달한 객체가 자체 toJSON() 메서드를 갖고 있다면, 문자열화 전 toJSON()가 자동으로 호출되어 JSON안전 값으로 '강제변환'된다.


### ToNumber
- 숫자 아닌 값 -> 수식 연산이 가능한 숫자 변환 로직
  - true는 1로
  - false는 0으로
  - undefined는 NaN으로
  - nulldms 0으로
- 문자열 값에 ToNumber를 적용하면, 대부분 숫자 리터럴 규칙/구문과 비슷하게 작동한다.
- 변환이 실패하면 결과는 NaN이다.
- 객체, 배열은 일단 동등한 원시 값으로 변환 후, 그 결괏값을 ToNumber 규칙에 의해 강제변환한다.
  - 동등한 원시 값으로 바꾸기 위해, ToPrimitive 추상 연산 과정에서 해당 객체가 valueOf() 메서드를 구현했는지 확인한다.
  - valueOf()를 쓸 수 있고 반환 값이 원시 값이면 그대로 강제벼환하되, 그렇지 않을 경우 toString()을 이용하여 강제변환한다.
  - 어찌해도 원시 값으로 바꿀 수 없을 땐 TypeError오류를 던진다.
    ```javascript
    var a = {
      valueOf: function() {
        return "42";
      }
    };

    var b = {
      toString: function() {
        return "42";
      }
    }

    var c = [4, 2];
    c.toString = function() {
      return this.join("");   // "42"
    }

    Number(a);        // 42
    Number(b);        // 42
    Number(c);        // 42
    Number("");       // 0
    Number([]);       // 0
    Number(["abc"])   // NaN
    ```

### ToBoolean
- 흔히들 1과 0이 각각 true, false에 해당한다고 생각하는데, 다른 언어에서는 그럴지 몰라도 **자바스크립트에서는 숫자는 숫자고, 불리언은 불리언으로 서로 별개다!!!!!**
- 1을 true로, 0을 false로 강제변환할 수는 있지만 그렇다고 두 값이 똑같은 건 아니다.
- true/false가 아닌 값을 불리언에 맞는 값으로 강제변환했을 때, 이 값들은 어떻게 동작할까
- 자바스크립트의 모든 값은 다음 둘 중 하나이다.
  - 불리언으로 강제변환되면 false가 되는 값
  - 나머지
#### falsy 값
- 불리언으로 강제변환 시 false가 되는 몇 개 안되는 특별한 값들이 자바스크립트 명세에 이미 정의되어 있다.
  - undefined
  - null
  - false
  - +0, -o, NaN
  - ""
  - 이게 전부. 더이사 없음.
- 정리하자면 이렇다.
  |인자 타입 | 결괏값|
  |---|---|
  |Undefined | false|
  |Null | false |
  |Boolean | 인자 값과 동일 (변환 안함) 
  |Number | 인자가 +0, -0, NaN이면 false, 그 외에는 true |
  |String | 인자가 공백 문자열(length가 0)이면 false, 그 외에는 true |
  |Object | true |

#### Falsy 객체
- 모든 객체는 truthy한데 Falsy 객체...?
- 일반적인 자바스크립트의 의미뿐만 아니라 브라우저만의 특이한 작동방식을 가진 값을 생성하는 경우가 있는데, 이것이 바로 'falsy 객체'의 정체이다.
- falsy 객체는 겉보기엔 평범한 객체처럼 작동할 것 같지만 불리언으로 강제변환하면 false이다.

## 명시적 강제변환
- 명시적 강제변환은 분명하고 확실한 타입변환이다.
### 문자열 <-> 숫자
- String()과 Number() 함수를 이용하는데, **앞에 new 키워드가 붙지 않기때문에 객체 래퍼를 생성하는 것이 아니다!!!!**
- ToString 추상 연산 로직에 따라 String()은 값을 받아 원시 문자열로 강제 변환한다.
- Number() 역시 마찬가지로 ToNumber 추상 연산 로직에 의해 어떤 값이든 원시 숫자 값으로 강제변환한다.
- 또다른 명시적 타입변환
  ```javascript
  var a = 42;
  var b = a.toString();

  var c = "3.14";
  var d = +c;

  b;    // "42";
  d;    // 3.14;
  ```
  - a.toString()은 겉보기엔 명시적이지만, 몇 가지 암시적인 요소가 감춰져있다.
  - 원시 값 42에는 toString() 메서드가 없으므로 엔진은 toString()를 사용할 수 있게 자동으로 42를 객체 래퍼로 박싱한다.

### 날짜 -> 숫자
- Date 객체에서 숫자로 강제변환하기 위해서는 `+`단항 연산자가 사용된다.
  ```javascript
  var d = new Date("Mon, 18 Aug 2014 08:53:06 CDT");
  +d;   // 1408369975000

  // 다음과 같이 현재 시각을 타임스탬프로 바꿀 때 관용적으로 사용하는 방법이다.
  var timestamp = +new Date();

  // 하지만 이 방법이 더 좋다.
  var timestamp = new Date().getTime();

  // 그리고 이 방법이 제이이이이이이이일 좋다!!
  var timestamp = Date.now();
  ```
  - 현재 타임스탬프는 `Date.now()`로, 그 외 특정 날짜/시간 타임스탬프는 `new Date().getTime()`을 대신 쓰도록 하자

### 틸드(~)
- `~` 연산자는 먼저 32비트 숫자로 강제변환한 후 NOT 연산을 한다. (각 비트를 거꾸로 뒤집는다. - 보수 구하기)
  ```javascript
  ~42;  // -(42+1) ==> -43
  ```