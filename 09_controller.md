# Controller 객체 구현

###### 2020.06.28

## I. `@RequestMapping()`
- 속성
  - value : 사용자가 요청한 url을 명시
    - `value = "/member/join"`
  - method : 사용자가 요청한 method를 명시
    - `method="RequestMethod.POST`
    - default는 GET 메서드
  - value 속성만 명시할 경우네는 그냥 url 문자열만 입력하면 된다.
    - `@RequestMapping("/member/join")`
- class 위에도 붙일 수 있는데 이럴경우 메서드의 value와 class의 value를 합쳐서 판단한다.
  ```java
  @RequestMapping("/member")
  @Controller
  class MemberController {

      // ...

      @RequestMapping(value="/join", method=RequestMethod.POST)
      public String join(Model model, HttpServletRequest request) {
          // ...
      }
      // ...

  }
  ```

## II. 커맨드 객체
- 컨트럴러 메서드에서 인자로 `Model model, HttpServletRequest request`를 통해 데이터를 받고 `request.getParameter`를 통해 사용자 입력을 받아오지 않고 Member라는 커맨드 객체자체를 통해 가져올 수 있다.
  ```java
  @RequestMapping(value="/join", method=RequestMethod.POST)
  public String join(Member member) {
      service.memberRegister(member.getMemId(), member.getMemPw(), member.getMemName());

      // model.addAttribute() 없이도 곧바로 member를 전달함

      return "memJoinOk";
  }
  ```
  ```jsp
  <p> ID : ${member.memId} </p>
  <!-- ... -->
  ```
  - 이렇게하면 자동으로 getter가 호출되므로 반드시 커맨드 객체에 getter가 선언되어 있어야한다.

## III. `@ModelAttribute`
- `@ModelAttribute`를 사용하면 커맨드 객체의 이름을 변경할 수 있고, 이렇게 변경된 이름은 뷰에서 커멘드 객체를 참조할 때 사용된다.
  ```java
  public String memLogin(@ModelAttribute("mem") Member member)
  ```
  ```jsp
  <p> ID : ${mem.memId} </p>
  ```

## IV. 커맨드 객체 프로퍼티 데이터 타입
- 데이터가 기초데이터 타입인 경우는 Spring MVC framework이 알아서 맞춰서 보내주지만 그렇지 않을 경우에는 (memPhones) 새로운 객체를 필요로 한다.
  ```java
  private String memId;
  private List<MemPhone> memPhones;
  private String[] memFSports;
  ```
  ```java
  public class MemPhone {
      private String memPhone1;
      private String memPhone2;
      private String memPhone3;
      // getter
      // setter
  }
  ```
  ```jsp
  ID :
  <input type="text" name="memId" />

  PHONE1 :
  <input type="text" name="memPhones[0].memPhones1" size="5" />
  <input type="text" name="memPhones[0].memPhones2" size="5" />
  <input type="text" name="memPhones[0].memPhones3" size="5" />

  PHONE2 :
  <input type="text" name="memPhones[1].memPhones1" size="5" />
  <input type="text" name="memPhones[1].memPhones2" size="5" />
  <input type="text" name="memPhones[1].memPhones3" size="5" />

  FAVORITE SPORT :
  <input type="checkbox" name="memFSprots" value="baseball" />baseball,
  <input type="checkbox" name="memFSprots" value="soccer" />soccer,
  <input type="checkbox" name="memFSprots" value="basketball" />basketball,
  ```

## V. Model & ModelAndView
- 컨트럴러에서 뷰에 데이터를 전달하기 위해 사용되는 객체로 Model과 ModelAndView가 있다.
- 두 객체의 차이점은 Model은 뷰에 데이터만을 전달하기 위한 객체이고, ModelAndView는 데이터와 뷰으 이름을 함께 전달하는 객체이다.
- Model : 원래 하던 것
- ModelAndView
  ```java
  @RequestMapping(value="/memModify", method=RequestMethod.POST)
  public ModelAndView memModify(Member member) {

      Member[] members = service.memberModify(member);

      ModelAndView mav = new ModelAndView();
      mav.addObject("memBef", members[0]);
      mav.addObject("memAft", members[1]);

      mav.setViewName("memModifyOk");

      return mav;

  }
  ```