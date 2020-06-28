# 리다이렉트와 인터셉터

###### 2020.06.28

## I. 리다이렉트 (Redirect)
> 컨트롤러에서 뷰를 분기하는 방법
- 지금의 페이지에서 특정 페이지로 전환하는 기능
  ```java
  @RequestMapping("/modifyForm")
  public String modifyForm(Model model, HttpServletRequest request) {

      HttpSession session = request.getSession();
      Member member = (Member)session.getAttribute("member");

      if(member == null) {
          return "redirect:/";
      } else {
          model.addAttribute("member", service.memberSearch(member));
      }

      return "/member/modifyForm";
  }
  ```
  ```java
  @RequestMapping("/modifyForm")
  public String removeForm(HttpServletRequest request) {

      ModelAndView mav = new ModelAndView();

      HttpSession session = request.getSession();
      Member member = (Member)session.getAttribute("member");

      if(member == null) {
          mav.setViewName("redirect:/");
      } else {
          mav.addObject("member", member);
          mav.setViewName("/member/removeForm");
      }

      return mav;
  }
  ```

## II. 인터셉터 (Interceptor)
> 컨트롤러 실행 전/후에 특정 작업을 가능하게 하는 방법
- 리다이렉트를 사용해야 하는 경우가 많은 경우 HandlerInterceptor를 이용할 수 있다.
  ![](assets/Screen%20Shot%202020-06-28%20at%208.57.40%20PM.png)
  - preHandle() :가장 많이 사용
    - 컨트롤러가 작업하기전에 먼저 작업
  - postHandle()
    - 컨트롤러가 작업한 후에 작업
  - afterCompletion()
    - 컨트럴러와 뷰가 모두 작업한 후에 작업
- `HandlerInterceptor`는 인터페이스
  - 모두 구현하기 힘듬
- `HandlerInterceptor`구현한 `HandlerInterceptorAdapter`를 상속받아 클래스를 만든 후 스프링 설정 파일로 설정해주면 된다.
- `/src/main/java/com/jngcii/pjt/member/MemberLoginInterceptor.java`
  ```java
  public class MemberLoginInterceptor extends HandlerInterceptorAdapter {

      @Override
      public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {

          HttpSession session = request.getSession(false);
          if(session != null) {
              Object obj = session.getAttribute("member");
              if(obj != null) return true;
          }

          response.sendRedirect(request.getcontextPath() + "/");
          return false;

      }

  }
  ```
- `/src/main/webapp/WEB-INF/spring/appServlet/servlet-context.xml`
  ```xml
  <beans:beans>
    <!-- ... -->

    <interceptors>
      <mapping path="/member/modifyForm" />
      <mapping path="/member/removeForm" />
      <!--
        <mapping path="/member/**" />
        <exclude-mapping path="/member/joinForm" />
        ...
      -->
      <beans:bean class="com.jngcii.pjt.member.MemberLoginInterceptor" />
    </interceptros>
  </beans:beans>
  ```