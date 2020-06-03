# 작동 위임

###### 2020.06.03

> 자바스크립트의 무한한 가능성을 이끌어낼 가장 중요한 핵심 기능이자 실제적인 체계는 전적으로 **객체를 다른 객체와 연결하는 것**에서 비롯된다.

## I. 위임 지향 디자인

### 1. 클래스 이론
- 클래스 디자인 패턴에서는 상속의 진가를 발휘하기 위해 될 수 있으면 메서드를 오버라이드할 것을 권장하고 작동 추가뿐 아니라 때에 따라서 오버라이드 이전 원본 메서드를 super 키워드로 호출할 수 있게 지원한다.

### 2. 위임 이론
- 태스크별로 객체를 정의하여 고유한 데이터와 작동을 정의하고 상위 객체에 연결해 필요할 때 특정 테스크 객체가 상위 객체를 위임하도록 작성한다.
  ```js
  Task = {
    setID: function(ID) { this.id = ID; },
    outputID: function() { console.log(this.id); },
  };

  XYZ = Object.create(Task);
  XYZ.prepareTask = function(ID, Label) {
    this.setID(ID);
    this.label = Label;
  };

  XYZ.outputTaskDetails = function() {
      this.outputID();
      console.log(this.label);
  }

  ABC = Object.create(Task);
  // ABC = ...
  ```
> 상호위임(허용되지 않음) : 복수의 객체가 서로 위임하고 있는 상태 -> 에러발생

### 3. 멘탈 모델 비교

#### 1) OOP 스타일
```js
function Foo(who) {
    this.me = who;
}
Foo.prototype.identify = function () {
    return "I am " + this.me;
};
function Bar(who) {
    Foo.call(this, who);
}
Bar.prototype = Object.create(Foo.prototype);
Bar.prototype.speak = function() {
    alert("Hello, ", this.identify() + ".");
};

var b1 = new Bar("b1");
var b2 = new Bar("b2");

b1.speak();
b2.speak();
```

#### 2) OLOO 스타일
```js
Foo = {
    init: function(who) {
        this.me = who;
    },
    identify: function() {
        return "I am " + this.me;
    },
};

Bar = Object.create(Foo);
Bar.speak = function() {
    alert("Hello, " + this.identify() + ".");
};

var b1 = Object.create(Bar);
b1.init("b1");
var b2 = Object.create(Bar);
b2.init("b2");

b1.speak();
b2.speak();
```