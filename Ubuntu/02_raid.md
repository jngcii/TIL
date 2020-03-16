# 하드디스크 관리 (RAID & mdadm)

###### 2020.03.16

## SATA와 SCSI : 메모리 슬롯
- SATA 슬롯은 30개의 SATA장치 연결 가증
- SCSI 슬롯은 슬롯당 15개의 SCSI 장치 연결 가능 (0:0 ~ 0:15, 0:7 사용 불가)
- SATA 슬롯 : 주로 PC용 하드디스크나 CD/DVD 장치 연결에 사용
- SCSI 슬롯 : 서버용으로는 주로 SCSI 하드디스크 사용 (1슬롯당 15개)
            요즘은 SAS를 주로 사용한다. (1슬롯당 65535개)<br />
- 리눅스에 처음 장착된 하드 디스크 이름 : `/dev/sda`
- 그 후 하드디스크 이름들 : `/dev/sdb`, `/dev/sdc` ~
- 파티션을 나누면 : `/dev/sdb1` & `/dev/sdb2` ~
- 추가 하드디스크를 사용하려면 최소 1개 이상의 파티션으로 나누고 특정 디렉터리에 마운트해야한다.
```shell
# 1. 하드 디스크 장착
# vm의 경우 store virtual disk as a single file & 알아보기 쉽게 scsi0-1.vmdk같이 hdd 생성

# 2. 파티션 나누기
fdisk /dev/sdb
# n -> p -> 1 -> enter -> enter -> p -> w
# 파티션을 2개로 나누고자 할땐, 예를 들어 3G 하드롤 2G&1G로 나누고자 할 땐, 첫번째 파티션을 만들땐 Last sector 부분에 +2G 입력

# 3. 해당 파티션 파일 시스템 생성
mkfs.ex4 /dev/sdb1

# 4. 마운트
mkdir /mydata
mount /dev/sdbv1 /mydata

# 5. 항상 마운트되어 있도록 설정
# /etc/fstab 제일 밑에 추가
# /dev/sdb1 /mydata ext4 defaults 0 0
```

## RAID : 여러 개의 하드디스크를 하나의 하드디스크처럼 사용하는 방식
- 하드웨어 RAID : 여러개의 하드를 연결할 장비를 만들어서 직접 연결
- **소프트웨어 RAID** : 하드가 이미 여러개 있을 때, 운영체제가 지원하는 방식으로 RAID를 구성하는 방법

### RAID 구성 방식 (N: 하드 갯수)
1. Linear RAID : 하드디스크에 순서대로 차곡차곡 쌓는 것
   - i.e. scsi0:1에 다차면 scsi0:2에 쌓기 시작
   - 디스크 사용률 : N
2. RAID 0 : 장착된 하드디스크에 분산되어 데이터를 쌓는 것 (스트리핑 방식)
   - Linear RAID에 비해 속도가 거의 N배 빨라짐
   - Linear가 1초라면, RAID 0은 1/N초
   - 하지만 하드디스크 1개가 고장마도 데이터 전부가 날아감
3. RAID 1 : 2개 장착된 하드웨어에 같은 데이터를 동시에 저장 (mirroring)
   - 결함 허용 제공
   - 저장속도는 빠르지 않다.
   - 사용률 : 50%;
4. RAID 5 : 최소 3개 이상, 대개는 5개 이상의 하드디스크로 구성
   - 결함 허용 (패리티 사용)
   - 속도 : *(N-1)
   - 사용률 : N-1- 디스크 사용률 : N
5. RAID 1+0 : RAID 1과 0을 결합한 방식
   - 결함 허용
   - 속도 : * N/2
   - 디스크 사용률 : N/2

### RAID 실제 구성

1. 하드디스크를 장치 이름과 맞게 설치
   - i.e. scsi 0:1  ->  disk0-1.vmdk
2. RAID용 파티션으로 만들기 (/dev/sdb ~)
   - fdisk /dev/sdb
   - n -> p -> 1 -> enter -> enter -> t -> fd -> p -> w
   - n : new
   - p : primary
   - t : 파일 시스템 유형 선택
   - fd : raid 오토디텍트 (L : 전체 유형 출력)
   - p : 확인
   - w : 저장
3. apt-get -y install mdadm
4. snapshot

### RAID 구축
> 부팅후 df명령 : 마운트된 raid장치 찾기
```shell
# 1. 파티션 상태 확인
fdisk -l /dev/sdb ; fdisk -l /dev/sdc
# 2. raid 생성
mdadm --create /dev/md9 --level=linear --raid-devices=2 /dev/sdb1 /dev/sdc1
# 3. raid 확인
mdadm --detail --scan
# 4. 파일 시스템 생성
mkfs.ex4 /dev/md9
# 5. 마운트할 디렉터리 생성
mkdir /raidLinear
# 6. 마운트
mount /dev/md9 /raidLinear
# 7. 항상 마운트되어 있게 설정
vim /etc/fstab
##끝에 이것 추가 /dev/md9 /raidLinear ext4 defaults 0 0
# 8. 확인
mdadm --detail /dev/md9
# 9. 버그 방지 설정
mdadm --detail --scan >file.txt
vim file.txt #복사 (yy)
vim /etc/mdadm/mdadm.conf #맨 뒤에 붙여넣고 name=server:<숫자> 부분 지우기
update-initramfs -u
# 10. 스냅샷
```

### RAID 문제 발생 조치 방법
1. 망가진 하드디스크 없애기
2. boot - 응급모드로 진입 (raid로 구성된 하드디스크가 고장나면 응급모드로 접속됨)
3. root 비번 입력
4. `ls -l /dev/sd*`로 장치 확인하고 `df`명령어로 마운트된 디렉터리 확인
5. 결함을 허용하는 RAID 1, 5 다시 가동
    - `mdadm --run /dev/md1`
    - `mdadm --run /dev/md5`
    - `df`
    - `ls -l /raid`
    - `mdadm --detail /dev/md1`
6. 결함 허용이 안되는 RAID Linear 0 다시 가동
    - `mdadm --run /dev/md9` (실패)
    - `mdadm --run /dev/md0` (실패)
    - `mdadm --stop /dev/md9`
    - `mdadm --stop /dev/md0`
    - `/etc/fstab` 밑 md0, md9 앞에 주석 (#)
7. 하드 디스크 망가진 기계 찾아서 그 scsi 슬롯으로 장착
8. 새 하드디스크 파티션 나누기 & `ls -l /dev/sd*`로 확인
9. 결함허용 안되는 것들 처리
    - `mdadm --create /dev/md9 --level=linear --raid-devices=2 /dev/sdb1 /dev/sdc1`
    - `mdadm --detail /dev/md1`로 확인
10. 결함 허용되는 것들 처리
    - `mdadm /dev/md1 --add /dev/sdg1`
    - `mdadm --detail /dev/md1`로 확인
11. `/etc/fstab` 수정(#제거) 및 mdadm 버그 수정 및 reboot
12. 다시 응급모드로 가면, fsck -y /dev/md0 & reboot (쓰레기값 제거)


### 고급 RAID 구성
> RAID 6 & RAID 1+0
- RAID 6 : RAID 5와 거의 동일 
- RAID 1+0
  1. 2개씩 짝지어서 raid 1로 구성한 다음
  2. raid 1로 만들어진 `/dev/md2`, `/dev/md3`을 raid0으로 구성한 후
  3. 파일시스템 생성 & 마운트
  4. 나머지는 동일
   

### 고급 RAID 응급 복구
1. 응급 모드에서 root password로 접속
2. 실행
   - `mdadm --run /dev/md6`
   - `mdadm --run /dev/md2`
   - `mdadm --run /dev/md3`
3. `mdadm --create /dev/md10 --level=0 --raid-devices /dev/md2 /dev/md3`
4. `mdadm detail /dev/md10`로 확인
5. `mdadm /dev/md2 --add /dev/sd머시기` (fdisk로 먼저 파티션 devide)