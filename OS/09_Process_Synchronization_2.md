# Process Synchronization 2

###### 2020.03.01

### I. 크리티컬 섹션에 대한 프로그램적 해결법의 충족 조건

1. Mutual Exclusion
    - 프로세스 Pi가 critical section 부분을 수행 중이면 다른 모든 프로세스들은 거들의 critical section에 들어가면 안된다.
2. Progress
    - 아무도 critical section에 있지 않은 상태에서 critical section에 들어가고자 하는 프로세스가 있으면 critical section에 들어가게 해주어야 한다.
3. Bounded Waiting
    - 기다리는 시간이 유한해야 한다.
    - 기아현상(starvation)이 없어야한다.
    - 프로세스가 critical section에 들어가려고 요청한 후부터 그 요청이 허용될 때까지 다른 프로세스들이 critical section에 들어가는 횟수에 한계가 있어야 한다.

- 가정
  - 모든 프로세스의 수행 속도는 0보다 크다.
  - 프로세스들 간의 상대적인 수행 속도는 가정하지 않는다.
