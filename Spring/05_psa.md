# **P**ortable **S**ervice **A**bstraction

###### 2020.06.24

- 잘 맞는 인터페이스
- 나의 코드 중간에 PSA가 없으면 확장성이 없기때문에 테스트도 만들기 어렵고 특정 기술에 특화되어있기 때문에 어떠한 기술을 바꿀때마다 나의 코드가 바뀐다.
- 어떤 잘 만든 인터페이스를 사용해서 내 코드를 작성하면 테스트하기도 좋고 다른 것으로 바꿔 끼기도 좋다. 그리고 그 인터페이스 아래 있는 기술 자체를 바꿔도 (예를 들어, JDBC를 쓰다가 Hibernate를 쓰고 Hibernate를 쓰다가 JPA를 쓰는) 나의 코드가 바뀌지 않는다.
- 스프링이 제공해주는 대부분의 API가 전부 PSA이다.
- 스프링 레퍼런스 중 PSA는
  - Resources (File system 리소스를 읽어올 것이냐 classpath리소스를 읽어올 것이냐 HTTP로 접근할수 있는 리소스를 읽어올 것이냐)
  - i18n
  - Validation
  - Data Binding
  - Type Conversion
  - Transactions
  - DAO support
  - ORM
  - ...

## I. Spring Transaction
- @Transactional
  - @Transactional이라는 어노테이션을 처리할 Aspect가 어딘가 있다.
  - 그 Aspect에서는 Transaction 처리를 기술에 독립적인 PlatformTransactionManager라는 인터페이스를 통해서 코딩을 해놨다.
  - 그래서 PlatformTransactionManager의 구현체들(JpaTransactionManager, DatasourceTransactionManager, HibernateTransactionManager, ...)이 바뀌더라도 Aspect의 코드는 바뀌지 않는다.
  - Aspect 안에서 PlatformTransactionManager를 가져다 쓰게 된다.

## II. Spring Web MVC
- @Controller와 @GetMapping을 사용해서 Web MVC를 구현하고 있다.
- 작성한 코드가 Servlet에 쓰이는 거일 수도 있고 Reactive에 쓰이는 거일 수도 있다.