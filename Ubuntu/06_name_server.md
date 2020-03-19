# Name Server

###### 2020.03.19

## PC가 도메인을 찾아가는 순서
1. `/etc/hosts` 파일 검색 (전화번호부)
2. domain cache table 검색 (일시적인 cache)
3. `/etc/resolv.conf` 파일 속 nameserver 부분을 통해 로컬네임서버를 알아낸다.
   (로컬네임 서버 : 8.8.8.8, KT 네임서버, 192.168.111.2 등)
4. 로컬네임서버에 IP주소를 물어본다.
   1. 자신의 캐시 DB에서 domain name 알아보고
   2. master dns로서의 기능을 할 수 있는지 보고
   3. 없으면 root 네입서버, .com네임서버에 domain name을 무렁봐서 마스터 네임서버 IP를 알아낸다.
   4. master nameserver가 IP주소를 로컬 네임서버에 주고 Client로 전달

## 캐싱전용 네임서버 구축
> root, .com. 마스터 서버에 물어보는 서버 프로그램 bind9를 사용해 캐시저용 네임서버까지만 구축한 모습
```bash
# 1. package 설치
$ apt-get -y install bind9 bind9utils

# 2. /etc/bind/named.conf.options 파일 수정
$ vim /etc/bind/named.conf.options
# (아래가 없으면 3행쯤 추가)
# recursion yes;
# allow-query { any; };

# 3. 데몬 실행
$ systemctl restart / enable / status bind9

# 4. 방화벽 열기
$ ufw allow 53

# 5. 테스트
$ dig @192.168.111.100 www.nate.com

```

## 마스터 네임서버 구축
> 웹서버를 192.168.111.200에서 구동중이라고 가정
```bash
# 1. /etc/bind/named.conf (네임서버서비스가 시작될 때 제일 먼저 읽는 파일) 맨아래 추가
$ vim /etc/bind/named.conf
# zone "jngcii.com" IN {
#   type master;
#   file "/etc/bind/jngcii.com.db"
# };

# 2. 문법 확인
$ named-checkconf

# 3. /etc/bind 디렉터리에 jngcii.com.db 파일 만들기
$ cd /etc/bind
$ vim jngcii.com.db
# $TTL  3H
# @     IN    SOA   @   root.   ( 2 1D  1H  1W  1H  )
# @     IN    NS    @
#       IN    A     192.168.111.100
#
# www   IN    A     192.168.111.200

# 4. 문법 검사
$ named-checkzone jngcii.com  jngcii.com.db

# 5. 데몬 재시작
$ systemctl restart / status bind9
```

### jngcii.com.db : 포워드 존 파일 or 정방학 영역 파일
- 문법
  1. `;` : 주석
  2. `$TTL` : Time To Live
    - www.jngcii.com의 호스트이름이 질의됐을 때, 질의해간 로컬네임서버가 IP 주소를 캐시에 저장하는 시간
  3. `@` : /etc/bind/named.conf에 정의된 jngcii.com을 의미
    - `@` 대신 `jngcii.com` 써도 됨
  4. `IN` : 클래스 이름으로 internet을 의미
  5. `SOA` : **S**tart **O**f **A**uthority, 권한의 시작을 뜻함
  6. `NS` : **N**ame **S**erver의 약자
  7. `MX` : **M**ail **E**xchanger의 약자
  8. `A` : 호스트 이름에 상응하는 IP주소
  9. `CNAME` : 호스트 이름에 별칭을 부여할때 사용
- IP주소를 통해 도메인을 아는 것 : 리버스존 or 역방향 영역
- 도메인을 IP주소로 변경하는 것 : 포워드존 or 정방향 영역