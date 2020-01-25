# 입출력 처리 (IO)

###### 2020.01.25

- 외부데이터 : 하드 디스크의 파일 / 네트워크상에 존재하는 자원 / 메모리 상의 자원 등

- 외부데이터의 타입이 무엇이든 Java는 외부 데이터를 일거나 쓸때 동일하게 처리한다.

- **스트림(stream)**

    - 프로그램과 외부 데이터가 연결된 길

    - 입력 스트림 : 데이터를 읽어오기 위한 길

    - 출력 스트림 : 데이터를 출력하기 위한 길

    - 입력과 출력을 분류하는 이유는 스트림이 단방향이기 때문
        
        (한번에 하나의 처리만 가능하다. 동기적이다.)

- 입출력 API (java.io 패키지의 객체들)

    - 입력 스트림 : ~InputStream(1바이트 단위로 작업), ~Reader(2바이트 단위로 작업)

    - 출력 스트림 : ~OutputStream(1바이트 단위로 작업), ~Writer(2바이트 단위로 작업)


### I. 기본 입출력 작업

#### (1) 파일 입출력

- 입력

    - FileInputStream과 FileReader

    - 매개변수로 전달받은 파일로부터 데이터를 읽어오는 입력 스트림

    - File, FileDescriptor, String 타입으로 읽어올 수 있다.

    - 메서드 : read()

- 출력

    - FileOutputStream과 FileWriter

    - 매개변수로 전달받은 파일에 데이터를 출력하는 출력 스트림

    - 메서드 : write()

- 사용 예제

    ```java
    try(FileInputStream fi = new FileInputStream("a.txt");
        FileOutputStream fo = new FileOutputStream("b.txt");) {
        int c = 0;
        while((c = fi.read()) != -1) {
            fo.write(c);
        }
    } catch(Exception e) {
        e.printStackTrace();
    }
    ```

#### (2) 표준 입출력

- 입출력 대상을 지정하지 않았을 경우에 사용되는 입출력 대상

- 키보드 : 표준 입력 스트림 `(System.in)`

- 모니터 : 표준 출력 스트림 `(System.out)`

- 사용 예제

    ```java
    public static void main(String[] args) {
        try(InputStream keyboard = System.in; PrintStream console = System.out;) {
            int c = 0;
            while((c=keyboard.read()) != -1) {
                console.write(c);
            }
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
    ```

#### (3) 필터 스트림

- 기본 스트림은 외부 데이터와 직접 연결하는 스트림

- 필터 스트림은 기본 스트림에 추가로 사용할 수 있는 스트림

- e.g

    ```java
    //기본
    FileReader fr = new FileReader("a.txt");

    //필터
    BufferedReader br = new BufferedReader(fr);
    ```
    >기본스트림 객체를 인자로 받는다.

- FileReader는 **한바이트** 또는 인자로 전달한 바이트 배열의 수만큼 읽는다.

- BufferedReader는 외부 데이터와 프로그램 중간에 버퍼를 사용해 잠시 저장해두었다가, **줄단위**로 데이터를 읽는 readLine() 메서드를 제공하기 때문에 처리 속도가 빠르다.

<br />

### II. 파일 처리

>`java.io.File` 과 `java.nio.file` 두 패키지 모두 사용

#### (1) File 클래스

- 파일 처리를 수행하는 대표적인 객체

    ```java
    File(File parent, String child)
    File(String pathname)
    File(String parent, String child)
    File(URI uri)
    ```

- 메서드들 : `exists()`(파일/디렉터리 존재유무), `isDirectory()`, `isFile()`, `delete()`, `renameTo()`, `length()`, `canRead()`, `canWrite()`, `setReadable()`, `setWritable()`, `getPath()`, `list()`(현재경로의 파일 또는 디렉터리 목록 추출), ...


#### (2) Path 클래스

- 경로를 나타내는 클래스

- java.nio.file.FileSystem 의 getPath() 메서드

- java.nio.file.Paths 의 get() 메서드
