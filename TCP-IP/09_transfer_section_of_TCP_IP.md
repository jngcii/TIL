# TCP/IP 방식의 전송 계층

###### 2020.02.06

- 응용 계층과는 달리 단 두개의 프로토콜 존재 **TCP** **UDP**
- 버퍼링 및 단편화 유(TCP)/무(UDP)에 따라 구분

### I. TCP 프로토콜의 전송 과정

> 응용계층에서 1,024바이트 크기의 페이로드를 생성했다고 가정

#### 1) 전송전 3단계 연결 설정

1. 1,024바이트의 페이로드를 응용계층 버퍼에 임시로 저장 (버퍼링)
2. 전송계층에서 SYN 신호를 담은 세그먼트 1개를 생성한다. (이 모든 것을 운영체제가 한다.)
3. SYN 세그먼트는 네트워크 계층과 데이터링크 계층을 차례로 통과하면서 각각의 헤더를 붙인 뒤 물리 계층에서 비트단위로 전환해 목적지로 나간다.
4. 수신 측 호스트는 해당 SYN 신호를 전송 계층까지 끌어올려 전송 계층에서 SYN/ACK 신호를 담은 세그먼트 1개를 생성해 출발지로 보낸다. (3번의 과정을 거쳐서)
5. 송신 측 호스트는 해당 SYN/ACK 신호를 전송 계층까지 끌어올린 뒤 ACK 신호를 담은 세그먼트 1개를 생성해 목적지로 보낸다.
6. 전송전 3단계 연결 설정 완료

#### 2) 단편화

1. 연결이 확립되면 운영체제가 응용계층 버퍼에 넣어놨던 페이로드를 전송계층으로 넘긴다.
2. 전송계층에서는 1,024바이트의 페이로드를 2개의 512바이트의 페이로드로 **단편화**한다.

#### 3) 세그먼트 생성

- 조각난 각각의 페이로드 앞에 출발지와 목적지 포트번호 등이 담긴 헤더를 붙여 두개의 세그먼트를 생성한다.

#### 4) 네트워크 계층으로 전달

- 조각난 페이로드는 네트워크 계층으로 넘어가 각각의 패킷으로 생성된다.


> 전송은 무조건 응용계층에서 시작하는 것이 아니라 전송 전 3단계 연결 설정처럼 전송 계층에서 시작하는 경우도 있다.