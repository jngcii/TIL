# 기본 API 활용하기

###### 2020.01.22


### I. 자바 API

- 자바에서 제공하는 라이브러리

    > 라이브러리 : 여러가지 기능을 구현하여 제공하는 파일

- 자바클래스파일(`*.class`)로 구성되어 있다.

- Java SE에서 제공하는 API는 자바 프로그램을 개발하기 위해 설치한 JDK에 포함되어 있다.

- API는 `&JAVA_HOME%/jmods` 폴더에 jmod 파일 형태로 저장

    >jmod파일 : 자바 9 에서 도입된 모듈 파일
    >
    >모듈 : 관련있는 여러 개의 자바 패키지를 묶어놓은 단위

- [Java API 문서](https://docs.oracle.com/en/java/javase/11/docs/api/index.html)


#### (1) Docs 이용법  e.g.기본모듈(java.base)

- java.base에서 자주 사용하는 패키지 : java.io, java.lang, java.util

- 생성자 : API를 사용하기 위해서는 해당 클래스의 인스턴스를 생성해야 한다.

    - Object
    - String
    - ...

- 필드

- 메서드

</br>



### II. 기본 API
> java.lang 패키지에 있는 기본 API 중 Object, String, StringBuffer, StringBuilder, Math 클래스

#### (1) Object 클래스

- 모든 자바 클래스의 상속구조에서 가장 루트에 있는 클래스

- 모든 객체는 이 클래스의 메서드를 상속받는다.

    1. 해시 코드 메서드

        `public int hashCode()`

        - 자바에서 new 명령문으로 힙 메모리에 새로운 인스턴스를 만들면 해당 인스턴스에 일련번호가 만들어지는데, 그런 역할을 하는 메서드 

        - `hashCode()` 메서드가 반환하는 일련번호 : 해시 코드

        - 메모리에 생성되는 주솟값을 기초로 만들어진다.

        - 유니크값이다.


    2. 클래스 정보 리턴 메서드

        `public final Class<?> getClass()`

        - getClass() 메서드는 Class 타입의 인스턴스를 생성해 반환

        - 클래스에 대한 정보만 담는 객체를 새로 생성하여 활용하고자 할 때 사용횐다.

        - e.g.

            ```java
            public class Test01 {
                public static void main(String[] args) {
                    // ...

                    Class c = obj1.getClass();

                    System.out.println(c.getName());

                    // ...
                }
            }
            ```
            >실행 결과 : java.lang.Object

            >obj1.getClass()는 obj1 인스턴스 정보를 가지는 Class 객체를 생성하여 반환해 Class 타입 변수 c 에 저장


    3. 문자열로 표현하는 메서드

        `public String toString()`

        - 인스턴스에 대한 정보를 문자열로 반환하는 메서드

        - 형식 : `getClass().getName() + 'a' + Integer.toHexString(hashCode())`

        - 참조변수를 출력할 때, `toString()`메서드를 명시하지 않으면 컴파일러가 자동으로 `toString()` 메서드를 호출하는 코드로 변환

        - e.g.

            ```java
            public class Test01 {
                public static void main(String[] args) {
                    System.out.println(obj1.toString());
                    System.out.println(obj2.toString());

                    System.out.println(obj1);
                    System.out.println(obj2);
                }
            }
            ```
            >java.lang.Object@15db9742
            >java.lang.Object@6d06d69c
            >
            >java.lang.Object@15db9742
            >java.lang.Object@6d06d69c


        - `toString()` 메서드 오버라이딩

            만약 객체 정보값을 다른 값으로 출력하고 싶다면, toString() 메서드를 오버라이딩하여 원하는 문자열을 반환하게 하면 된다.

        - e.g.
            ```java
            package com.ruby.java.ch09;

            public class Test01 {
                public static void main(String[] args) {
                    MyObject obj4 = new MyObject();
                    System.out.println(obj4);
                }
            }
            ```
            >실행 결과 : com.ruby.java.ch09.MyObject@4e25154f

            ```java
            package com.ruby.java.ch09;

            public class MyObject {
                public String toString() {
                    return "MyObject";
                }
            }
            ```
            >실행 결과 : MyObject

    4. 같은지 비교하는 메서드

        `public boolean equals(Object obj)`

        - equals()메서드는 인자로 전달된 객체와 현재 객체가 같은지 판단한다.

        - 어떤 클래스로부터 만들었는지가 아닌, **해시코드를 비교한다.**

<br />

#### (2) String 클래스

- 문자열 처리를 돕는 API

- 문자열을 생성하는 방법 : 2가지

    ```java
    String s1 = new String("java");
    String s2 = "java";
    String s3 = new String("java");
    String s4 = "java";
    ```
    >new 연산자를 사용해 만든 String 객체는 모두 다른 힙 메모리에 저장된다.
    >
    >반면, `""`로 생성된 String 객체는 모두 같은 인스턴스이다.

    ![](assets/string_memory.jpg)

    1. 문자열 비교 메서드

        `boolean equals(Object anObject)`

        `boolean equalsIgnoreCase(String anotherString)`

        - String 클래스는 Object로부터 상속받은 equals()메서드를 오버라이딩 했다.

        - String의 equals()메서드는 String 인스턴스의 문자열을 비교하여 같으면 true, 다르면 false를 반환한다.

        - equalsIgnoreCase() 메서드는 대소문자를 상관하지 않는다.

    2. 문자열 출력 메서드

        `String toString()`

        - 역시 Object로부터 toString() 메서드를 오버라이딩 했다.

        - 참조변수를 출력할 때는 자동으로 toString() 메서드가 호출된다.

    3. 문자열 정보 반환 메서드

        `int length()`

        `char charAt(int index)`

        - length()메서드는 문자열의 전체 길이를, charAt() 메서드는 인자값을 전달받은 인덱스의 문자를 반환

    4. 문자열 공백 관련 메서드

        `String trim()`

        `boolean isEmpty()`

        - trim()메서드는 문자열 양 끝에 있는 공백을 제거

        - isEmpty() 메서드는 문자열의 길이가 0인지 판단

    5. 문자열 검색 메서드

        ```java
        int indexOf(int ch)
        int indexOf(int ch, int fromIndex)
        int indexOf(String str)
        int indexOf(String str, int fromIndex)
        int lastIndexOf(int ch)
        // ...
        ```

        - indexOf()는 인자로 지정된 문자 또는 문자열이 시작되는 인덱스를 문자열의 처음부터 검색

        - lastIndexOf()는 인자로 지정된 문자 또는 문자열이 시작되는 인덱스를 문자열의 끝부터 검색

        - 만약 검색한 문자열이 없으면 `-1` 반환

        ```java
        boolean startsWith(String prefix)
        boolean startsWith(String prefix, int toffset)
        boolean endsWith(String suffix)
        ```

        - startsWith()는 인자로 전달받은 문자열이 대상 문자열의 시작부분에 포함되었는지를 판단한다.
        
        - endsWith()는 인자로 전달받은 문자열이 대상 문자열의 끝부분에 포함되었는지를 판단한다.

    6. 문자열 편집 메서드
        
        ```java
        Strint concat(String str)
        String replace(char oldChar, char newChar)
        String replaceAll(String regex, String replacement)
        String replaceFirst(String regex, String replacement)
        String toLowerCase()
        String toUpperCase()
        ```

        - concat() : 새로운 문자열 추가
        - replace() : 기존 문자열 변경
        - toLowerCase() : 소문자로
        - toUpperCase() : 대문자로

    7. 문자열 추출 메서드

        ```java
        String[] split(String regex)
        String[] split(String regex, int limit)
        String substring(int beginIndex)
        String substring(int beginIndex, int endIndex)
        ```

        - split()의 regex : 문자열을 구분할 구분자
        
        - 구분자로 문자열을 잘라서 배열로 반환

        - substring() : 문자열 슬라이싱

        - beginIndex부터 잘라서 endIndex-1까지 자름 (파이썬 슬라이싱 인덱스와 같음)

        - 두번째 인자가 없다면 끝까지 자름

    8. 문자열로 변환하는 메서드

        `static String valueOf(뭐든 다)`

        - 어떤 데이터 타입이던지 들어온 그대로를 문자열로 바꿔서 리턴한다.

        - `static` 으로 선언되어 있어서 `String.valueOf()`로 사용할수 있다.

<br />

#### (3) StringBuffer/StringBuilder 클래스

- String처럼 문자열을 처리하는 클래스

- String 클래스는 원본이 변경되지 않고 수정할때마다 메모리에 새로운 문자열이 생성되어 자리를 차지한다.

- StringBuffer/Stringbuilder 클래스는 처음 만들 때 넉넉한 메모리 공간을 확보해 그 안에서 문자열을 저장하고 수정한다.

- StringBuffer는 동시접근하는 상황에 유리하고 그 외에는 StringBuilder가 더 효율적이다.

- 생성 방법

    ```java
    StringBuilder()             // 처음 크기가 16인 StringBuilder 생성
    StringBuilder(int capacity) // 지정된 크기의 StringBuilder 생성
    StringBuilder(String str)   // 지정된 문자열을 가진 StringBuilder 생성
    ```
- 주요 메서드

| 제어자 및 타입 | 메서드 | 설명 |
| --- | --- | --- |
|StringBuilder | append(*) | 매개변수로 전달받는 값을 추가 |
|int | capacity() | 현재 크기 반환 |
|char | charAt(int) | 매개변수로 전잘받는 인덱스의 문자 반환 |
|StringBuilder | delete(int, int) | 매개변수로 전잘받는 인덱스 사이의 문자열 삭제 |
|StringBuilder | deleteCharAt(int) | 매개변수로 전잘받은 인덱스의 문자 삭제 |
|int | indexOf(*) | 매개변수로 전달받은 문자열의 시작 인덱스 반환 |
|StringBuilder | insert(int, *) | 첫 번째 매개변수로 전달받은 위치 다음에 두번째 매개변수 삽입 |
|int | lastIndexOf(*) | 매개변수로 전달받은 문자열을 뒤에서부터 검색하여 시작인덱스 반환 |
|int | length() | 문자열 전체 길이 반환 |
|StringBuilder | replace(int, int, String) | 매개변수로 전달받은 범위를 세번째 매개변수의 문자열로 대체 |
|StringBuilder | reverse() | 문자열을 거꾸로 뒤집기 |
|void | setCharAt(int, char) | 특정 위치에 문자 삽입 |
| void | setLength(int) | 문자열의 길이를 새로 지정 |
| String | substring(int) | 매개변수로 전달받은 위치부터 문자열 추출 |
| String | substring(int, int) | 문자열 일부 추출 |
| String | toString() | 문자열 반환 |
| void | trimToSize() | StringBuilder의 크기를 저장된 문자 수에 맞춤 |


#### (4) Math 클래스

- 수학적인 계산을 위한 클래스

- Math 클래스의 필드, 메서드 모두 static으로 선언되어서 `Math.변수` 및 `Math.메서드()` 형태로 사용한다.

- 생성자가 private로 선언되어서 인스턴스를 생성할 수 없다.

- 필드

    1. `Math.E` : 자연로그 (2.71828...) double 반환
    2. `Math.PI` : 원주율 (3.141592...) double 반환

- 메서드

    1. `Math.abs(-12)` : 절대값
    2. `Math.ceil(12.5)` : 올림, double 반환
    3. `Math.floor(12.5)` : 버림, double 반환
    4. `Math.round(12.5)` : 반올림
    5. `Math.max(5,8)` : 최대값
    6. `Math.pow(double a, double b)` : a의 b승, double 반환
    7. `Math.sqrt(double a)` : a의 제곱근, double 반환
    8. `Math.random()` : 0.0 ~ 1.0미만 난수 구함, double 반환


#### (5) Wrapper 클래스
> Boolean, Byte, Charactor, Double, Float, Integer, Long, Short 클래스

- 박싱과 언박싱

    기본 데이터는 값 자체만 저장되어 있으므로 데이터에 대해 처리할 대 메서드를 사용할 수 없다.

    따라서 데이터에 대한 처리 기능이 필요하거나, 반대로 연산을 해야 할때 Wrapper 클래스로 생성하거나 다시 기본 데이터로 되돌리는 박싱/언박싱이 필요하다.

    - 박싱
    
        ```java
        Boolean obj1 = Boolean.valueOf(true);
        Integer obj2 = Integer.valueOf(12);
        // ... 이런식으로 하면 된다.
        ```
    - 언박싱

        ```java
        boolean bool = obj1.booleanValue();
        int d = obj2.intValue();
        // ... 이런식으로 하면 된다.
        ```

- 오토박싱

    >JDK 1.5 부터 이러한 박싱/언박싱을 자동으로 처리해준다.

    ```java
    int n1 = 10;
    Integer obj1 = n1;

    Integer obj2 = 30
    n2 = obj2 + 40;
    // 이와 같이 가능해졌다.
    ```

- 문자열 변환

    >Wrapper 클래스는 문자열 타입의 데이터를 기본 데이터 타입으로 변환하는 메서드를 제공한다.
    >
    >모든 메서드는 static으로 선언되어 있다.

    ```java
    boolean bool = Boolean.parseBoolean("true");
    int d = Integer.parseInt("123");
    double dd = Double.parseDouble("3.14");
    float f = Float.parseFloat("10.5f");
    // 이와 같이 한다.
    ```

<br />


### III. 유틸리티 API

#### (1) StringTokensize 클래스

```java
String Tokenizer(String str)                //전달받은 문자열을 공백을 기준으로 분리
String Tokenizer(String str, String delim)  //전달받은 구분자를 이용하여 분리
```

- String의 `split()`메서드처럼 문자열을 분리하는 기능이 있는 클래스

- String의 `split()`메서드는 `String[]` 배열로 분리된 문자열을 반환하지만,  StringTokenizer 클래스는 자체적으로 분리된 문자열을 처리한다.

- 분리된 문자열 : token

- 사용 예

    ```java
    String msg = "Hi, my name is jngcii!"

    StringTokenizer st1 = new StringTokenizer(msg);
    int cnt = st1.countTokens(); // 단어수 반환



    String s = "id=guest&name=jngcii&pwd=1004";
    StringTokenizer st2 = new StringTokenizer(msg, "&");
    while(st2.hasMoreTokens()) {                // 커서 다음에 토큰이 있는지 판단
        System.out.println(st2.nextToken());    // 다음 토큰을 출력하고 커서는 그 다음으로 이동
    }
    ```

#### (2) Random 클래스

- 난수에 관한 기능을 처리하는 API

- `Random r = new Random();` 과 같이 인스턴스를 만들어 사용

- 메서드

    1. nextBoolean() : `true` 또는 `false` 반환
    2. nextDouble() : 0.0~1.0미만의 난수 반환
    3. nextInt() : int 범위의 난수 반환
    4. nextInt(int bound) : 0~bound미만의 난수 반환


#### (3) Arrays 클래스

- 배열에 관한 여러가지 기능 제공

- 모든 메서드 static으로 선언

- 메서드

    ```java
    int[] score = {80, 72, 95, 100, 50};
    // 배열에서 해당 점수 찾아 index 반환
    int a1 = Arrays.binarySearch(score, 100);
    
    // score 배열을 0번지부터 score.length만큼 복사
    int[] score2 = Arrays.copyOf(score, score.length);

    // score 배열을 3번지부터 5번지 전까지 복사
    int [] score3 = Arrays.copyOfRange(score, 3, 5);

    // 새로 만든 배열에 score 배열을 복사
    // java.lang 패키지의 System 클래스에 static으로 선언된 메서드 사용
    int[] score4 = new int[score.length];
    System.arraycopy(score, 0, score4, score.length);

    // 정렬
    Arrays.sort(score);

    // 배열처럼 생긴 String 리턴
    // e.g. [80, 72, 95, 100, 50]
    Arrays.toString(score);
    ```


#### (4) Date 클래스

    ```java
    Date d = new Date();

    String s = d.toString();
    ```


#### (5) Calendar 클래스

- 날짜와 시간 정보를 설정하여 사용할 수 있는 API

- 기본적인 날짜와 시간 정보는 설정해서 사용하도록 추상 클래스로 선언되어 있다.

- 추상클래스라서 new 명령문으로 생성하지 못하구 getInstance `static`메서드를 사용해야 한다.

    ```java
    Calendar c = Calendar.getInstance();
    ```

- Calendar 객체가 생성된 후에는 날짜와 시간을 자세하게 다룰 수 있는데, 모두 static final로 선언되어 있어 값을 수정할 수 없다.

    ```java
    c.get(Calendar.YEAR);
    c.get(Calendar.MONTH)+1;
    c.get(Calendar.DAY_OF_MONTH);
    c.get(Calendar.HOUR);
    c.get(Calendar.MINUTE);
    ```

- 생성된 Calendar의 날짜와 시간 정보를 설정하는 방법

    ```java
    void set(int field, int value)
    void set(int year, int month, int date)
    void set(int year, int month, int date, int hourOfDay, int minute)
    ```
    ```java
    Calendar c = Calendar.getInstance();
    c.clear();
    c.set(2020, 3, 19);

    int year = c.get(Calendar.YEAR);
    int month = c.get(Calendar.MONTH);
    int day = c.get(Calendar.DAY_OF_MONTH);
    ```