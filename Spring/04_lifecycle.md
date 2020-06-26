# Lifecycle

###### 2020.06.26

> 스프링 컨테이너와 빈 객체가 어느 시점에 생성이 되고 어느 시점에 소멸이 되는지, 또 그것을 이용해 개발자가 무엇을 할 수 있는지

## I. 스프링 컨테이너 생명 주기
![](assets/Screen%20Shot%202020-06-26%20at%205.16.58%20PM.png)
- `GenericXmlApplicationContext`를 인스턴스화해 컨테이너 생성
- 컨테이너가 생성된다는 것은 메모리에 스프링 컨테이너가 만들어진다는 것
- 컨테이너가 생성됨가 동시에 빈(Bean)객체가 생성된다.
- `getBean()`메서드를 통해 빈 객체를 얻어 사용하고 `close()`메서드를 통해 컨테이너 자원을 소멸시킨다. (빈객체도 소멸된다.)

## II. 빈(Bean) 생명 주기
- 스프링 컨테이너가 생성될 때 빈 객체도 생성/주입되고, 스프링 컨테이너가 종료될 때 빈 객체 역시 소멸된다.
- 빈 객체는 `InitializingBean`(`afterPropertiesSet`메서드를 정의)인터페이스와 `DisposableBean`(`destroy`메서드를 정의)인터페이스를 구현한 객체
- `afterPropertiesSet()` : 빈객체 생성시점에 호출
- `destory()` : 빈객체 소멸시점에 호출
- 위 메서드가 필요한 경우 예시
  - DB 연결 및 인증
  - 다른 네트워크 상의 PC에 인증
  - ...

### `bookRegisterService` 빈 객체에서 `afterPropertiesSet()`, `destroy()` 메서드 사용하기
- xml파일
  ```xml
  <bean id="bookRegisterService" class="com.brms.book.service.BookRegisterService" />
  ```
- java파일
  ```java
  public class BookRegisterService implements InitializingBean, DisposableBean{

      @Autowired
      private BookDao bookDao;

      public BookRegisterService() { }

      public void register(Book book) {
          bookDao.insert(book);
      }

      @Override
      public void afterPropertiesSet() throws Exception {
          System.out.println("bean 객체 생성");
      }    

      @Override
      public void destroy() throws Exception {
          system.out.println("bean 객체 소멸");
      }

  }
  ```

## III. init-method, destory-method 속성
> 인터페이스를 구현하지 않고 xml 속성에 정의하여 사용할 수도 있다.
- xml파일
  ```xml
  <bean id="bookRegisterService" class="com.brms.book.service.BookRegisterService" init-method="initMethod" destroy-method="destroyMethod" />
  ```
- java파일
  ```java
  public class BookRegisterService {

      @Autowired
      private BookDao bookDao;

      public BookRegisterService() { }

      public void register(Book book) {
          bookDao.insert(book);
      }

      public void initMethod() {
          System.out.println("BookRegisterService 빈 객체 생성")
      }

      public void destroyMethod() {
          System.out.println("BookRegisterService 빈 객체 소멸")
      }
  }
  ```