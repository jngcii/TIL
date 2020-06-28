# 세션과 쿠키

###### 2020.06.28

## I. Connectionless Protocol
![](assets/Screen%20Shot%202020-06-28%20at%208.23.34%20PM.png)
- 웹 서비스는 HTTP 프로토콜을 기반으로 하는데, HTTP 프로토콜은 클라이언트와 서버의 관계를 유지하지 않는 특징이 있다.
- 장점 : 서버의 부하를 줄일 수 있다.
- 단점 : 클라이언트의 요청 시마다 서버와 매번 새로운 연결이 생성되기 때문에 일반적인 로그인 상태 유지, 장바구니 등의 기능을 구현하기 어렵다.
- 이러한 Connection Protocoldml 불편함을 해결하기 위해서 세션과 쿠키를 이용한다.
- 세션과 쿠키는 클라이언트와 서버의 연결 상태를 유지해주는 방법으로, 세션은 서버에서 연결 정보를 관리하는 반면, 쿠키는 클라이언트에서 연결 정보를 관리하는데 차이가 있다.

## II. HttpServletRequest를 이용한 세션 사용
```java
@RequestMapping(value="/login", method=RequestMethod.POST)
public String memLogin(Member member, HttpServletRequest, request) {

    Member mem = service.memberSearch(member);

    HttpSession session = request.getSession();
    session.setAttribute("member", mem);

    return "/member/loginOk";

}
```

## III. HttpSession을 이용한 세션
- HttpServletRequest와 HttpSession의 차이는 거의 없으며, 단지 세션객체를 얻는 방법에 차이가 있을 뿐이다.
- `public String login(Member member, HttpServletRequest request) { ... }`
- `public String login(Member member, HttpSession session) { ... }`

## IV. 세션 삭제
- 세션을 삭제하는 방법은 세션에 저장된 속성이 더 이상 필요없을 때 이루어지는 과정으로 주로 로그아웃 또는 회원 탈퇴 등에 사용된다.
- 로그아웃
  ```java
  @RequestMapping("/logout")
  public String logout(Member member, HttpSession session) {

      session.invalidate();
      return "/member/logoutOk";

  }
  ```
- 회원 탈퇴
  ```java
  @RequestMapping(value="/remove", method=RequestMethod.POST)
  public String removeMember(Member member, HttpServletRequest request) {

      service.memberRemove(member);

      HttpSession session = request.getSession();
      session.invalidate();

      return "/member/removeMemberOk";

  }
  ```

## V. 세션 주요 메서드 및 플로어
|세션 메서드 | 기능|
| --- | --- |
| getId() | 세션 ID를 반환한다. |
| setAttribute() | 세션 객체에 속성을 저장한다. |
| getAttribute() | 세션 객체에 저장된 속성을 반환한다. |
| removeAttribute() | 세션 객체에 저장된 속성을 제거한다. |
| setMaxInactiveInterval() | 세션 객체의 유지시간을 설정한다. |
| getMaxInactiveInterval() | 세션 객체의 유지시간을 반환한다. |
| invalidate() | 세션 객체의 모든 정보를 삭제한다. |
