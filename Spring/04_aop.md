# **A**spect **O**riented **P**rogramming

###### 2020.06.23

## I. AOP 방법론
- 흩어져있는 코드를 한 곳으로 모으는 코딩 기법
- 예시 (흩어진 AAAA와 BBBB)
  ```java
  class A {
    method a {
      AAAA
      오늘은 7월 4일 미국 독립기념일이래요.
      BBBB
    }

    method b {
      AAAA
      저는 아침에 운동을 했어요.
      BBBB
    }
  }

  class B {
    method c {
      AAAA
      점심은 뭘 먹을까요
      BBBB
    }
  }
  ```
- 예시 (모아놓은 AAAA와 BBBB)
  ```java
  class A {
    method a() {
      오늘은 7월 4일 미국 독립기념일이래요.
    }

    method b() {
      저는 아침에 운동을 했어요.
    }
  }

  class B {
    method c() {
      점심은 뭘 먹을까요
    }
  }

  class AAAABBBB {
    method aaaa() {
      AAAA
    }

    method bbbb() {
      BBBB
    }
  }
  ```

## II. AOP 사용 예제
- `PetRepository.java`
  ```java
  public interface PetRepository extends Respository<Pet, Integer> {

    @Query("SELECT ptype FROM PetType ptype ORDER BY ptype.name")
    @Transactional(readOnly=true)
    List<PetType> findPetTypes();
  }
  ```
- @Transactional(readOnly=True) 가 AOP의 예제
- @Transactional 코드가 AAAA BBBB 처럼 모든 코드를 다 감싼다.
- 사실 @Transactional 코드는 모든 스프링코드에 적용되어있다.
- 다만 readOnly=true라는 옵션을 주기위해 명시적으로 표시한 것이다.
- 예를들어 AAAA 자리에서 트랜잭션 매니저를 가지고 트랜잭션의 오토커밋을 false로 만든다.
- BBBB 자리에서 트랜잭션을 커밋한다.
- AAAA, BBBB 사이에는 모두 try catch로 묶여있다.
- catch 구문에서 어떠한 문제가 생겼을때, transcation을 rollback 시킨다.

## III. 특정 어노테이션이 붙은 메서드만 시간 로깅 찍기

### 1) 패키지 선언
- `main/java/org.s.../` 에서 new -> package 선택 후 aspect 패키지 만들기

### 2) 어노테이션 선언
- 새로운 패키지에 LogExecutionTime이라는 어노테이션 java 파일 생성
- `LogExecutionTime.java`
  ```java
  package org.springframework.samples.petclinic.aspect;

  import java.lang.annotation.ElementType;
  import java.lang.annotation.Retention;
  import java.lang.annotation.RetentionPolicy;
  import java.lang.annotation.Target;

  @Target(ElementType.METHOD)
  @Retention(RetentionPolicy.RUNTIME)
  public @interface LogExecutionTime {
  }
  ```
  - Target : 메서드에 적용
  - Retention : 런타임중에 로그가 뽑힘

### 3) 원하는 메서드에 어노테이션 붙이기
- ex : initCreationForm, processCreationForm, initFindForm

### 4) 어노테이션을 처리할 녀석을 만들기
- `LogAspect.java`
  ```java
  package org.springframework.samples.petclinic.aspect;

  import org.aspectj.lang.ProceedingJoinPoint;
  import org.aspectj.lang.annotation.Around;
  import org.aspectj.lang.annotation.Aspect;
  import org.slf4j.Logger;
  import org.slf4j.LoggerFactory;
  import org.springframework.stereotype.Component;
  import org.springframework.util.StopWatch;

  @Component
  @Aspect
  public class LogAspect {

    Logger logger = LoggerFactory.getLogger(LogAspect.class);

    @Around("@annotation(LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
      StopWatch stopWatch = new StopWatch();
      stopWatch.start();

      Object res = joinPoint.proceed();

      stopWatch.stop();
      logger.info(stopWatch.prettyPrint());

      return res;
    }
  }
  ```
  - @Component : 스프링 빈으로 설정되어 있어야 실행됨
  - joinPoint : 메서드