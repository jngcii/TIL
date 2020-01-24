# 컬렉션 API 활용하기 (JAVA Collection Framework)

###### 2020.01.22

>**기존 배열의 크기가 정해져 있거나, 삭제 및 삽입의 연산에서의 비효율성, 구조적 한계 등을 보완할 수 있는 자료구조 API 모음**
>
>List, Set, Map 세가지 계열이 있다.
>
>List와 Set은 Iterable과 Collection을 상속하고 있어서 다음 메서드들을 공통으로 사용할 수 있다.
>
> - forEach() : 지정된 명령문 실행
> - iterator() : 원하는 타입의 iterator 생성
> - add() : 전달받은 객체를 컬렉션에 추가
> - addAll() : 전달받은 컬렉션객체를 컬렉션에 추가
> - claer() : 컬렉션의 모든 요소 삭제
> - contains() : 전달받은 객체 포함 여부 판단
> - equals() : 전달받은 객체와 현재 컬렉션 동일 여부 판단
> - hashCode() : 해쉬코드 반환
> - isEmpty() : 비어있는지 여부 판단
> - remove() : 전달받은 객체를 컬렉션에서 삭제
> - size() : 컬렉션의 요소 개수
> - stream() : 컬렉션을 소스로 하는 스트림 생성
> - toArray() : 컬렉션의 요소들을 가지는 Object 타입의 배열 생성
> - toArray(T[] a) : 컬렉션의 요소들을 가지는 T 타입의 배열 생성

### I. List

- List의 특징은 저장되는 데이터의 순서가 보장된다는 것

- List를 상속하는 ArrayList와 Vector는 배열처럼 데이터가 저장될 때마다 인덱스가 부여된다.

- LinkedList는 데이터가 저장될 때, 이전에 저장된 데이터와 이후 저장된 데이터의 정보를 포함한다.

#### (1) ArrayList 클래스

```java
ArrayList()
ArrayList(int initialCapacity)
```

- 배열과 유사하지만 크기를 변경할 수 있다!!

- 인자없이 생성하면 크기 10인 ArrayList 생성됨. ( 하지만 유동적이다!! )

- 인자에 50을 넣으면 기본 크기 50

- ArrayList를 사용해 만든 배열의 내부 데이터들은 기본적으로 Object 부모 타입을 참조한다.

- 즉, 부모로부터 상속한 내용에만 접근할 수 있다.

    ```java
    ArrayList list = new ArrayList();
    String s = "java";
    Integer i = 123;
    list.add(s);
    list.add(i);
    int len2 = list.get(0).length(); // 오류 발생
    ```
    >list.get(0)은 `Object s = "java"`를 반환하는데,  참조 타입이 String이 아닌 Object가 기본값이기 때문에 String의 메서드인 length()를 사용할 수 없다.

- 사용하는 방법
    `int len2 = ((String)list.get(0)).length();

- **제네릭**

    데이터가 저장될 때, 지정된 타입이 맞는지 검사하고 데이터를 추출할 때 지정된 탕입으로 변환한 후 반환

    `클래스<데이터 타입> 변수 = new 클래스<데이터 타입>();`
    
    `ArrayList<String> list = new ArrayList<String>();`
    > 이렇게 하면 저장될때 String 참조타입으로 저장되고, get으로 가져올때도 자동으로 String 타입으로 변환되어 반환된다.

    **예시**
    ```java
    // String 타입만 저장할 수 있는 자료구조 ArrayList 생성 (기본크기 10)
    ArrayList<String> list = new ArrayList<String>();

    // String 타입 데이터 추가
    list.add("서울"); list.add("북경"); list.add("도쿄");
    ```

- `toArray()` 메서드

    ArrayList의 데이터들을 가진 Object 타입의 배열을 생성하여 변환

    ```java
    // 1. 기본방법
    Object obj[] = list.toArray();


    // 2. 원하는 타입의 배열로 받기 위해서는?
    String cities[] = new String[0]
    // 특정 타입의 배열을 인자로 전달하면 된다!
    // 배열의 크기보다 ArrayList의 크기가 클때는 자동으로 배열의 크기가 변경되므로 new String[0]로 배열 생성
    cities = list.toArray(cities);
    ```

- `asList()` 메서드

    - java.util 패키지의 Arrays 클래스의 배열처리 메서드

    - 인자로 전달한 데이터를 가지는 List 객체를 생성해 반환

    ```java
    List<String> list2 = Arrays.asList("서울", "뉴욕", "도쿄");
    ```
    ```java
    list.addAll(list2); // list2를 list 뒤에 연결
    list.retainAll(list2); // list에서 list2의 데이터들만 남겨두고 모두 삭제
    ```


#### (2) Vector 클래스

- ArrayList는 동시 접근 동기화 처리가 안되고, Vector는 안전하게 동시 사용을 처리할 수 있도록 설계된 클래스이다.

- 나머지 내용은 같다. 동시접근이 필요 없을때는 ArrayList가 효율적이다.


#### (3) LinkedList 클래스

`LinkedList<E> list = new LinkedList<E>();

- LinkedList는 ArrayList처럼 메모리에 순서대로 저장하는 것이 아니라 메모리에 저장할 수 있는 공간이 있다면 위치에 상관없이 저장한다.

- 메모리 효율면에서 효과적이다.

- 노드(: **데이터의 정보**와 **다음 데이터의 주소** )를 하나의 단위로 한다.

- Single LinkedList, Double LinkedList Circular LinkedList 등이 있다.

- 가정 처음 생성된 노드를 **head**, 마지막에 생성된 노드를 **tail**이라 부른다.

- ArrayList보다 더 많은 메모리를 사용하지만, 데이터의 삭제, 삽입 작업이 간단하다.

- List를 상속하고 있어서 ArrayList와 기본적인 메서드 사용은 비슷하다.

- 더 사용하는 메서드들

    `addFisrt`, `addLast`, `element`(head 추출), `getFisrt`, `getLast`, `peek`(head 추출), `poll`(head 추출 후 삭제), `pop`(tail 추출), `push`(tail에 추가), ...

    ```java
    // 빈 링크들리스트 만들기
    LinkedList<String> list = new LinkedList<String>();

    // 미리 초기화된 링크드리스트 만들기
    List<String> tmpList = Arrays.asList("서울", "대전", "구미");
    LinkedList<String> list = new LinkedList<String>(tmpList);

    list.add("부산");
    list.add("제주");

    for
    ```

<br />

### II. Map

- 인덱스 또는 다른 데이터의 위치 정보를 가지지 않는다.

- 순서를 보장하지 않는다.

- key, value로 구성 (파이썬의 Dictionary)

- Map Interface의 메서드

    1. clear()
    2. compute(k, func) : 키값에 작업 수행
    3. computeIfAbsent(k, func) : 키값이 없을때 작업 수행
    4. computeIfPresent(k, func)
    5. containsKey(Object key)
    6. contiansValue(Object value)
    7. equals(Object o)
    8. get(Object key) : 키값에 해당하는 value 추출
    9. put(k, v) : 키와 값 추가
    10. remove(Object key) : 키 있으면 삭제
    11. replace(k, v) : 키를 찾아 값을 v로 변경
    12. values() : 맵의 모든 값에 대한 정보를 가지는 컬렉션 생성


#### (1) Entry 인터페이스

- Map은 여러 개의 Entry로 구성된 컬렉션이다.

- Map 인터페이스의 내부 인터페이스로 선언된 Entry는 Map.Entry로 표현한다.


#### (2) HashMap 클래스

- 해싱 검색 방법을 사용해 많은 양의 데이터를 검색할 때 효율적이다.
    > 해싱 : 메모리에 저장된 데이터를 빨리 찾을 수 있도록 주소에 직접 접근할 수 있는 짧은 길이의 값이나 키로 변환하는 것

`HashMap<String, String> users = new HashMap<String, String>();

- 인자에 용량을 미리 지정할 수 있고, 75%만큼 차면 두배로 용량이 변경되는 등의 지정을 할 수도 있다.

- 사용 예제

    ```java
    String words[] = {"A", "B", "C"};
    String starts[] = {"Apple", "Banana", "Chocolate"};

    Hashmap<String, String> dic = new HashMap<String, String>();

    for(int i=0; i < words.length; i++) {
        dic.put(words[i], starts[i]);
    }

    dic.replace("B", "Beer");

    dic.containKey("B");

    doc.remove("B");
    ```
    
#### (3) Hashtable 클래스

- null 키와 null 값을 저장할 수 없는 HashMap

#### (4) TreeMap 클래스

    `TreeMap()`

- 트리 형태로 데이터 저장 (이진트리 데이터구조)

- 기존의 데이터와 새로운 데이터를 비교하여 저장되는 위치 결정

- `노드`가 기본 단위

- 데이터 저장, 삽입, 삭제, 검색은 항상 루트부터 탐색을 시작

- 사용 예시

    ```java
    TreeMap<String, String> users = new TreeMap<String, String>();

    users.put("20080319", "A");
    users.put("20070620", "B");
    users.put("20050817", "C");
    users.put("20120728", "D");

    // 받을 준비하기
    Map.Entry<String, String> entry = null;

    // 가장 날짜가 빠른거
    entry = users.firstEntry();
    ```

<br />

### III. Set

> List와는 달리 데이터의 순서가 의미가 없다.
>
> 해시코드는 Object클래스의 hashCode() 메서드에서 반환하는 값을 사용
> 
> 해시코드를 사용해 데이터를 처리해 컬렉션 중 가장 빠르게 검색

#### (1) HashSet 클래스

- e.g. 로또 추첨

    ```java
    Random number = new Random();
    HashSet<Integer> lotto = null;
    for(int i = 0; i < 5; i++) {
        lotto = newHashSet<Integer>();

        for(int j=0; lotto.size() <= 6; j++) {
            lotto.add(number.nextInt(46));
        }

        List<Integer> L = new ArrayList<Integer>(lotto);
        Collections.sort(L);
    }
    ```

#### (2) TreeSet 클래스

- Tree와 set 특성을 동시에 가지는 컬렉션

- 순서보장 x, 중복된 데이터 저장 x, 트리 구조로 저장

- TreeMap과 거의 유사

    ```java
    TreeSet<Integer> score = new TreeSet<Integer>();

    score.add(90);
    score.add(100);
    score.add(85);
    score.add(65);
    score.add(50);
    score.add(75);

    score.fisrt(); score.last(); //... 등등 많은 메서드 존재
    ```