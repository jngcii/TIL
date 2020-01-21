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