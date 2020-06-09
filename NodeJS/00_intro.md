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

- Node.js의 핵심적인 3가지
  - 이벤트 기반
  - 논블로킹 I/O
  - 싱글 스레드

### 1) 이벤트 루프
