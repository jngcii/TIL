# Docker Engine

###### 2020.07.09

## I. 도커 이미지와 컨테이너
- 도커 엔진에서 사용하는 기본 단위는 이미지와 컨테이너이며, 이 두가지가 도커 엔진의 핵심이다.

### 1) 도커 이미지
- 컨테이너를 생성할 때 필요한 요소
- 여러 개의 계층으로 된 바이너리 파일로 존재
- 컨테이너를 생성하고 실행할 때, 읽기 전용으로 사용된다.
- [저장소 이름]/[이미지 이름]:[태그] 형태로 구성
  - 저장소 이름 : 이미지가 저장된 장소 (도커 허브), 생략 가능
  - 이미지 이름 : 해당 이미지가 어떤 역할을 하는지 나타낸다. 생략 불가
  - 태그 : 이미지의 버전 관리 혹은 리비전 관리에 사용, 생략하면 latest로 인식

### 2) 도커 컨테이너
- 이미지로 컨테이너를 생성하면 해당 이미지의 목적에 맞는 파일이 들어있는 파일시스템과 격리된 시스템 자원 및 네트워크를 사용할 수 있는 독립된 공간이 생성되고, 이것이 바로 도커 컨테이너가 된다.
- 대부분의 도커 컨테이너는 생성될 때 사용된 도커 이미지의 종류에 따라 알맞은 설정과 파일을 가지고 있기 때문에 도커 이미지의 목적에 맞도록 사용되는 것이 일반적이다.
- 컨테이너는 이미지를 읽기 전용으로 사용하되 이미지에서 변경된 사항만 컨테이너 계층에 저장하므로 컨테이너에서 무엇을 하던지 원래 이미지는 영향을 받지 않는다.


<br />

## II. 도커 컨테이너 다루기

### 1) 컨테이너 생성
- 도커 엔진의 버전을 확인하며 시작
    ```bash
    $ docker -v
    ```
    > 사소한 버전 차이로 도커의 중요한 기능을 사용하지 못할 수도 있기 때문
- `run`
    ```bash
    $ docker run -i -t ubuntu:16.04

    Unable to find image 'ubuntu:16.04' locally
    16.04: Pulling from library/ubuntu
    512h6l7gw0ad: Pull complete
    ...
    root@g312gw8fas08wt: /#
    ```
    - 컨테이너를 생성 및 실행과 동시에 컨테이너 내부로 들어가는 명령어
    - ubuntu:16.04 : 컨테이너를 생성하기 위한 이미지의 이름
    - `-i -t` : 컨테이너와 상호 입출력을 가능하게 한다.
      - `-i` : 상호 입출력 활성화
      - `-t` : tty 활성화해서 배시 셸을 사용하도록 설정
    - 컨테이너에서 기본 사용자는 root
    - 호스트 이름은 무작위의 16진수 해시값
- 컨테이너 나오기
  - `exit` or `ctrl + D` : 내부에서 자오면서 동시에 컨테이너 정지
  - `ctrl + P, Q` : 단순히 컨테이너의 셸에서만 빠져나온다.
- `create`
    ```bash
    $ docker pull centos:7
    $ docker images
    $ docker create -i -t --name mycentos centos:7
    ```
    - `create` 명령어는 컨테이너를 생성만 할 뿐 컨테이너로 들어가지 않는다.
    - 들어가려면 아래 명령어를 실행하면된다.
        ```bash
        $ docker start mycentos
        $ docker attach mycentos
        ```
    - 그러나 `run` 명령어를 더 많이 사용한다.
- `ps`
  - 컨테이너 목록 출력
  - 현재 실행중인 컨테이너만 출력한다.
  - `-a` 옵션을 통해 멈춰있는 컨테이너까지 모두 볼 수 있다.
  - 결과 예시
    ```bash
    CONTAINER ID   IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES
    ```
    - CONTAINER ID : 컨테이너에 자동으로 할당되는 공유한 ID
    - IMAGE : 컨테이너를 생성할 때 사용된 이미지 이름
    - COMMAND : 컨테이너가 시작될 때 실행될 명령, 커맨드는 대부분의 이미지에 미리 내장되어 있기 때문에 별도로 설정할 필요는 없다. 컨테이너가 시작될 때 `/bin/bash`라는 명령어가 실행되어 상호 입출력이 가능한 셸 환경을 사용할 수 있다.
    - CREATED : 컨테이너가 생성되고 난 뒤 흐른 시간
    - STATUS : 컨테이너의 상태 (Up은 실행중, Exited는 종료, Pause는 일시정지)
    - PORTS : 컨테이너가 개방한 포트와 호스트에 연결한 포트를 나열합니다.
    - NAMES : 컨테이너의 고유한 이름

### 2) 컨테이너를 외부에 노출
- 컨테이너는 가상 머신과 마친가지로 가상 IP를 할당받는다.
- 기본적으로 도커는 컨테이너에 172.17.0.x의 IP를 순차적으로 할당한다.
- 컨테이너를 새롭게 생성한 후 ifconfig 명령어로 컨테이너의 네트워크 인터페이스를 확인한다.
    ```bash
    $ docker run -it --name newtwork_test ubuntu:16.04

    root@f786b7a62c:/# ifconfig

    eth0    Link encap:Ethernet ....
            inet addr:172.17.0.2 ....

    lo      Link encap:Local Loopback
    inet    inet addr:127.0.0.1 ....
    ```
    - 도커의 NAT IP인 172.17.0.2를 할당받은 eth0 인터페이스와 로컬 호스트인 lo 인터페이스가 있다.
    - 아무런 설정을 하지 않았으면 이 컨테이너에는 외부에서 접근할 수 없고, 도커가 설치된 호스트에서만 접근할 수 있다.
    - 외부에서 컨테이너의 애플리케이션을 노출하기 위해서는 eth0의 IP와 포트를 호스트의 IP와 포트에 바인딩해야 한다.
    - 예시
        ```bash
        $ docker run -it --name mywebserver -p 80:80 ubuntu:16.04
        ```
        - `-p [호스트포트]:[컨테이너포트]`