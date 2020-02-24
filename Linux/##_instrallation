# 리눅스에 각종 프로그램 설치하기

###### 2020.02.24

### I. node.js 및 npm (nvm 사용)

1. 관련 패키지 설치하기

  ```shell
  $ sudo apt install build-essential libssl-dev
  ```

2. nvm 설치 (curl 이용)

  ```shell
  $ sudo curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
  ```
  >bash에 적용까지 한것


3. bashrc를 통해 적용

  ```shell
  $ source ~/.bashrc
  ```

4. node.js 설치 및 확인 (원하는 버전으로)

  ```shell
  $ nvm install [12.15.0]
   
  $ node --version
  $ npm --version
  ```

<br />

### II. python 및 pip 설치

1. 시작

  ```shell
  $ sudo apt update
  ```

2. ppa(개인 패키지 저장소) 추가

  ```shell
  $ sudo apt install software-properties-common
  $ sudo add-apt-repository ppa:deadsnakes/ppa
  $ sudo apt update
  ```

3. python 3.7 설치

  ```shell
  $ sudo apt install python3.7

  $ python3.7 --version
  ```

4. python3.7을 기본으로!

  ```shell
  $ sudo vim ~/.bashrc
  ```

  ***.bashrc***
  ```shell
  alias python="python3.7"
  ```

  ```shell
  esc + :wq + enter
  ```

5. pip3.7 설치

  ```shell
  #  pip3 설치
  $ sudo apt install python3-pip

  # pip version 확인
  $ pip --version
  $ pip3 --version

  # 만약 pip가 pip3 버전이 아니면 .bashrc에 alias 추가
  $ sudo vim ~/.bashrc

  # pip를 3.7 버전으로 업그레이드
  $ python3.7 -m pip install pip
  ```


<br />

### III. NginX 설치

1. nginx ppa 추가

  ```shell
  $ apt install software-properties-common
  $ add-apt-repository ppa:nginx/development
  $ apt update
  ```

2. nginx 설치

  ```shell
  $ apt install nginx-full
  ```