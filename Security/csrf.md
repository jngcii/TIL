# CSRF 

###### 2020.02.24

- Cross Siting Request Forgery
- 사이트 간 요청 위조는 웹사이트 취약점 공격의 하나로, 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 하는 공격을 말한다.
- 공격자가 mail이나 게시판등을 이용해 악의적인 http request의 주소를 사용자쪽으로 전달해 http://xxx.xxx.xxx/changepassword?password=abc와 같은 request를 서버로 전송하게끔하면 사용자가 해당 주소를 실행하여 원하지 않는 request를 전송하게 된다.

## 방지법 : Double-Submit Cookie

### 1. Django

- view가 CSRF 보호를 하고 있고, `POST`나 `PUT`, `DELETE`와 같은 안전하지 않은 메서드의 요청을 받으면, <strong>`csrfmiddlewaretoken`</strong>을 요청 페이로드 (바디) 에 넣어서 보내는 것을 요청한다.
- 그리고 받은 요청 바디의 `csrfmiddlewaretoken`을 함께 넘어온 쿠키에 들어있는 <strong>`csrftoken`</strong>값과 일치하는지 확인한다.
- 만약 같지 않다면 요청은 거절된다.
<br />
<br />
- 장고 템플릿은 현재 쿠키에서 `csrftoken`을 읽어 다음과같이 hidden 타입의 폼에 삽입해 전송한다.
    ```python
    <form action="https://tweeter.com/tweet" method="POST">
    <input type="hidden" name="csrfmiddlewaretoken" value="nc98P987bcpncYhoadjoiydc9ajDlcn">
    <input type="text" name="tweet">
    <input type="submit">
    </form>
    ```

### 2. DRF

- DRF(Django Rest Framework)에서 CSRF protection은 기본적으로 session authentication과 함께 동작한다.
- CSRF cookie는 <strong>`X-CSRFToken`</strong> 요청 헤더 값과 비교되어진다.
- 세션 쿠키로 인증하는 웹 클라이언트로 API를 실행하려면 항상 CSRF 쿠키의 값을 읽고이를 요청 헤더로 추가해야합니다.