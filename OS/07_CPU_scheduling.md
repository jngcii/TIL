# CPU 스케쥴링

###### 2020.02.27

> I/O bound job같이 사람과 인터렉션하는 잡이 오랙 기다리지 않게 하기 위한 것

### I. 프로세스의 특성 분석
- I/O bound process
  - CPU를 잡고 계산하는 시간보다 I/O에 많은 시간이 필요한 job
  - many short CPU bursts
- CPU-bound process
  - 계산 위주의 job
  - few very long CPU bursts
- CPU-bound process 가 너무 오래 CPU를 잡고있으면 사람과 일터렉션하는 I/O bound process가 너무 오래 기다려야 하기 때문에 이를 위해 CPU 스케쥴링이 필요하다.

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


### III. CPU 성능 척도

1. Utilization (이용률)
   - 시스템 입장에서의 성능 척도
   - 전체 시간중 CPU가 놀지 않고 일한 시간의 비율
   - CPU는 비싼 자원이기 때문에 놀리지 말고 최대한 일을 바쁘게 시켜라
2. Throughput (처리량)
   - 시스템 입장에서의 성능 척도
   - 주어진 시간동안에 몇개의 일을 처리했느냐
3. Turnaround time (소요시간)
   - 프로세스입장에서의(시간 기준) 성능 척도
   - CPU를 쓰러 들어와서 다 쓰고 I/O를 하러 나갈때까지 걸린 시간
4. Waiting time (대기시간)
   - 프로세스입장에서의(시간 기준) 성능 척도
   - ready queue에서 기다리는 시간
5. Response time (응답시간)
   - 프로세스입장에서의(시간 기준) 성능 척도
   - ready queue에 들어와서 처음으로 CPU를 쓰기까지 기다리는 시간

<br />


## CPU Scheduling Algorithm - nonpreemptive(비선점형)

### I. FCFS (First-come Fisrt-served)
- 먼저 온 순서대로 처리하는 방법
- 사람들 사이에서 많이 사용되는 방법
- 은행 줄 기다리기, 화장실 줄서기
- 처음 시작한 작업이 10000000초가 걸리면 그 뒤의 프로세스들은 무지하게 기다려야하는 알고리즘 (convoy effect)
- 앞에 어떤 프로스세가 있느냐에 따라 평균 waiting time이 많이 달라진다.

### II. SJF (Shortest Job First)
- SRTF의 Preemtive 버전
- 짧은 작업들 먼저 처리하는 방법
- 하나의 프로세스가 끝났을때 스케쥴링
- Starvation(기아현상) : CPU사용시간이 긴 프로세스는 영원히 CPU할당을 받을 수 없는 문제

### III. Priority Scheduling
- 우선순위 기준의 스케쥴링
- 프로세스 하나가 끝나야 다음 우선순위 스케쥴링된 프로세스 실행
- 역시 기아현상 발생

<br />


## CPU Scheduling Algorithm - preemptive(선점형)

### I. SRTF (Shortest Remaining Time First)
- SJF의 Preemtive 버전
- 짧은 작업들 먼저 처리하는 방법
- 처리하는 중간에라도 남은 시간보다 더 짧은 시간의 작업이 들어오면 뺏어서 준다.
- 평균 waiting time이 가장 짧은 알고리즘
- 새로운 프로세스가 들어왔을때 바로 스케쥴링
- Starvation(기아현상) : CPU사용시간이 긴 프로세스는 영원히 CPU할당을 받을 수 없는 문제

### II. Priority Scheduling
- 우선순위 기준의 스케쥴링
- 새로운 프로세스가 들어오면 즉시 뺏어서라도 우선순위 스케쥴링된 프로세스 실행
- 역시 기아현상 발생

### III. RR (Round-Robin)
- 현대적인 컴퓨터 시스템에서 사용하는 스케쥴링
- CPU를 줄때 할당 시간을 주고, 할당 시간이 끝나면 Ready queue 맨 뒤에 서는 방법
- 응답 시간이 빠르다. (CPU를 최초로 얻을 수 있는 시간이 빠르다.)
- Performance
  - q large => FCFS
  - q small => context swtich
  - 10~100ms 정도가 적당하다.

<br />


## CPU Scheduling Algorithm - 복합적

### I. Multilevel Queue
- 우선순위를 가진 여러개의 큐를 가지고 상위 우선순위의 큐가 비어있을때, 다음 큐로 넘어가는 방식
- Ready queue를 여러개로 분할
  - foreground queue (interactive)
  - background queue (batch - no human interaction)
- 각 큐는 독립적인 스케쥴링 알고리즘을 가진다.
  - foreground - RR
  - background - FCFS

### II. Multilevel Feedback Queue
- 우선순의가 바뀔수 있는 방식
- 우선순위 승격, 강등 기준 관건

### III. Multiple-Processor Scheduling
- CPU가 여러개인 경우 스케쥴링이 더욱 복잡해짐
- Homogeneous processor인 경우
  - queue에 한줄로 세워서 각 프로세서가 알아서 꺼내가게 할 수 있다.
  - 반드시 특정 프로세서에서 수행되어야 하는 프로세스가 있는 경우에는 문제가 더 복잡해진다.
- Load sharing
  - 일부 프로세서에 job이 몰리지 않도록 부하를 적절히 공유하는 메커니즘 필요
  - 별개의 큐를 두는 방법 vs 공동 큐를 사용하는 방법
- Symmetric Multiprocessing (SMP)
  - 각 프로세서가 각자 알아서 스케쥴링 결정
- Asymmetric Multiprocessing
  - 하나의 프로세서가 시스템 데이터의 접근과 공유를 책임지고 나머지 프로세서는 거기에 따름

### IV. Real-Time Scheduling
- Hard real-time systems
  - 반드시 데드라인 안에 끝나야하는 것
- Soft real-time computing

### V. Trhead Scheduling
- Local Scheduling
  - User level thread의 경우 사용자 수준의 thread library에 의해 어떤 thread를 스케줄할지 결정
- Global Scheduling
  - Kernel level thread의 경우 일반 프로세스와 마찬 가지로 커널의 단기 스케쥴러가 어떤 thread를 스케쥴할지 결정