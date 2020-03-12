# File System

###### 2020.03.11

## File and File System

### I. File
- 이름을 통해 접근하는 것
- "A named collection of related information"
- 일반적으로 비휘발성의 보조기억장치에 저장
- 운영체제는 다양한 저장 장치를 file이라는 동일한 논리적 단위로 볼 수 있게 해줌
- Operation
  - create, read, write, reposition(lseek), delete, open, close 등

### II. File attribute (혹은 파일의 metadata)
- 파일 자체의 내용이 아니라 파일을 관리하기 위한 각종 정보
  - 파일 이름, 유형, 저장된 위치, 파일 사이즈
  - 접근 권한 (읽기/쓰기/실행), 시간 (생성/변경/사용), 소유자 등

### III. File system
- 운영체제에서 파일을 관리하는 부분
- 파일 및 파일의 메타데이터, 디렉토리 정보 등을 관리
- 파일의 저장 방법 결정
- 파일 보호 등


<br />

## Directory and Logical Disk

### I. Directory
- 파일의 메타데이터 주 일부를 보관하고 있는 일종의 특별한 파일
- 그 디렉터리에 속한 파일 이름 및 파일 attribute들
- operation
  - search for a file, create a file, delete a file
  - list a directory, rename a file, traverse the file system

### II. Partition (=Logical Disk)
- 하나의 (물리적) 디스크 안에 여러 파티션을 두는게 일반적
- 여러 개의 물리적인 디스크를 하나의 파티션으로 구성하기도 함
- (물리적) 디스크를 파티션으로 구성한 뒤 각각의 파티션에 file system을 깔거나 swapping area 등 다른 용도로 사용할 수 있음


<br />

## File system 흐름

### I. `open()` system call
> open("/a/b/c")
![](assets/read-file.jpeg)
- 디스크로부터 파일 c의 메타데이터를 메모리로 가지고 옴
- 이를 위하여 directory path를 search
  - 루트 디렉터리 "/"를 open하고 그 안에서 파일 "a"의 위치 획득
  - 파일 "a"를 open한 후, read하여 그 안에서 파일 "b"의 위치 획득
  - 파일 "b"를 open한 후, read하여 그 안에서 파일 "c의 위치 획득
  - 파일 "c"를 open한다
- Directory path의 search에 너무 많은 시간 소요
  - Open을 read/write와 별도로 두는 이유임
  - 한번 open한 파일은 read/write 시 directory search 불필요
- Open file table
  - 현재 open 된 파일들의 메타데이터 보관소 (in memory)
  - 디스크의 메타데이터보다 몇 가지 정보가 추가
    - Open한 프로세스의 수
    - File offset: 파일 어느 위치 접근 중인지 표시 (별도 테이블 필요)
- File descriptor (file handle, file control block)
  - Open file table에 대한 위치 정보 (프로세스 별)

### II. Mounting
- 다른 partition의 파일 시스템을 루트 파티션에 가져오기 위한 것

### III. Access Method
- 시스템이 제공하는 파일 정보의 접근 방식
  - 순차 접근
    - 카세트 테이프를 사용하는 방식처럼 접근
    - 읽거나 쓰면 offset은 자동적으로 증가
  - 직접 접근
    - LP 레코드 판과 같이 접근하도록 함
    - 파일을 구성하는 레코드를 임의의 순서로 접근할 수 있음

<br />

## File Protection
>각 파일에 대해 누구에게 어떤 유형의 접근을 허락할 것인가? (read/write/execution)
### I. Access Control 방법
- Access control Matrix
  | | file 1 | file 2 | file 3 |
  |---|---|---|---|
  |user1|rw | rw | r|
  |user2|rw | r | r |
  |user3|r | | |
- Access control list: 파일별로 누구에게 어떤 접근 권한이 있는지 표시
- Capability: 사용자별로 자신이 접근 권한을 가진 파일 및 해당 권한 표시

### II. Grouping
- 일반적으로 사용하는 방법
- 전체 user를 owner, group, public의 세 그룹으로 구분
- 각 파일에 대해 세 그룹의 접근 권한(rwx)을 3비트씩으로 표시
- i.e. UNIX   rwxr--r-- (owner group other 순)
- 
### III. Password
- 파일마다 password를 두는 방법 (디렉터리 파일에 두는 방법도 가능)
- 모든 접근 권한에 대해 하나의 password: all-or-nothing
- 접근 권한별 password: 암기 문제, 관리 문제