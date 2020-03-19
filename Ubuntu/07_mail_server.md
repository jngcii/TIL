# Mail Server

###### 2020.03.19

- SMTP : 클라이언트 -> **서버** <-> **서버** <- 클라이언트
- POP3 / IMAP : 서버에 저장된 메일을 Client가 읽는 프로토콜

## 메일 서버 구현
1. 두개의 메일 서버 구현
  ```bash
  # 1.
  $ apt-get -y install sendmail

  # 2.
  $ vim /etc/hostname
  # mail.jngcii.com

  # 3.
  $ vim /etc/hosts
  # 192.168.111.100 mail.jngcii.com  (추가)

  # 4.
  $ reboot
  $ hostname    # mail.jngcii.com 나와야한다.

  # 5.
  $ vim /etc/NetworkMa tab/sys tab/Wired tab
  ```

- 에라 모르겠다