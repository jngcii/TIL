# 기본 개념

###### 2020.03.16

## 부팅관련 명령어

### 시스템 종료
```shell
poweroff
shutdown -P now
halt -p
init 0
```

### rebooting
```shell
reboot
shutdown -r now
init 6
```

## 가상 콘솔
> 우분투는 7개의 가상 콘솔이 존재하는데 1~6번째는 cli, (gui가 깔려있다면 7번째는 gui)
- 변경방법 : `ctrl` + `option` + `fn` + (`f1` ~ `f7`)
- run level 변경 방법
  ```shell
  # default.target에 연결된 파일 찾기
  ls -l /lib/systemd/system/default.target

  # multi-user를 default로 link 걸기
  ln -sf /lib/systemd/system/multi-user.target /lib/systemd/system/default.target

  # graphical을 default로 link 걸기
  ln -sf /lib/systemd/system/graphical.target /lib/systemd/system/default.target

  # reboot하면 처음부터 설정된 것으로 들어가진다.
  ```

## vi editor
- 비정상 종료된 vi파일 잔재 지우는 법
  - 비정상 종료시킨 파일의 위치 directory로 들어가서 `ls -a` 하면 숨김파일까지 모두 보여주는데, 스왑파일(`.swp`확장자)를 지우면 된다.
  - `rm -rf .new.txt.swp`
- 명령어
  - `i` : 현재 커서부터 입력
  - `shift` + `i` : 현재커서줄의 맨 앞부터 입력
  - `a` : 다음 커서부터 입력
  - `shift` + `a` : 현재커서줄의 맨 뒤부터 입력
  - `gg` : 제일 첫 행으로 이동
  - `shift` + `g` : 제일 끝행으로 이동
  - 숫자 + `G` : 해당 숫자 행으로 이동
  - 숫자 + `dd` : 현재 커서부터 숫자만큼 행 삭제
  - 숫자 + `yy` : 현재 커서부터 숫자만큼 행 복사
  - `p` : 복사한 내용을 현재 행 이후에 붙여넣기
  - `/문자열` + `enter` : 해당 문자열로 이동

## 마운트
- `mount` : 현재 마운트된 장치 확인
- `unmount /dev/cdrom` : 해당 디렉터리 마운트 해제
  (/dev/cdrom은 /dev/sr0에 링크된 이름)
- usb마운트 하는 법
    ```shell
    # 연결된 장치 확인
    ls /dev/sd*
    # media 디렉터리 하위에 마운트할 dir 생성
    mkdir /media/usb
    # 마운트
    mount /dev/sd1 /media/usb
    ```

## 리눅스 기본 명령어
```shell
pwd # 현재 위치 출력
cp /abc/old.txt /bcd/new.txt # abc의 old.txt 파일을 bcd에 new.txt로 복사
touch abc.txt # abc.txt라는 크기가 0인 새 파일 생성. 이미 존재하면 최종 수정 시간 변경
mv # 파일 or 디렉터리 이동
rmdir # 해당 디렉터리 삭제
head, tail : 앞, 뒤 10행 출력
```

## 사용자와 그룹
```shell
cat /etc/passwd #사용자 보기
cat /etc/group #그룹 보기

# 사용자 추가  --유저 아이디 --그룹 아이디 --홈디렉터리 --기본 쉘
adduser --uid --gid --home /newhome --shell /bin/csh
passwd # 비번변경
usermod --shell /bin/csh --groups ubuntu newuser1 # 사용자 속성 변경
userdel # 사용자 삭제
groups # 사용자 소속 그룹 출력
groupadd <group명> # 새 그룹 생성
groupmod # 그룹 모드 변경
groupdel # 그룹 삭제
gpasswd # 그룹 관리
```

## 파일 허가권
| user | group | other |
|---|---|---|
|rwx|rwx|rwx|
|421|421|421|
\
- 허가권 변경 `chmod 000~777 파일명`
- 파일 소유권 `chown ubuntu test` : test파일의 소유권을 ubuntu로 변경
- 파일 그룹 `chgrp ubuntu test` : test파일 그룹을 ubuntu로 변경
- 한번에 `chown ubuntu.ubuntu test`

## 링크
>inode : 리눅스/유닉스 파일 시스템의 자료구조로, 모든 파일 및 디렉터리에는 각자 한개씩의 inode가 있고 각 inode에는 해당 파일의 소유권, 허가관, 파일 종류, 주소 등의 메타 데이터를 포함하고 있다.
- `ln` : 심볼릭 링크 ( 링크대상파일의 위치가 바뀌면 연결 끊김 )
- `ln -s` : 하드 링크 ( 링크대상파일의 위치가 바뀌어도 연결 유지 )


## 패키지

### dpkg
- 의존성을 고려하지 않고 설치하는 패키지 매니저
- 보통 조회를 많이 한다.
  `dpkg -l <패키지 이름>`

### apt-get
```shell
apt-get -y install <패키지 이름> # 설치
apt-get update # 목록 업데이터
apt-get remove <패키지 이름> # 패키지만 삭제
apt-get purge <패키지 이름> # 의존성 패키지까지 모두 삭제
apt-get autoremove # 사용하지 않는 패키지 자동 삭제
apt-get clean <패키지 이름> # 과적 파일까지 삭제
apt-get autoclean # 사용하지 않는 패키지 과거 파일까지 모두 삭제

apt-cache show <패키지 이름> # 패키지 정보 출력
apt-cache depends <패키지 이름> # 의존성 정보 출력
apt-cache rdepends <패키지 이름> # 역의존성 정보 출력
```

## 파일 압축 및 묶기

### 압축
- xz, bzip2, gzip, zip이 있다.
- xz 사용법
  ```shell
  xz <파일이름> # 파일이름.xz로 압축, 기존파일 삭제
  xz -k <파일이름> # 파일이름.xz로 압축, 기존파일 유지
  xz -d <파일이름.xz> # 압축풀기
  xz -l <파일이름.xz> # 압축 파일 속 파일 목록, 압축률 출력
  ```

### 묶기 (tar)
>확장자명 tar로 묶음 파일을 만들거나 묶음 해제
- c : 묶음파일 생성
- C : 묶음을 풀때 지정된 디렉터리에 해제 (지정하지 않으면 묶을 때의 디렉터리로)
- x : 묶음 해제
- t : 묶음경로 보요주고 해제
- f : 묶음파일 이름 지정 (생략 불가)
- v : 묶이거나 풀리는 과정 보여주기 (생략 가능)
- J : tar + xz
- j : tar + bzip2
- z : tar + gzip
  ```shell
  tar cvf my.tar /etc/systemd/      # /etc/systemd/를 과정을 보여주면서 my.tar 이름으로 묶기
  tar cvfJ my.tar.xz /etc/systemd/  # /etc/systemd/를 과정 보여주면서 xz로 압축하면서 my.tar.xz로 묶기
  tar xvfj my.tar.bz2               # C를 지정하지 않았으므로, 묶을때의 directory로 my.tar.bz2 압축 및 묶음 풀기
  ```

### 파일 찾기
- `find /etc -name "*.swp"` : etc 하위 directory에서 .swp 확장자 파일들을 찾아라


## CRON
> 시스템 작업 예약

### 사용법
```shell
systemctl status cron
vim /etc/crontab 
# 아래 입력
```
```vim
PATH = /usr/~~~ #이거 아래 모두 삭제
#한줄 띄고
01 03 15 * * root /root/myBackup.sh
# 분 시 일 월 요일 사용자 실행파일
# 매요일 매월 15일 3시 15분에 root권한으로 /root/myBackup.sh 실행해라!
```
```shell
#my backup 만들기
touch myBackup.sh
chmod 755 myBackup.sh
ls -s myBackup.sh
vim myBackup.sh
```
```vim
#! /bin/sh
set $(date)
fname="backup - $1$2$3tar.xz"
tar cfJ /backup/$fname /home
```
```shell
mkdir /backup
systemctl restart cron
```

## 네트워크 관련 명령어
```shell
nm-connection-editor
nmtui
systemctl [start/stop/restart/status] networking
ifconfig
nslookup
```
- `/etc/resolv.conf` : 임시로 사용되는 파일로 dns 정보와 호스트 이름이 있다. (dns 서버 정보를 영구히 바꾸려면 `/etc/network/interfaces` 직접 편집)
- reboot 해야 적용된다.

## 프로세스, 데몬, 서비스, 소켓

### 프로세스 : 프로그램이 실행되어 메모리에 올라온 상태
- 관련 명령어
  - `ps` : 현재 프로세스의 상태를 확인하는 명령어
    `ps -ef | grep <pid>`
  - `kill` : 프로세스 강제 종료
    `kill -9 <pid>`
### 서비스 (=데몬)
- 백그라운드 프로세스 중 하나로 서비스, 데몬, 서버프로세스 등.
- 웹서버, 네임서버, DB서버 등

### 소켓
- 필요할때만 가동시키는 서버 프로세스

### 서비스와 소켓 작동 및 관리하는 프로그램 : systemd
- 명령어 : `systemctl`
- 현재사용/비사용 서비스 보는 법 : `systemctl list-unit-files`
