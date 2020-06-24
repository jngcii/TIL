# **I**nversion **o**f **C**ontrol

###### 2020.06.23

- 제어의 역전
- 제어가 뒤바뀐 것
- 무엇에 대한 제어가 뒤바뀐것인가?
  - 여기서는 주로 의존성
  - 의존성에 대한 컨트럴이 뒤바뀌었다.
- 원래는 어땠길래?
  - 원래 의존성에 대한 제어권은 자기 자신이 들고 있는 것이다.
  - 제어역전을 사용하지 않았을 때의 예시
    ```java
    class OwnerController {
      private OwnerRepository owners = new OwnerRepository();
    }
    ```
    - `OwnerRepository`는 `OwnerController`의 의존성이다.
    - `OwnerRepository`가 있어야 `OwnerController`를 제대로 사용할 수 있다.
    - `OwnerController`는 `OwnerRepository`를 필요로 한다.
    - `OwnerRepository`가 있어야지만 화면에서 넘어온 데이터를 저장도 하고, owners에서 꺼네서 화면으로 보여주기도 가능하다.
    - **다만 그걸 누가 만드느냐, 누가 관리하느냐가 관건**
- 의존 역전이란
  - 의존성을 내가 관리하지 않고, 나 이외에 밖에서 누군가가 넣어주면 사용한다.
  - 내가 쓸 놈의 타입만 맞으면 어떤거든 상관없지 뭐
  - 그래야 내 코드 테스트 하기도 편하지
  - 제어역전을 사용했을 때의 예시
    ```java
    class OwnerController {
      private OwnerRepository owners = null;

      public OwnerController(OwnerRepository owners) {
        this.owners = owners;
      }
    }

    class OwnerControllerTest {
      @Test
      public void create() {
        OwnerRespository repo = new OwnerRepository();
        OwnerController controller = new OwnerController(repo);
      }
    }
    ```