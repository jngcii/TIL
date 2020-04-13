# 문법

###### 2020.03.30

## 문(Statement) vs 식(Expression)
```javascript
var a = 3 * 6;
var b = a;
b;
```
- 식 : `3 * 6`, `b = a`, `b`, ...
  - 할당 표현식 : `a = 3 * 6`, `b = a`
- 문 : 세 줄이 모두 각가 표현식이 포함된 문
  - 선언문 ( 변수를 선언 ) : `var a = 3 * 6;`, `var b = a;`
  - 표현식문 : `b;`

### I. 문의 완료값
> 모든 문은 완료값을 가진다.
- `var b = a;`문의 완료값은 ? `undefined`
  - `b = a`는 할당 이후의 값이 완료 값이지만, var 문 자체의 완료 값은 `undefined`
- 아래의 완료값은 ?
  ```javascript
  var b;

  if (true) {
    b = 4 + 38;
  }
  ```
  - 블록 내의 마지막 문 b = 4 + 38의 완료값이 42이므로 if 블록의 완료 값도 42를 반환
  - 즉, ***블록의 완료값은 내부에 있는 마지막 문의 값을 암시적으로 반환한 값***

### II. 표현식의 부수효과
- 대부분의 표현식에는 부수효과가 없다.
- 다음의 함수 호출 표현식은 부수효과를 가진 표현식의 전형적인 예이다.
  ```javascript
  function foo() {
    a = a + 1;
  }

  var a = 1;
  foo();        // 결괏값 : 'undefined', 부수 효과 : 'a'가 변경됨.
  ```
  ```javascript
  var a = 42;
  var b = a++;
  ```
  ```javascript
  var a, b, c;
  a = b = c = 42;
  ```

### III. 콘텍스트 규칙
> 자바스크립트 문법 규칙 중에 같은 구문이지만 어디에서 어떤 식으로 사용하냐에 따라 서로 다른 의미를 가지는 경우가 있다.

#### 중괄호
- 자바스크립트에서 중괄호(`{}`)가 나올만한 곳은 두군데이다. (객체 리터럴, 레이블)

#### 레이블
```javascript
{
  foo: bar()
}
```
- 여기서 `{}`는 평범함 코드 블록이다.
- 이 `{}` 코드 블록은 for/while 루프, if 조건 등에 붙어있는 코드 블록과 기능적으로 매우 유사하다.
- `foo: bar()` 구문이 특이한 이유는 **레이블문**이기 때문
- 자바스크립트에는 레이블 점프라는 continue, break 문이 있어서, 선택적으로 어떤 레이블을 받아 실행 흐름을 점프시킨다.
  ```javascript
  foo: for (var i=0; i<4; i++) {
    for (var j=0; j<4; j++) {
      // 두 루프의 반복자가 같을 때마다 바깥쪽 루프를 continue 한다.
      if (j == i) {
        // 다음 순회 시 'foo' 붙은 루프로 점프한다.
        continue foo;
      }

      // 홀수 배수는 건너뛴다.
      if ((j*i)%2 == 1) {
        // 평범한(레이블 없는), 안쪽 루프의 'continue'
        continue;
      }

      console.log(i, j);
    }
  }

  // 1 0
  // 2 0
  // 2 1
  // 3 0
  // 3 2
  ```
  > break foo는 "foo라는 레이블을 빠져나가 그 이후부터 계속하라"

#### 블록
```javascript
[] + {};  // "[object Object]"
{} + [];  //  0
```
- 마치 + 연산자가 첫 번째 피연산자에 따라 다른 결과를 내놓는 것처럼 보인다. 하지만 실제로는 전혀 상관없다!
- 윗줄에서 엔진은 + 연산자 표현식의 {}를 실제 값으로 해석한다.(빈 객체)
  - []는 ""로 강제 변환되고 {}도 문자열 "[object Object]"로 강제 변환된다.
- 아랫줄의 {}는 동떨어진 빈 블록으로 간주된다. 결국 + [] 표현식에서 명시적으로 []를 숫자 0으로 강제변환한다.