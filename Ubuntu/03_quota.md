# Quota (사용자별 공간 할당하기)

###### 2020.03.17

> 파일시스템마다 사용자나 그룹이 생성할수 있는 파일의 용량과 갯수 제한
> 1. /etc/fstab 옵션 부분에 쿼터 관련 부분 추가
> 2. reboot or remount
> 3. 쿼터 DB 생성
> 4. 개인별 쿼터 설정

## 사용 방법
1. 10gb userDisk.vmdk 디스크 하나 추가하고 boot
2. /dev/sdb 파티션 생성 및 파일 시스템 포맷
3. /userHome 생성 후 거기에 마운트
4. /etc/fstab 맨 밑에 아래 추가
   ```sh
   /dev/sdb1    /userHome   ext4    defaults    0   0
   ```
5. 유저 추가
   ```shell
   # adduser --home /userHome/john john
   # adduser --home /userHome/bann bann
   ```
6. /etc/fstab 편집
   ```sh
   /dev/sdb1    /userHome   ext4    defaults,usrjquota=aquota.user,jqfmt=vfsv0  0   0
   ```
7. 리마운트 (재부팅효과 적용됨)
   ```shell
   # mount --options remount /userHome
   ```
8. quota 설치
   ```shell
   # apt-get -y install quota
   ```
9. 쿼터 DB 생성
    ```shell
    # cd /userHome
    # quotaoff -avug
    # quotacheck -augmn
    # rm -f aquota.*
    # quotacheck -augmn
    # touch aquota.user aquota.group
    # chmod 600 aquota.*
    # quotacheck -augmn
    # quotaon -avug
    ```
10. 사용자별 공간 할당
    ```shell
    # edquota -u john
    ```