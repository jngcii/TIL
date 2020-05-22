# 클래스와 객체의 혼합
> 클래스 지향 디자인패턴

###### 2020.05.21

## I. 클래스 이론

### 1. 클래스 디자인 패턴
- 순회자, 관찰자, 팩토리, 싱글톤 등의 유명한 객체 지향 디자인 패턴들과 같이 클래스 역시 디자인 패턴의 일종이다.
- 자바와 같은 몇몇 언어는 선택의 여지가 없이 모든게 클래스이고, C/C++이나 PHP 같은 언어는 절차적 구문과 클래스 지향 구문을 함께 제공하므로 개발자가 스타일을 선택할 수 있다.

### 2. 자바스크립트 클래스
- 자바스크립트에는 클래스가 없다!
- `new`나 `instanceof` 등 클래스와 비슷하게 생긴 구문도 있고 ES6부터는 아예 `class`라는 키워드가 명세에 정식적으로 추가됐지만, **사실 클래스는 없다.**
- 자바스크립트의 클래스는 여타 언어의 클래스와 달리 그저 모조품에 지나지 않는다.

## II. 클래스 체계
- 스택은 구체적인 객체를 만들기 위해 건축 도면이나 붕어빵 틀처럼 만들어져있는 틀이다.
- 생성자
  - 인스턴스는 보통 클래스명과 같은 이름의 생성자라는 특별한 메서드로 생성한다.
  - 새로운 인스턴스를 생성할 거라는 신호를 엔진이 인지할 수 있도록 항상 `new` 키워드를 앞에 붙여 생성자를 호출한다.

## III. 클래스 상속
- 클래스 지향 언어는 자체로 인스턴스화할 수 있는 클래스는 물론이고 첫 번째 클래스를 상속받은 두 번째 클래스를 정의할 수 있다. (부모클래스와 자식클래스)

### 1. 다형성
- 한 메서드가 상위 수준의 상속 체계에서 다른 메서드를 참조할 수 있게 해주는 아이디어
- 대부분의 언어에서는 `super` 키워드를 사용한다.
- 같은 이름의 메서드가 상속 연쇄의 수준별로 다르게 구현되어 있고 이 중 어떤 메서드가 적절한 호출 대상인지 자동으로 선택하는 것 또한 다형성의 특징이다.

### 2. 다중 상속
- 일부 클래스 지향 언어에서는 복수의 부모 클래스에서 상속받을 수 있다.
- 다중 상속은 부모 클래스 각각의 정의가 자식 클래스로 복사된다는 의미이다.

## IV. 믹스인
- 자바스크립트 객체는 상속받거나 인스턴스화해도 자동으로 복사작업이 일어나지 않는다.
- 자바스크립트엔 인스턴스로 만들 클래스란 개념 자체가 없고 오직 객체만 있다.
- 객체는 복사되는게 아니라 서로 연결된다.
- **믹스인**은 자바스크립트에서 누락된 클래스 복사 기능을 흉내 낸 것으로, 명시적 믹스인과 암시적 믹스인 두 타입이 있다.

### 1. 명시적 믹스인
```js
function mixin(sourceObj, targetObj) {
  for (var key in sourceObj) {
    if (!key in targetObj) {
      targetObj[key] = sourceObj[key];
    }
  }
  return targetObj;
}

var Vehicle = {
  engines: 1,
  ignition: function() {
    console.log("엔진을 켠다.")
  },
  drive: function() {
    this.ignition();
    console.log("방향을 맞추고 앞으로 간다!");
  }
};

var Car = mixin(Vehicle, {
  wheels: 4,
  drive: function() {
    Vehicle.drive.call(this);
    console.log(this.wheels + "개의 바퀴로 굴러간다!");
  }
});
```
- `Car`에는 `Vehicle`에서 복사한 프로퍼티와 함수 사본이 있다.
- 함수가 실제로 복사된 것이 아니라 원본 함수를 가리키는 레퍼런스만 복사된 것이다.
- `Car`에는 이미 자체 `drive` 프로퍼티가 있으므로 이 프로퍼티 레퍼런스는 오버라이드되지 않는다.

#### 다형성 재고
- `Vehicle.drive.call(this)`와 같은 코드를 명시적 의사다형성이라 부른다.
- 자바스크립트는 상대적 다형성을 제공하지 않는다.
- 따라서 `drive()`란 이름의 함수가 `Vehicle`과 `Car` 양쪽에 모두 있을 때 이 둘을 구별해서 호출하려면 절대적인 레퍼런스를 이용할 수밖에 없고 그래서 명시적으로 `Vehicle` 객체의 이름을 지정하여 `drive()` 함수를 호출한 것이다.
- 하지만, `Vehicle.drive()`로 함수를 호출하면 `this`는 `Car` 객체가 아닌 `Vehicle` 객체와 바인딩 되는데, 이때문에 `.call(this)`를 붙여 `drive()`를 `Car` 객체의 콘텍스트로 실행하도록 강제한 것이다.
- 명시적 의사다형성은 장점보다 비용이 훨씬 더 많이 들기 때문에 가능한 한 쓰지 않는게 좋다.

### 2. 암시적 믹스인
```js
var Something = {
  cool: function() {
    this.greeting = "Hello World";
    this.count = this.count ? this.count + 1 : 1;
  }
};

Something.cool();
Something.greeting();
Something.count();

var Another = {
  cool: function() {
    Something.cool.call(this);
  }
};

Another.cool();
Another.greeting();
Another.count;
```
- 가장 일반적인 생성자 호출 또는 메서드 호출 시 `Someting.cool.call(this)`를 하면 `Something.cool()` 함수를 본질적으로 빌려와서 `Another` 콘텍스트로 호출한다.
- 결국 `Something.call()`의 할당은 `Something`이 아닌 `Another`다. 따라서 `Something`의 작동을 `Another`와 섞은 셈이다.
- `this` 재바인딩을 십분 활용한 이런 유형의 테크닉은 `Something.cool.call(this)`같은 호출이 상대적 레퍼런스가 되지 않아 불안정하므로 사용할 때 신중히 해야한다.
- 대부분은 깔끔하고 관리하기 쉬운 코드를 유지하기 위해 쓰지 않는 편이 좋다.