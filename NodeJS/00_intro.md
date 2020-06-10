# Node.js intro

###### 2020.06.08

## I. Node.js
- Chrome V8 Javascript 엔진으로 빌드된 Javascript 런타임
- Javascript가 웹브라우저 밖의 환경에서 돌아갈 수 있도록 만든 프로그램

### 1) 런타임
- 컴퓨터 프로그램이 실행되고 있는 동안의 동작

### 2) 런타임 환경
- 컴퓨터가 실행되는 동안 프로세스나 프로그램을 위한 소프트웨어 서비스를 제공하는 가상 머신의 상태
- 실제로 Node.js 안에 VM이 들어있다.

### 3) REPL
- Read, Evaluate, Print, Loop
- 사용자가 친 글을 읽고(Read), 파악하고(Evaluate), 읽은 값을 출력(Print)하는 것을 반복(Loop)한다.


## II. 호출 스택과 이벤트 루프

![](assets/Screen%20Shot%202020-06-10%20at%203.14.51%20PM.png)

- Node.js의 핵심적인 3가지
  - 이벤트 기반
  - 논블로킹 I/O
  - 싱글 스레드

### 1) 호출 스택 (call stack)

#### 예제 1)
```js
function first() {
  second();
  console.log('first');
}

function second() {
  third();
  console.log('second');
}

function third() {
  console.log('third');
}

first();
```
> third > second > first

1. 빈 스택에서 시작한다.
2. fisrt()가 실행된다.
3. first 안의 `second()`가 스택에 쌓인다.
4. second 안의 `third()`가 스택에 쌓인다.
5. third 의 `console.log('third')`가 실행되고 third가 스택에서 빠진다.
6. third가 완료됐으므로 second 안의 `console.log('second')`가 실행되고 second가 스택에서 빠진다.
7. second가 완료됐으므로 first 안의 `console.log('first')`가 실행되고 first가 스택에서 빠지면서 빈 스택이 되어 끝난다.

#### 예제 2)
```js
function run() {
  console.log('run')
}
console.log('start')
setTimeout(run, 0)
console.log('end')
```
> start > end > run

1. `console.log('start')`가 실행되어 콜스택에 들어간후 바로 종료되고 빠진다.
2. `setTimeout`이 실행되어 콜스택에 들어간후 바로 종료되고 빠진다.
  - 다만 여기서 인자로 받는 콜백함수 (`run`)을 **TASK QUEUE**에 보낸다.
  - 그게 `setTimeout`의 일이기에 할일 다했으니까 콜스택에서 빠진다.
3. `console.log('end')`가 실행되어 콜스택에 들어간후 바로 종료되고 빠진다.
4. **TASK QUEUE**에 있는 함수를 차례대로 실행한다.
  - 이 경우에는 `run()` 하나만 실행한다. (호출스택에 run이 쌓인다.)
  - 그래서 `console.log('run')`이 콜스택에 들어간후 바로 종료되고 빠진다.
  - `run()`도 종료되고 호출스택에서 빠진다.

### 3) 이벤트 루프
![](assets/Screen%20Shot%202020-06-10%20at%203.21.57%20PM.png)
- 호출 스택이 비워지면, 태스크 큐에서 함수를 꺼내오는 역할을 한다.
- 만약 `setTimeout(() => {}, 3000)`일 경우, 이벤트루프는 태스크 큐에 계속 3초가 지났는지 물어보다가 지난순간 호출스택으로 끌어온다.

#### 언제 큐에 들어가나요?
- `setTimeout`
- `setInterval`
- `setImmediate`
- `Promise` (`resolve`, `reject`)
- `async`, `await`
- `eventListener`의 콜백함수

#### 실제로는 Task가 여러개이다.
- 함수마다 자기가 위치할 큐로 들어간다.
- 이벤트루프의 역할은 이 다섯개의 큐에서 정해진 순서대로 하나씩 꺼내오는 것이다.
- 이 순서는 이벤트 루프가 알고 있고, 자바스크립트 엔진마다 차이가 있다.
- [Node.js의 이벤트 루프에 대한 자세한 설명](https://nodejs.org/ko/docs/guides/event-loop-timers-and-nexttick/)