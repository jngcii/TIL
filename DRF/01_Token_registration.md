# 간단한 User registration & login form 만들기

###### 2020.02.27

## 기본 세팅

### I. Django Project Setup

- python 3.7, pipenv 설치 후 `pipenv shell` 환경에서 실행

1. Django와 DRF 설치
   
   ```shell
   $ pip install django djangorestframework
   ```

2. 새 프로젝트 생성

    ```shell
    $ django-admin startproject myproject
    ```

3. 프로젝트의 Installed app 리스트에 DRF 추가

    ```python
    # myproject/settings.py

    INSTALLED_APPS = (
        ...
        'rest_framework',
    )
    ```
4. migrate

    ```shell
    $ python manage.py migrate
    ``` 

### II. User Registration - Serializers

- 이 튜토리얼에서는 장고 기본 유저(django.contrib.auth.models)만을 사용
- username, email, password만을 회원정보를 받음

1. users app 생성

    ```shell
    python manage.py startapp users
    ```

2. users 폴더에 serializers.py 파일 생성
3. UserSerizliser정의

    ```python
    from rest_framework import serializers
    from rest_framework.validators import UniqueValidator
    from django.contrib.auth.models import User

    class UserSerializer(serializers.ModelSerializer):
        email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
        )
        username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
        )
        password = serializers.CharField(
            min_lenght=8, write_only=True
        )

        def create(self, validated_data):
            user = User.objects.create_user(
                validated_data['username'],
                validated_data['email'],
                validated_data['password']
            )
            return user

        class Meta:
            model = User
            fields = ('id', 'username', 'email', 'password')
    ```


### III. View 만들기

- Serializer 가 있으니 View를 만들수 있다!
  
1. users/tests.py를 만들고 `test_create_user`라는 새로운 유저를 생성하는 간단한 test code를 추가한다.

    ```python
    from django.core.urlresolvers import reverse
    from rest_framework.test import APITestCase
    from django.contrib.auth.models import User
    from rest_framework import status


    class AccountsTest(APITestCase):

        # 이 테스트는 user-create namespace를 가진 url로의 테스트이다.
        def setUp(self):
            self.text_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

            self.create_user = reverse('user-create')

        def test_create_user(self):
            data = {
                'username': 'foobar',
                'email': 'foobar@example.com',
                'password': 'somepassword'
            }

            # create_url로 json data를 post형식으로 보낸 후의 응답
            response = self.client.post(self.create_url, data, format='json')

            self.assertEqual(User.objects.count(), 2)
            self.assertEqual(reponse.status_code, status.HTTP_201_CREATED)

            self.assertEqual(response.data['username'], data['username'])
            self.assertEqual(response.data['email'], data['email'])
            # response.data에 'password'가 있으면 False 리턴해야한다.
            self.assertFalse('password' in response.data)
    ```

2. `python manager.py test api/users` 실행

- 해당 Reverse 를 찾을 수 없다고 나온다.

    ```shell
    NoReverseMatch: Reverse for 'user-create' with arguments '()' and keyword arguments '{}' not found. 0 pattern(s) tried: []
    ```

   - 왜냐하면 user-create라는 name의 url을 만들지 않았기 때문이다.

3. 그렇다면? 기본 view와 url을 만들어보자.
4. users/views.py 를 열고 다음을 추가하자.

    ```python
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import status
    from accounts.serializers import UserSerializer
    from django.contrib.auth.models import User

    class UserCreate(APIView):
        """
        creates the user.
        """

        def post(self, request, format='json'):
            return Response('hello')
    ```

5. users/urls.py를 만들고 다음을 추가하자.

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('users/', views.UserCreate.as_view(), name='user-create'),
    ]
    ```

6. settings/urls.py도 수정해주자.

    ```python
    from django.urls import include, path
    from django.contrib import admin

    urlpatterns = [
        ...,
        path('api/users/', include('accounts.urls')),
    ]
    ```

7. 다시 `python manager.py test api/users` 실행

    ```shell
    AssertionError: 1 != 2
    ```
    >해당 endpoint view에서 우리가 user를 만들어주지 않아서 발생하는 에러이다.
    >test 파일을 보면 setUp에서 유저를 하나 만들어놓았고
    >self.assertEqual(User.objects.count(), 2)에서 현재 유저 카운트가 2개인지 물어봤는데, 만드는 view가 없어서 아직 한개이다.

8. users/views.py의 UserCreate view를 변경하고 다시 테스트해보자!

- api/users/views.py 수정

    ```python
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import status
    from accounts.serializers import UserSerializer
    from django.contrib.auth.models import User

    class UserCreate(APIView):
        """ 
        Creates the user. 
        """

        def post(self, request, format='json'):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
    ```

- 다시 테스트! (`python manage.py test api/users`)

    ```shell
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.053s

    OK
    ```

<br />

## 다양한 에러 테스트

>지금까지는 valid한 입력만을 받는다고 가정한 것이다.<br />
>각 invalid input에 대해서는 아래와 같은 error를 가질 수 있다.<br />
> - Username
>   - Username already exists
>   - Username not provided
>   - Username to long
> - Password
>   - Password not provided
>   - Password too short
> - Email
>   - Email already taken
>   - Email not provided
>   - Invalid email format

### I. User Registration - Errors

1. password test 를 만들어보자

    ```python
    class AccountsTest(APITestCase):
    ...

        def test_create_user_with_short_password(self):
            """
            Ensure user is not created for password lengths less than 8.
            """
            data = {
                    'username': 'foobar',
                    'email': 'foobarbaz@example.com',
                    'password': 'foo'
            }

            response = self.client.post(self.create_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(len(response.data['password']), 1)

        def test_create_user_with_no_password(self):
            data = {
                    'username': 'foobar',
                    'email': 'foobarbaz@example.com',
                    'password': ''
            }

            response = self.client.post(self.create_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(len(response.data['password']), 1)
    ```

2. 테스트를 해보자

    ```shell
    AssertionError: Expected a `Response`, `HttpResponse` or `HttpStreamingResponse` to be returned from the view, but received a `<type 'NoneType'>`
    ```
    > 두둥...
    > invalid case일 경우 Response가 없다..!

3. UserCreate view를 수정하자

    ```python
    ...
    def post(self, request, format='json'):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ```

4. 테스트를 해보자

    ```shell
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.110s

    OK
    ```
    >성공!

5. 다른 테스트들도 추가하고 테스트해보자

    ```python
    ...
    class AccountsTest(APITestCase):
        ...

        def test_create_user_with_too_long_username(self):
            data = {
                'username': 'foo'*30,
                'email': 'foobarbaz@example.com',
                'password': 'foobar'
            }

            response = self.client.post(self.create_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(len(response.data['username']), 1)

        def test_create_user_with_no_username(self):
            data = {
                    'username': '',
                    'email': 'foobarbaz@example.com',
                    'password': 'foobar'
                    }

            response = self.client.post(self.create_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(len(response.data['username']), 1)

        def test_create_user_with_preexisting_username(self):
            data = {
                    'username': 'testuser',
                    'email': 'user@example.com',
                    'password': 'testuser'
                    }

            response = self.client.post(self.create_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(len(response.data['username']), 1)
    ```
- 테스트 결과

    ```shell
    ERROR: test_create_user_with_too_long_username (users.tests.AccountsTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "/Users/jngcii/jngciiCoding/hmc/api/users/tests.py", line 72, in test_create_user_with_too_long_username
        self.assertEqual(len(response.data['username']), 1)
    KeyError: 'username'
    ```
    > view의 is_valid에 걸려서 response에 'username', ... 데이터가 비어있다.

6. serializers 수정하고 다시 테스트!

    ```python
    # accounts/serializers.py
    ...
    username = serializers.CharField(
                max_length=32,
                validators=[UniqueValidator(queryset=User.objects.all())]
                )
    ...
    ```

- 테스트 결과
    ```shell
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.189s

    OK
    ```

7. 마지막으로 email test추가하고 테스트하자

    ```python
    ...
    class AccountsTestCase(APITestCase):
        ...

        def test_create_user_with_preexisting_email(self):
            data = {
                'username': 'testuser2',
                'email': 'test@example.com',
                'password': 'testuser'
            }

            response = self.client.post(self.create_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(len(response.data['email']), 1)

        def test_create_user_with_invalid_email(self):
            data = {
                'username': 'foobarbaz',
                'email':  'testing',
                'passsword': 'foobarbaz'
            }


            response = self.client.post(self.create_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(len(response.data['email']), 1)

        def test_create_user_with_no_email(self):
            data = {
                    'username' : 'foobar',
                    'email': '',
                    'password': 'foobarbaz'
            }

            response = self.client.post(self.create_url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(User.objects.count(), 1)
            self.assertEqual(len(response.data['email']), 1)
    ```

- 테스트 결과

    ```python
    .........
    ----------------------------------------------------------------------
    Ran 9 tests in 0.265s

    OK
    ```

### II. Token 발급받기

>token 기반 인증을 해보자!!

1. settings.py 에 몇몇 설정 추가하기

    ```python
    #config/settings.py
    ...

    INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    )

    ...

    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        )
    }
    ...
    ```

2. 만약 wsgi를 사용하면 authorization header를 허용해라!
3. test_create_user 메서드 수정하기

    ```python
    ...
    from rest_framework.authtoken.models import Token
    ...
    class AccountsTest(APITestCase):
        def test_create_user(self):
            """
            Ensure we can create a new user and a valid token is created with it.
            """
            data = {
                    'username': 'foobar',
                    'email': 'foobar@example.com',
                    'password': 'somepassword'
                    }

            response = self.client.post(self.create_url , data, format='json')
            user = User.objects.latest('id')
            ...
            token = Token.objects.get(user=user)
            self.assertEqual(response.data['token'], token.key)
    ```

4. UserCreate view 수정하고 테스트!

    ```python
    from rest_framework.authtoken.models import Token

    class UserCreate(APIView):
        """ 
        Creates the user. 
        """

        def post(self, request, format='json'):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                if user:
                    token = Token.objects.create(user=user)
                    json = serializer.data
                    json['token'] = token.key
                    return Response(json, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ```

- 테스트 결과
    ```shell
    ...
    ----------------------------------------------------------------------
    Ran 9 tests in 2.020s

    OK
    Destroying test database for alias 'default'...
    ```