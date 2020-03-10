# Virtual Memory 2

###### 2020.03.10

## Caching

### I. Caching 기법
- 한정된 빠른 공간(=캐시)에 요청된 데이터를 저장해 두었다가 후속 요청시 캐시로부터 직접 서비스하는 방식
- paging system 외에도 cache memory, buffer caching, web caching 등 다양한 분야에서 사용

### II. 캐시 운영의 시간 제약
- 교체 알고리즘에서 삭제할 항목을 결정하는 일에 지나치게 많은 시간이 걸리는 경우 실제 시스템에서 사용할 수 없음
- Buffer caching이나 web caching의 경우
  - O(1)에서 O(log n) 정도까지 허용
- Paging system인 경우
  - page fault인 경우에만 OS가 관여함
  - 페이지가 이미 메모리에 존재하는 경우 참조시각 등의 정보를 OS가 알 수 없음
  - **그래서 사실상 LRU, LFU 알고리즘 사용할수 없다**
  - O(1)인 LRU의 list 조작조차 불가능


<br />

## 실제 사용 알고리즘

### I. Clock algorithm
- 개념
  - LRU의 근사 알고리즘
  - 여러 명칭으로 불림
    - Second chance algorithm
    - NUR (Not Used Recently) 또는 NRU (Not Recently Used)
  - reference bit을 사용해서 교체 대상 페이지 선정 (circular list)
  - reference bit가 0인 것을 찾을 때까지 포인터를 하나씩 앞으로 이동
  - 포인토 이동하는 중에 reference bit 1은 모두 0으로 바꿈
  - reference bit이 0인 것을 찾으면 그 페이지를 교체
  - 한 바퀴 되돌아와서도(=second chance) 0이면 그때에는 replace 당함
  - 자주 사용되는 페이지라면 second chance가 올때 1
- Clock algorithm의 개선
  - reference bit과 modified bit을 함께 사용
  - reference bit = 1 : 최근에 참조된 페이지
  - modified bit = 1 : 최근에 변경된 페이지 (I/O를 동반하는 페이지)

### II. Page Frame의 Allocation
- Allocation problem : 각 process에 얼만큼의 page frame을 할당할 것인가?
- Allocation의 필요성
  - 메모리 참조 명령어 수행시 명령어, 데이터 등 여러 페이지 동시 참조
    - 명령어 수행을 위해 최소한 할당되어야 하는 frame의 수가 있음
  - Loop를 구성하는 page들은 한꺼번에 allocate 되는 것이 유리함
    - 최소한의 allocation이 없으면 매 loop 마다 page fault
- Allocation Scheme
  - Equal allocation: 모든 프로세스에 똑같은 개수 할당
  - Proportional allcaiotion: 프로세스 크기에 비례하여 할당
  - Priority allocation: 프로세스의 priority에 따라 다르게 할당

### III. Global vs Local Replacement
- Global replacement
  - Replace 시 다른 process에 할당된 frame을 빼앗아 올 수 있다.
  - Process 별 할당량을 조절하는 또 다른 방법임
  - FIFO, LRU, LFU 등의 알고리즘을 global replacement로 사용시에 해당
  - working set, PFF 알고리즘 사용
- Local replacement
  - 자신에게 할당된 frame 내에서만 replacement
  - FIFO, LRU, LFU 등의 알고리즘을 process 별로 운영시
  - 
<br />


## Thrashing

### Thrashing
- 프로세스의 원활한 수행에 필요한 최소한의 page frame 수를 할당받지 못한 경우 발생
- page fault rate가 매우 높아짐
- CPU utilization이 낮아짐
- OS 는 MPD(Multiprogramming degree)를 높여야 한다고 판단
- 또 다른 프로세스가 시스템에 추가됨(higher MPD)
- 프로세스 당 할당된 frame의 수가 더욱 감소
- 프로세스는 page의 swap in / swap out으로 매우 바쁨
- 대부분의 시간에 CPU는 한가함
- low throughput