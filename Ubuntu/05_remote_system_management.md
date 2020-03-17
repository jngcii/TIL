# 원격지 시스템 관리

###### 2020.03.17

## Telnet
> 전통적으로 사용되어온 원격 접속 방법

- 리눅스에 텔넷 서버 설치, Client PC에 텔넷 클라이언트 프로그램이 필요함
- telnet client program은 대부분 OS에 내장

### Telnet 서버 구축
1. telnet 서버 프로그램 설치
   ```shell
   # dpkg -l xinetd # telnet package 설치됐는지 확인
   # apt-get -y install xinetd telnetd # 관련 package 설치
   ```
2. telnet서버가 가동하도록 설정
   ```shell
   # cd /etc/xinetd.d
   # touch telnet
   # vim telnet
   ```
   */etc/xinetd.d/telnet*
   ```
   service telnet {
       disable = no
       flags = REUSE
       socket_type = stream
       wait = no
       user = root
       server = /usr/sbin/in.telnetd
       log_on_failure += USERID
   }
   ```
3. 접속 테스트를 위한 사용자 만들기
   ```shell
   # adduser teluser
   ```
4. 텔넷 서비스 가동
   ```shell
   # systemctl restart xinetd
   # systemctl enable xinetd
   # systemctl status xinetd
   ```
5. 23번 포트 방화벽 허용
   ```shell
   # ufw allow 23/tcp
   ```
### Client에서 접속하기 (teluser로 접속해야한다.)
   ```shell
   $ telnet [serverIP]
   server login : teluser
   password :

   $ whoami
   ```

## OpenSSH
> telnet과 용도는 동일하지만 보안이 강화된 원격지 서버<br />
> 데이터 전송 시 패킷 암호화

### OpenSSH 서버 구축
1. 서버 설치
   ```shell
   # apt-get -y install openssh-server
   ```
2. 재가동 / 상시가동 / 상태확인
   ```shell
   # systemctl restart ssh
   # systemctl enable ssh
   # systemctl status ssh
   ```
3. 방화벽 열기
   ```shell
   # ufw allow 22/tcp
   ```

### Client 접속 방법
```shell
$ ssh <사용자 이름>@<서버 IP 주소>
```