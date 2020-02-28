# Start Django Rest API Project

###### 2020.02.27

### I. Project 시작하기
- project 생성 준비 및 생성
    ```shell
    $ mkdir myproject
    $ cd myproject
    $ pipenv --three
    $ pipenv shell
    $ pipenv install django djangorestframework
    $ django-admin startproject myproject .
    ```

### II. 기본 Set up
- wsgi.py, settings.py 등이 있는 myproject folder명을 config로 바꿔주고, manage.py, settings.py, wsgi.py 등 속 myproject를 config로 변경해주기

### III. Database 설정
- django-environ, psycopg2-binary 설치하기
    ```shell
    $ pipenv install django-environ psycopg2-binary
    ```

- settings.py 수정
    ```python
    ...
    import environ

    env = environ.Env()
    ...

    ...
    DATABASES = {
        "default": env.db("DATABASE_URL", default="postgres:///hmc")
    }
    # DATABASES = {
    #     "default": {
    #         "ENGINE": "django.db.backends.postgresql",
    #         "NAME": "helpmycode",
    #         "USER": "root",
    #         "PASSWORD": os.environ.get("POSTGRES_PW"),
    #         "HOST": os.environ.get("POSTGRES_HOST"),
    #         "PORT": "5432"
    #     }
    # }
    ...
    ```