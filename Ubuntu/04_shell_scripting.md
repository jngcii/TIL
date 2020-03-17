# Shell Script Programming

###### 2020.03.17

## Shell의 기본
> 셸은 사용자가 입력한 명령을 해석해 커널에 전달하거나, 커널의 처리 결과를 사용자에게 전달하는 역할을 한다.

### Ubuntu의 bash 셸
- ubuntu에서 기본적으로 사용하는 셸은 bash(**B**ourne **A**gain **SH**ell)이다.
- 특징
  - Alias 기능 (명령 단축 기능)
  - History 기능 (`^` 또는 `v`)
  - 연산 기능
  - Job Control 기능
  - 자동 이름 완성 기능 (`tab`)
  - 프롬프트 제어 기능
  - 명령 편집 기능

### 셸의 명령문 처리 방법
- 여러가지 옵션이나 인자 사용 가능 : `(프롬프트) 명령 [옵션...] [인자...]`
- i.e.
  ```shell
  $ ls -l
  $ rm -rf /mydir
  $ find . / -name "*.conf"
  ```

### 환경 변수
- 셸은 여러가지 환경 변수 값을 갖는데, 설정된 환경 변수는 `echo $환경변수이름` 형식으로 명령을 실행하면 확인할 수 있다.
- i.e `echo $HOSTNAME`
- 환경변수 값을 변경하려면 `export 환경변수=값` 형식을 실행한다.
- 그 외의 환경 변수는 `printenv` 명령을 실행하면 출력된다.

## 셸 스크립트 프로그래밍
- 리눅스 셸 스크립트는 C 언어와 유사한 방법으로 프로그래밍할 수 있다.

### 셸 스크립트 작성과 실행
1. name.sh 파일 작성
   ```sh
   #!/bin/sh
   echo "사용자 이름: " $USER 
   echo "홈 디렉터리: " $HOME
   exit 0
   ```
   >셸 스크립트 파일의 확장명을 지정하지 않거나, 다른것으로 지정대호 되자만, 사용자가 작성한 셸스크립트 파일은 되도록 sh확장자로 지정한다.
   - 1행 : 특별한 형태의 주석(#!)으로 bash를 사용하겠다는 의미이다. 꼭 써줘야 함
   - 2행 : echo 명령은 화면에 출력하는 명령. 먼저 '사용자 이름 : '을 출력하고 옆의 $USER 환경변수 내용을 출력
   - 4행 : 종료 코드를 반환하게 해준다. 다른 스크립트에서 이 스크립트를 호출한 후, 제대로 실행되었는지 확인하려면 적절한 종료 코드를 반환하는 것이 중요하다. 0은 성공을 의미

2. sh 명령으로 실행 
   `$ sh name.sh` 

3. 실행 가능 속성으로 변경한 후 실행
   ```shell
   # ls -l name.sh
   # chmod +x name.sh
   # ls -l name.sh

## 변수

### 변수의 기본
- 셸 스크립트에서는 변수를 사용하기 전에 미리 선언하지 않으면, 처음 변수에 값이 할당되면 자동으로 변수가 생성된다.
- 변수에 넣는 모든 값은 문자열로 취급한다.
- 변수 이름은 대소문자를 구분한다.
- 변수를 대입할때 '='좌우에는 공백이 없어야한다.
- i.e.
  ```sh
  #!/bin/sh
  myvar="Hi Woo"
  echo $myvar
  echo "$myvar"
  echo '$myvar'
  echo \$myvar
  echo 값 입력 :
  read myvar
  echo '$myvar' = $myvar
  exit 0
  ```
  >'(홑따옴표) 안의 문자는 문자열로 인식<br/>
  >\$는 $를 글자로 취급하게 한다.

### 숫자 계산
- 변수에 넣은 값은 모두 문자열로 취급한다고 했다. 
- 만약 변수에 들어 있는 값에 `+`, `-`, `*`, `/` 등의 연산을 하려면 `expr` 키워드를 사용하면 된다. 
- 수식과 함께 템플릿 리터럴(`)로 묶어줘야 한다. 
- 괄호를 사용하려면 그 앞에 역슬래시(`\`)를 붙여줘야 한다.
- 또한, `+`, `-`, `/`와 달리 `*` 앞에 역슬래시(`\`)를 붙여줘야 한다.
- i.e.
  ```sh
  #!/bin/sh
  num1=100
  num2=$num1+200
  echo $num2
  num3=`expr $num1 + 200`
  echo $num3
  num4=`expr \( $num1 + 200 \) / 10 \* 2`
  echo $num4
  exit 0
  ```
  >echo $num2 는 100+200이 출력된다.

### 파라미터 변수
- 파라미터 변수는 $0, $1, $2 등의 형태를 갖는다.
- 이는 실행하는 명령의 부분 하나하나를 변수로 지정한다는 의미이다.
- i.e. `apt-get -y install gftp`
  |명령 | apt-get | -y | install | gftp |
  |---|---|---|---|---|
  |파라미터 변수 | $0 | $1 | $2 | $3 |
- 명령 전체의 파라미터 변수는 $*로 표현한다. <br />
  *paravar.sh*
  ```sh
  #!/bin/sh
  echo "실행파일 이름은 <$0>이다."
  echo "첫번째 파라미터는 <$1>이고, 두번째 파라미터는 <$2>다."
  echo "전체 파라미터는 <$*>다."
  exit 0
  ```
  ```shell
  # sh paravar.sh 값1 값2 값3
  실팽파일 이름은 <paravar.sh>이다.
  첫번째 파라미터는 <값1>이고, 두번째 파라미터는 <값2>다.
  전체 파라미터는 <값1 값2 값3>다.
  ```


## 조건문 

### if 문과 else 문
```shell
if [ 조건 ]
then
참일 경우 실행
fi
```
>[ 조건 ]사이의 각 단어에는 모두 공백이 있어야 한다.
- i.e. *if1.sh*
  ```sh
  #!/bin/sh
  if [ "woo" = "woo" ]
  then
    echo "참입니다"
  fi
  exit 0
  ```
  > `=` : 같다, `!=` : 같지않다.<br />
  > `if [ "woo" = "woo" ]`는 `if test "woo" = "woo"`와 같다.
 
- i.e. *if2.sh
  ```sh
  #!/bin/sh
  if [ "woo" != "woo" ]
  then
    echo "true"
  else
    echo "false"
  fi
  exit 0
  ```

### 조건문에 들어가는 비교 연산자
- 문자열 비교 연산자
  | 문자열 비교 | 결과 |
  |---|---|
  |"문자열1"="문자열2" | 두 문자열이 같으면 참|
  |"문자열1"!="문자열2" | 두 문자열이 같지 않으면 참|
  |-n "문자열" | 문자열이 NULL(빈 문자열)이 아니면 참|
  |-z "문자열" | 문자열이 NULL(빈 문자열)이면 참|
- 산술 비교 연산자
  | 산술 비교 | 결과 |
  |---|---|
  |수식1 -eq 수식2 | 두 수식(또는 변수)이 같으면 참 |
  |수식1 -ne 수식2 | 두 수식(또는 변수)이 같지 않으면 참 |
  |수식1 -gt 수식2 | 수식1이 크다면 참 |
  |수식1 -ge 수식2 | 수식1이 크거나 같으면 참 |
  |수식1 -lt 수식2 | 수식1이 작으면 참 |
  |수식1 -le 수식2 | 수식1이 작거나 같으면 참 |
  |!수식 | 수식이 거짓이라면 참 |
- 파일과 관련된 조건
  | 파일 조건 | 결과 |
  |---|---|
  | -d 파일 이름 | 파일이 디렉터리이면 참 |
  | -e 파일 이름 | 파일이 존재하면 참 |
  | -f 파일 이름 | 파일이 일반 파일이면 참 |
  | -g 파일 이름 | 파일에 set-group-id가 설정되면 참 |
  | -r 파일 이름 | 파일이 읽기 가능이면 참 |
  | -s 파일 이름 | 파일 크기가 0이 아니면 참 |
  | -u 파일 이름 | 파일에 set-user-id가 설정되면 참 |
  | -w 파일 이름 | 파일이 쓰기 가능 상태면 참 |
  | -x 파일 이름 | 파일이 실행 가능 상태면 참 |
- i.e *if4.sh*
  ```sh
  #!/bin/sh
  fname=/lib/systemd/system/cron.service
  if [ -f $fname ]
  then
    head -5 $fname
  else
    echo "cron 서버가 설치되지 않았습니다."
  fi
  exit 0
  ```
- 2행 : fname변수에 cron 서버 실행파일인 /lib/systemd/system/cron.service 저장
- 3행 : fname변수에 저장된 /lib/systemd/system/cron.service 파일이 일반 파일이면 참이므로 5행을 실행, 그렇지 않으면 거짓이므로 7행을 실행
- 5행 : fname에 들어 있는 파일의 앞 5줄을 출력

### case~esac문
> 다중분기 조건문
- i.e. *case.sh*
```sh
#!/bin/sh
case "$1" in
    start)
        echo "시작~~";;
    stop)
        echo "중지~~";;
    restart)
        echo "다시 시작~~";;
    *)
        echo "뭔지 모름~~";;
esac
exit 0
```
```shell
# sh case.sh stop
중지 ~~
```

## 반복문

### for in 문
- i.e. forin1.sh
  ```sh
  #!/bin/sh
  hap=0
  for i in 1 2 3 4 5 6 7 8 9 10
  do
    hap=`expr $hap + $i`
  done
  echo "1부터 10까지의 합: "$hap
  exit 0
  ```
- i.e. forin2.sh
  ```sh
  #!/bin/sh
  for fname in $(ls *.sh)
  do
    echo "--------$fname---------"
    head -3 $fname
  done
  exit 0
  ```

### while문
- i.e. while.sh
  ```sh
  #!/bin/sh
  echo "비밀번호를 입력해주세요."
  read mypass
  while [ $mypass != "1234" ]
  do
    echo "failed. try again"
    read mypass
  done
  echo "success"
  exit 0
  ```

## export
- 외부 변수로 선언한다. 즉, 선언한 변수를 다른 프로그램에서도 사용할 수 있게 한다. <br />
 
*exp1.sh*
```sh
#!/bin/sh
echo $var1
echo $var2
exit 0
```
*exp2.sh*
```sh
#!/bin/sh
var1="지역 변수"
export var2="외부 변수"
sh exp1.sh
exit 0
```
```shell
# sh exp2.sh
외부 변수
```

## set
- 리눅스 명령을 결과로 사용하려면 `$(명령)` 형식을 사용해야한다.
- 또, 결과를 파라미터로 사용하고자 할때는 set 명령과 함께 사용한다.
- i.e. *set.sh*
  ```sh
  #!/bin/sh
  echo "오늘 날짜는 $(date) 입니다."
  set $(date)
  echo "오늘은 $4 요일 입니다."
  exit 0
  ```
    - $(date)는 date 명령을 실행할 결과를 보여준다.
    - $(date)의 결과가 $1, $2, $3 ... 등의 파라미터 변수에 저장된다.
    - 4번째 파라미터인 요일이 출력된다.