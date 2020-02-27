# CPU 스케쥴링 1

###### 2020.02.27

> I/O bound job같이 사람과 인터렉션하는 잡이 오랙 기다리지 않게 하기 위한 것

### I. 프로세스의 특성 분석
- I/O bound process
  - CPU를 잡고 계산하는 시간보다 I/O에 많은 시간이 필요한 job
  - many short CPU bursts
- CPU-bound process
  - 계산 위주의 job
  - few very long CPU bursts

### II. CPU Scheduler & Dispatcher
- CPU Scheduler
  - 스케쥴링을 하는 운영체제 커널 코드를 가리킴
  - Ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다.
- Dispatcher
  - 프로그램에게 제어권을 넘겨주는 운영체제 커널 코드를 가리킴
  - CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘긴다.
  - 이 과정을 context switch라고 한다.
- CPU 스케줄링이 필요한 경우는 프로세스에게 다음과 같은 상태 변화가 있는 경우다.
    1. Running -> Blocked (e.i. I/O 요청하는 시스템 콜)
    2. Running -> Ready (e.i. 할당시간만료로 timer interrupt)
    3. Blocked -> Ready (e.i. I/O 완료 후 인터럽트)
    4. Terminate
- 1, 4에서의 스케쥴링은 **nonpreemptive**(자진반납)
- 나머지는 **preemptive**(강제로 뺏음)