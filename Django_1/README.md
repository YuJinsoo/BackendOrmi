# Django

- Django의 특징
    1. ORM(Object-Relational Mapping): 데이터베이스와의 상호작용을 자동화하여 개발자가 SQL 쿼리를 작성할 필요없이 데이터를 편리하게 다룰 수 있습니다. -->  models.py에서 함
    2. Admin 페이지: 기본적인(CRUD, Create-Read-Update-Delete) 기능이 갖춰진 관리자 페이지를 자동으로 생성해줍니다.
    3. 보안: 취약점 테스트를 통해 안정성이 검증된 보안 기능을 제공합니다. --> 타 프레임워크보다 보안이 좋음
      - SQL 인젝션은 악의적인 SQL을 주입하여 공격하는 방법이다.
      - XSS는 자바스크립트를 삽입해 공격하는 방법이다.
      - CSRF는 위조된 요청을 보내는 공격 방법이다.
      - 클릭재킹은 사용자의 의도하지 않은 클릭을 유도하는 공격 방법이다.
    4. MTV 패턴: Model-Template-View 패턴을 가지고 있어, 기능들을 분리하여 개발할 수 있습니다.

- Django의 구성요소 (MTV패턴)
    1. **Model**: 데이터베이스와 상호작용을 하는 컴포넌트
    2. **Template**: 사용자에게 보여지는 HTML, CSS, JS 등
    3. **View**: HTTP 요청 처리 및 Model과 Template 연결

## Django의 구조

- 장고는 여러개의 `app`을 가질 수 있는 구조로 설계되어있습니다.

## Django 동작과정
1. WSGI Application 생성
2. settings에서 정의한 settings.MIDDLEWARE 로드
3. WSGI(uwsgi, gunicorn)에서 applcation call
4. WSGI environ(request data를 담은 딕셔너리)과 함께 WSGIRequest 인스턴스 생성
5. 미들웨어 체인에 WSGIRequest 인스턴스와 함께 call
6. 미들웨어를 모두 거쳐간 후 최종적으로 view에 request가 전달되어 개발자가 정의한 로직을 거친 후 최종적으로 Response 반환

- 출처: https://wookkl.tistory.com/60

- django.core.wsgi.py의 get_wsgi_application()는 WSGIHandler()가 반환됨
- 이때 setting.py에 정의한 미들웨어를 로드합니다.
WSGI가 해당 applicationd을 call 하면 __call__메서드가 실행됩니다.
(WSGIHandler는 django.core.handlers.wsgi 에 정의되어있습니다.)

- middleware_chain 메서드에 request 객체르 넘겨주고 stack 구조인 middleware는 순서에 따라 각각 처리된 수 responst가 반환됩니다.
- 미들웨어는 load_middleware(self, is_async=False) 함수에서 차례대로 로드됩니다.


## setting.py 설정

- Django 프로젝트를 생성하면 생기는 파일로 프로젝트에 관한 다양한 설정을 줄 수 있는 파일입니다.

- **SECRET_KEY** 
  - 내가 생성한 프로젝트가 유일함을 알려주는 키. 탈취되지 않도록 주의
- **DEBUG** 
  - 개발때는 True로 해서 에러를 알려주도록 함. 하지만 배포할때는 False로 해서 배포해야 함께
- **ALLOWED_HOSTS** ??

- **INSTALLED_APPS** 
  - 이 프로젝트에서 관리해줄 앱 목록. 내가 추가한 앱도 여기에 추가해줘야함.
  - 내가 만든 앱 추가!

- **ROOT_URLCONF** = "app.urls"
  - 이 사이트에 들어왔을 때 url root를 app.urls 라는 파일 (app: 생성한 프로젝트) 폴더의 urls 파일에서 찾을것이라는걸 알려주는것

- **DATABASES** = {}
  - 데이터베이스 세팅? 연결? 기본은 sqlite3으로 생성되게 설정되어있음

- 언어, 시간설정부분 처음에는 en-us, UTC로 되어있는데 한국엉로 바꿔줄수있음
  - **LANGUAGE_CODE** = "ko-kr" # 한국어
  - **TIME_ZONE** = "Asia/Seoul" # 한국시간
  - **USE_I18N** = True
  - **USE_TZ** = True

- **TEMPLATES**
  - `DIRS` key에 템플릿 경로설정을 할 수 있습니다.
  - `"DIRS": [BASE_DIR / "templates"], # Django_1/templates`


## 장고 개발 순서

> 기능정리 - model (데이터베이스) - URL - View / Form - template

- 데이터베이스를 먼저 하는 이유 : view에서 template를 만들어서 내보낼 때 model이 잘 안되어있으면 template가 계속 수정되어야 할수있음

- 장고는 관계형 데이터베이스를 사용해야 함.
- 관계형 데이터베이스 (RDBMS) - 테이블, 엑셀
- migrations에 저장된 데이터베이스 상태로 되돌릴 수 있다.( 장고의 강력한 장점 중 하나)
- python manage.py migrate (특정시점) : 특정시점의 데이터베이스로 이동함

> view.py를 수정하면 반드시 urls.py 와 템플릿 파일을 확인해줍니다!
> 변경되는 즉시 변경된 것을 적용해주어야 에러가 발생하지 않습니다.



## Model : orm으로 사용할 클래스를 정의하는 부분

- django에서 model.py 선언한 클래스는 db의 table 입니다.
- ORM은 django와 db를 연결해주는 기능을 합니다.
- DB에 직접 들어가지 않고도 db를 다룰 수 있습니다. (굉장한 장점)

- ORM으로 CRUD!
    - 생성 
    - 객체 = 클래스(값)으로 객체애 인스턴스 선언
    - 저장 객체.save()
    
    - 조회
    - 클래스.objects.all()
    - 클래스.objects.get(조건)
    
    - 수정
    - 조회로 한개의 객체 혹 여러개 객체를 가져옴
    - 값을 수정
    - 객체.save() 로 저장
    
    - 삭제
    - 삭제할 객체를 조회로 불러옴
    - 객체.delete()

- 서버사이드 렌더링은 서버에 부하를 줄 수 있음
- 하지만 seo측면에서 이미 완성된 페이지 이기 때문에 유리하다 (검색노출)

- 파이썬에서 클래스로 테이블을 개발할 수 있습니다.
- django.db 의 models를 임포트하고, 각 클래스에 models.Model을 상속받아서 선언합니다.
- 필드 속성으로는 CharField, TextField, DateTimeField 등과 각 필드마다 옵션을 줄 수 있습니다.

```python
# hashtag 테이블 생성
from django.db import models

class HashTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
```

> models.py에 변경점이 있으면 db가 변경되었기 때문에 makemigrations > migrate를 해주어야 합니다.

### 테이블 상관관계 (모델 간의 관계) 개념 정리 필요

1. OneToN
 - 한쪽 테이블에서는 유일한 값(혹은 테이블 전체)가 다른 테이블에서 여러 번 들어갈 수 있는 관계
 - :eyes: post와 댓글 관계

2. OneToOne
 - 각 테이블 안에 서로 유일해야 하는 값을 공유하는 경우
 - :eyes: profile과 user의 관계

3. NtoN
 - to be continue...

### admin 화면에서 db 관리 - admin.py

- admin.py파일에 `models.py`에 정의한 클래스(테이블) 을 등록하면 `도메인/admin` url에서 테이블을 관리할 수 있습니다.
- admin 페이지에서 CRUD 모두 가능

```python
from django.contrib import admin
from .models import Post, Comment, HashTag # 작성한 models 임포트

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(HashTag)
```


## URL 설정하기 - urls.py
- url 설정에는 하트코딩 방법과 별칭 방법으로 나뉩니다.
- `path()`에 url pattern과 url mapping 으로 url를 설정해줍니다.

> url pattern 에 설정한 변수명은 매핑한 views.py의 함수/클래스 메서드 의 인자와 일치해야 에러가 발생하지 않습니다.
> 이 규칙은 템플릿에서 url태그 {% url '' 변수=값%} 를 사용할 때에도 변수에 url pattern에서 설정한 변수명으로 지정해야 동작합니다.
> :exclamation:요청에 대한 url은 urls.py에서부터 찾아가기 때문 + 여러개의 변수를 줄 경우에 구분해야 하기 때문으로 생각합니다.

1. 하드코딩
- 하드코딩의 경우 일반적인 URL 형태로 작성되기 때문에 직관적으로 표현할 수 있습니다.
- template에서 하드코딩은 일반적인 url작성 형식과 비슷합니다.

```html
<!-- 템플릿 내에서..  -->
{% for post in posts %} 
    <tr>
        <td><a href="/blog/detail/{{post.pk}}/">{{ post.title }}</a></td>
    </tr>
{% endfor %}
```

2. 별칭
- 개발 단계에서 URL을 리팩토링 하는 경우가 빈번하게 발생하는데, 별칭을 사용하면 URL 리팩토링시 모든 파일을 찾아가며 수정해야 하는 일을 줄일 수 있습니다. 즉 **유지보수 측면에서 월등**합니다.

- 별칭을 사용하기 위해서는 urls.py파일에 앱 별칭(별칭 namespace)과 `urlpatterns` 요소마다 `name` 속성에 별칭으로 쓸 str를 설정해줍니다.

```python
# blog.urls.py

## 생성한 app의 별칭을 지정합니다.
app_name = 'blog'

urlpatterns = [
    # 각 요청의 url path() 안에 name keyward에 별칭을 부여합니다.
    path("", views.List.as_view(), name='list'),
    path("detail/<int:pk>/", views.Detail.as_view(), name='detail'), #/blog/detail/1
    path("write/", views.Write.as_view(), name='write'),
]  

```

- 위와 같이 별칭 지정이 되면, `views.py`나 template에서 별칭으로 경로를 지정할 수 있습니다.
> `앱별칭:urls에서 설정한 각 url의 별칭`

```python
def write(request):
    if request.method == "POST":
        #form 확인
        form = PostForm(request.POST)
        if form.is_valid():
            post= form.save()
            return redirect('blog:list')  ## 경로 설정시 별칭 사용
        
    form = PostForm() 
    return render(request, 'blog/write.html', {'form': form})

# CBV, django.views.generic -> CreateView
class Write(CreateView):
    model = Post #모델
    form_class = PostForm # 폼
    success_url = reverse_lazy('blog:list') # 성공시 보내줄 url을 별칭으로 사용
```

- template 파일에서 별칭으로 사용하기 위해서는 템플릿태그 `{% url %}` 을 사용합니다.
- 지정한변수의 경우 urls.py 에서 `<int:변수>` 처럼 정의됩니다.

> "{% url '앱별칭:별칭' 지정한변수=값%}"
```html
{% for post in posts %} 
    <tr>
        <td><a href="{% url 'blog:detail' pk=post.pk %}">{{ post.title }}</a></td>
    </tr>
{% endfor %}
```

## View - view.py
- 요청에 따른 응답을 정리해두는 부분입니다.
- 웹 요청을 받는다
- 요청을 처리하고 데이터베이스에서 필요한 값이 있으면 가져온다.
- 가져온 값을 가공해서 응답 형태로 만들어준다.
- 응답을 반환한다.

1. FBV 함수 기반 뷰
2. CBV 클래스 기반 뷰

- 일반적으로 CBV방법을 더 많이 사용합니다.

- view에서 django.shorcuts import render 함수
- `render()`도 리턴값은 httpresponse 입니다. httpresponse와 다른 점은 html이나 데이터베이스 정보를 같이 넘겨줄 수 있음

- View 수정하면 urls.py, template 확인해야함

### View를 정의하는 방법

- Django에서 view를 표현하는 방법은 다양하게 준비되어있습니다(FBV, CBV).

- generic view 는 자주 사용하는 기능들을 편리하게 사용하도록 만들어 둔 기능입니다. 그래서 일반 View를 상속해서 사용하는 것 보다 생략된 부분이 많아 처음 사용하면 동작을 이해하기 어려운 경우가 있습니다.
- generic view를 제외하고, 요청을 처리하는 함수들의 첫 인자는 `request`로 지정합니다.


1. 함수형 Function Based View
- urls.py 에 매핑할 함수를 정의합니다. urls.py에서는 함수 이름만 전달합니다. () 는 생략

- HTTP 메서드는 인자로 전달받은 request를 통해 구분합니다.

```python
def index(request):
  if request.method == "GET":
    pass

  if request.method == "POST":
    pass
```

- return 되어야 하는 값은 `HttpResponse()`인데, `render()`, `redirect()`등의 메서드와 `HttpResponse()`메서드가 가능합니다.

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
```

- 예외적으로 반환값이 HttpResponse()는 아니지만 별칭을 통해 경로를 전달할 수 있는 `reverse()` 사용 가능합니다.


2. 클래스형 Class Based View

- urls.py 에 매핑할 클래스를 정의합니다. urls.py에서는 클래스이름.as_view() 를 전달합니다.

- HTTP 메서드는 클래스의 메서드 이름으로 구분합니다.

- return 값은 httpresponse를 리턴해줍니다.
- 그래서 화면을 보여주기 위해서는 `render()`를, 단지 보여줄 경로만 전달할 경우에는 `redirect()` 를 리턴해줍니다.

```python
from django.views import View

class Index(View):
    def get(self, request, *args, **kwargs):
        pass
    def post(self, request, **kwargs):
        pass
```

3. 클래스형 - genericView

- 매우 축약된 형태의 뷰 구현으로 다양한 클래스들이 개발되어 있습니다.

- 클래스에 미리 정해진 변수이름에 값을 설정하여 손쉽게 원하는 기능을 개발할 수 있습니다.

```python
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView #generic view

class PostList(ListView):
    model = Post
    ...
    pass
```


## 도메인 주소만 요청했을 때 index 페이지 보여주기

- 생성한 프로젝트 폴더에 `views.py`를 생성해서 index 요청 처리를 만들어준다.
```python
# app.views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

- 프로젝트 폴더의 `urls.py`에 urlpatterns에 추가
```python
# app.urls.py
from .views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("", index), ## 도메인 요청시 app.view.py 의 index() 호출!
]
```


## generic View

- **Django** 에서 미리 구현해 놓은 간결하지만 강력한 View 클래스들입니다.

- `django.views.generic`에서 필요한 generic view를 import하면 됩니다.

```python
#generic view
from django.views.generic import ListView, CreateView, DetailView 
```

---


## template
- 전체 프로젝트에 영향이 가는걸 변경했으면 항상 setting 에 가서 적용해야합니다.
- 전체 템플릿에 추가할 것이므로 `settings.py`파일의 `TEMPLATES` 에 `DIRS`에 추가해줘야 합니다.
- 공용 template는 에러화면이나, html을 고정시킬때? 많이 사용합니다.

- 템플릿 태그 {%%} 사용해서 편리하게 개발할 수 있습니다.

### 탬플릿 태그

- 항상 시작 태그와 닫는 태그로 이루어져있습니다. 
- 아닌 것도 있지만 그렇게 생각하는게 오류를 줄일 수 있습니다.

1. for 문
```html
{% for post in posts %}
...
{% endfor %}
```

2. 조건문
```html
{% if content %}
...
{% else %}
...
{% endif %}
```

3. url 태그
  - form이나 a 태그에 url를 설정하기 위한 태그
  - 별칭을 사용한 방법으로 편리하고 유지보수에 뛰어납니다.

```html
{% url 'app_name:name' var=value %}
```

4. 값
  - view에서 템플릿을 렌더링할 때 전달한 context 에서 지정한 key값들로 값을 사용할 수 있습니다.

```python
#views.py

def index(request):
  post = Post.objects.get(pk=1)
  context = {'post': post}
```

```html
<p>{{ post.content }}</p>
```

5. crsf 토큰.
  - form 태그 사용 시 django에서 인정한 요청임을 확인시켜주는 태그.
  - form 태그 사이에 넣어주어야 정상 동작합니다.
```html
<form ... >
  {% csrf_token %}
  ...
</form>
```

6. block 과 extends
  - 아래 절에서 자세히 설명합니다.
```html
{% extends 'base.html' %}
{% block content %}
  ...
{% endblock %}
```

7. 다른 템플릿을 현재 템플릿에 불러서 붙여넣기
  - 전달된 폼에 에러가 있을 경우, 에러를 출력하는 공간을 따로 부여하고, 표현할 템플릿을 따로 두어서 사용했습니다.
```html
{% include 'blog/form_error.html' %}
```


### 템플릿 태그 with

- 템플릿에서 context로 전달받은 변수를 다른 이름으로 변경해서 사용하고 싶을 때 쓰는 템플릿 태그입니다.

```html
<!-- context = {'post':post} -->

{% with new_post = post %}
    <!-- 이 구간에서 -->
    <!-- new_post 는 post와 동일합니다. -->
{% endwith %}
```

- 폼에 대한 에러를 처리할 때 `form_error.html`하나로 처리하는데, comment_form과 hashtag_form에 대한 에러를 한 번에 처리하기 위해서 `with`를 사용했습니다.

- `form_error.html`에서는 전달된 form 변수명이 `form`이므로 해당 파일을 include 하기 전에 form에다가 comment_form, hashtag_form을 with로 지정해주었습니다.

```html
<!-- post_detail.html -->
<h3>해시태그</h3>
    <form action="{% url 'blog:tag-write' post_id=post.pk%}" method="post">
        {% csrf_token %}
        {% if hashtag_form.errors %}
            {% with form=hashtag_form%}
            {% include 'blog/form_error.html' %}
            {% endwith %}
        {% else %}
            {{ hashtag_form.name }}
        {% endif %}
        
        <input type="submit" class="btn btn-dark" value="태그생성">
    </form>
```

```html
<!-- form_error.html -->
<div class="alert alert-danger">
    <ul>
        {% for errors in form.errors.values %}
            {% for error in errors %}
                <li>{{error}}</li>
            {% endfor %}
        {% endfor %}
    </ul>
    {{ form }}
</div>

```



### Django Template Engine의 변수 필터 활용

- 템플릿에서 변수 필터를 사용하려면 `{{ value|filter:parameter }}` 이와 같은 양식으로 사용합니다.
``` html
<!-- 필터 적용 -->
{{ value|filter }}

<!-- 여러 필터 적용 -->
{{ value|filter1|filter2 }}
```

- 템플릿 태그와 함께 사용할 경우에는 `{{ template_tag|filter:parameter }}` 이와 같이 사용할 수 있습니다.
- 필터에 매개변수를 전달하려면 `{{ value|filter:”parameter” }}` 이렇게 사용해야 합니다.
내장 필터 종류에는 upper, lower, length, default, join, slice 등이 있습니다.

- 예제
```html
<!--join -->
# ['a','b','c'] -> "a // b // c"
{{ value|join:" // " }}
```

```html
<!-- add -->
# value가 4면 6이 나옴
{{ value|add:"2" }}
# first가 [1,2,3] second가 [4,5,6] = [1,2,3,4,5,6]이 나옴
{{ first|add:second }}
```

```html
<!-- cut -->
# value = 'ab c d'
# 'ab c d' -> 'abcd'
{{ value|cur:" " }}
```

- 여러가지 필터 기능들이 있습니다. : 




### 탬플릿 파일을 쪼개서 개발하기

- {% block content %} / {% endblock %} 과 {% extends filename %} {% include filename %} 태그를 통해 템플릿 파일들을 조립하듯이 사용할 수 있습니다.

- 다른 템플릿이 들어갈 부분에 block 태그로 표시해줍니다.
```html
<!-- base.html -->
 <body>
    <div class="container">
      <h1>Blog</h1>
      {% block content %}
      {% endblock %}
    </div>

    <script ...> </script>
  </body>
```

- 해당 파일을 base.html의 block 태그에 끼워넣어진다고 생각하면 됩니다.
- 끼워넣을 파일을 {% extends 템플릿파일명 %}로 지엉하고, 전달될 내용부분을 block 태그로 감싸면 됩니다.

```html
<!-- post_edit.html -->
{% extends 'blog/base.html' %}

{% block content %}
<form method="post">
    {% csrf_token %}
    {{ form.title.label_tag }}
    <input type="text" name="{{ form.title.name }}" value="{{ form.initial.title }}">
    <br>
    {{ form.content.label_tag }}
    <textarea type="text" name="{{ form.content.name }}">{{ form.initial.content }}</textarea>
    <br>
    <input type="submit">
</form>
{% endblock %}
```

## 프로젝트 공용 template 만들기

- 여러 앱에서 공통으로 사용하는 부분 (예를 들어 헤더, 푸터, 게이트페이지) 등은 헷갈리지 않고 참조하기 쉽도록 프로젝트 템플릿을 만들어 둘 수 있습니다.

- 프로젝트폴더와 같은 경로에 `templates`라는 폴더를 생성하고, `settings.py`에 기본 템플릿 경로를 등록해줍니다. (app(프로젝트), blog, user 폴더와 함께 template 폴더가 있음)

- `TEMPLATES` 의 `DIRS`에 경로를 아래와 같이 설정해줍니다.
- 이렇게 설정하면 템플릿 파일에서 가장 베이스 경로로 설정됩니다.
```python
# setting.py
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"], # Django_1/templates
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

### 프로젝트 공용 template 파일 작성

- 공용 템플릿 파일을 작성하는데, title은 페이지를 렌더링할 때 context로 전달받아 입력할 수 있도록 구분해줍니다. (block을 사용해서)

- 로그인 상태일 때에는 로그아웃, 로그아웃 상태일 때에는 로그인 버튼이 보이도록 만들었습니다.

- 로그인 상태일 경우 어떤 유저가 로그인했는지 확인할 수 있도록 id(email)를 표시했습니다.
```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="ko-KR">
  <head>
    ...
    <title>
        {% block title %}
            {{ title }}
        {% endblock %}
    </title>
  </head>
  <body>
    <div class="container">
      {% if user.is_authenticated %}
      <p>Welcome, {{ user.email }}</p>
      <a href="{% url 'user:logout' %}" class="btn btn-primary">Logout</a>
      {% else %}
      <p>Please, Login</p>
      <a href="{% url 'user:login' %}" class="btn btn-primary">Login</a>
      {% endif %}
      <h1>Blog</h1>
      {% block content %}
      {% endblock %}
    </div>

    ...
  </body>
</html>
```

### 프로젝트 공용 템플릿 파일 사용하기

- `blog` 앱의 게시물들을 확인하는 `post_list.html`를 확인해보겠습니다.
- extends를 아무런 베이스 경로 없이 `base.html`로 불러와서 상속할 수 있게 되었습니다. (다른 앱에 있는 템플릿을 쓸 때에는 `앱이름/파일`로 사용해야 합니다.)

```html
<!-- post_list.html -->
{% extends 'base.html' %}

{% block content %}
<p>블로그 게시판 첫 화면입니다.</p>
```

- 또한 blog 의 views.py 에 title을 넘겨주는 부분을 추가해야 합니다.
- 왜냐하면 `base.html`의 title 부분은 정해지지 않고, 전달받아서 렌더링하기 때문입니다.

```python
## blog/view.py
class Index(View):
    def get(self, request):
        post_objs = Post.objects.all()
        context = {
            "posts": post_objs,
            'title': 'Blog' ## title에 들어갈 값을 text로 전달해줍니다.
        }
        return render(request, 'blog/post_list.html', context)
```


---


## forms.py

- 폼 형태를 지정해서 Database에 값을 손쉽게 전달할 수 있게 만들어줍니다.
- 뷰 레이어(views.py) 에서 정의해둔 form의 인스턴스를 생성해서 입력에 대한 유효성 검사를 하기 위해 사용합니다.

- 일반 form 과 modelform이 있습니다.

1. 일반 form
  - HTML 에 있는 form 태그를 가리킵니다.

2. ModelForm
  - models.py에 정의한 클래스(DB테이블)을 이용해서 form을 정의합니다.
  - 템플릿에 form을 직접 생성할 필요 없습니다.

```python
# blog/forms.py ## db에 연동할 form 형태 정의
from django import forms
from .models import Post, Comment

## 장고의 form을 사용하는 것은 사용자 입력에 대한 유효성 검사를 위해 사용합니다.
## 유효성 검사를 하는 이유는 sql injection, 데이터베이스와 일치하는 데이터인지 검사
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        
```

- views.py에서 정의한 폼의 인스턴스를 활용하여 유효성 검사(`.is_valid()`)
- 렌더링에 필요해 폼을 전달할 때에는 dictionary 형태로 전달합니다. (context에 넣어서 context로 전달해도 됩니다.)

```python
# view.py 뷰 단에서는 이렇게 사용합니다.

def write(request):
    if request.method == "POST":
        form = PostForm(request.POST) #form 확인
        if form.is_valid(): #form 유효성 확인
            post= form.save()
            return redirect('blog:list')
        
    form = PostForm() # 폼 생성
    ## 렌더링할 템플릿에 Dictionary로 form을 전달함
    return render(request, 'blog/post_form.html', {'form': form}) #생성한 form이 렌더링됨
```

- templates 파일 에서는 값 태그로 태그를 그릴 수 있습니다.
- 폼.as_p 뿐만 아니라 테이블, div 등 다양하게 표현이 가능하며, form에서 정의한 fields 값만 표현할 수도 있습니다. (ex_ form.title)

```html
<!-- templates 파일 -->
{% extends 'blog/base.html' %}
{% block content %}
<p>블로그 글 작성 화면</p>
<form action="{% url 'blog:write' %}" method="post">
  <!-- django 에서 보안 때문에 form을 막아둠 -->
  <!-- csrf_token을 추가하면 허락하 요청이라는 뜻. 승인해줌 -->
  {% csrf_token %}
  <!-- form의 요소를 각각 p tag로 쓰겠다-->
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock %}

```

### 생성한 폼에 에러 추가 add_error() : forms.py

- 데이터를 입력받기 위해 views.py에 생성한 폼을 전달하고 is_valid() 함수로 유효성을 검사합니다.

- 그런데 form이 유효하지 않은 경우에 어떤 에러가 발생했는지 표시를 해주기 위한 기능이 있습니다.

- 그것은 바로 add_error()라는 함수입니다.

> form.add_error('field name', 'error 내용') 으로 작성합니다.

- add_error로 추가된 에러 내용은 template에서 form을 출력하면 표기됩니다.
- 또한 field를 지정하지 않으려면 None으로 하면 됩니다.
- field는 전달할 db table의 column이름 중 하나입니다.
- 예를들어 댓글(comment) 이라면 post_id, content, writer 가 필드로 들어갈 수 있습니다.

```python

class CommentWrite(View):
    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        form = CommentForm(request.POST)
        hform = HashTagForm()
        
        if form.is_valid():
            ...
            return redirect('blog:detail', post_id=post_id)
        
        # 유효하지 않다면 여기로 나와서 add_error를 수행함
        form.add_error(None,'폼이 유효하지 않습니다.')
        context = {
            'title': 'Blog',
            ...
        }
        return render(request, 'blog/post_detail.html', context=context)

```





## backend - frontend 통신 : API

- 프론트와 백엔드도 서로 통신을 합니다.
- 통신 방법을 API라고 합니다.

- 지금까지 배운 Django처럼 서버사이드 렌더링을 할 때에는 프론트쪽에서 템플릿을 수정하면 됩니다. 하지만, 서버의 규모가 커지면 서버에서 직접 렌더링해서 보내주는게 서버의 컴퓨팅 리소스, 개발 리소스 면에서 부담으로 작용할 수 있습니다..

- API로 통신 해서 프론트 쪽에 데이터를 전달하면 프론트 쪽에서 보여주는 작업을 수행합니다.
- 데이터는 서버에서 클라이언트에게 JSON 으로 값을 보내주고, 프론트는 그 JSON 데이터를 브라우저 화면에 보여줍니다.

- 이런 API를 제공하는 서버를 설계하는 프레임워크 : Django REST Framework

---

# user app

- 사용자에 대한 정보를 취급하는 `user` 앱을 개발할 것입니다.

## 유저 기능 만들기 준비

- 전체 사용할 user를 user 앱에다가 선언했는데, 프로젝트 전체에서 user를 사용하기 싶다면 프로젝트의 `settings.py`의 import 바로 아래에 아래와 같이 추가해주어야 합니다.

```python
# app.settings.py
from pathlib import Path

# Auth user 
# user 앱의 User 모델
AUTH_USER_MODEL = 'user.User'
```

> migrate or makemigrations ... 에러날떄
  - https://blue-coding-story.tistory.com/177
  - settings.py에 위에처럼 (AUTH_USER_MODEL = 'user.User') 등록 했는데도 에러나면

  1. migrations폴더에 __init__.py 를 제외한 모든 파일 삭제
  2. venv의 db.sqlite3 파일 삭제
  3. makemigrations > migrate 다시해보기

createsuperuser
myadmin
myadmin@aaaaa.com
1234


## 회원가입 기능 만들기

- 먼저 기능을 개발 할 때는 아래 단계를 꼭 기억하기 바랍니다.

> 구현기능분석 - model - view / url - templates


### 유저 테이블 생성하기 : models.py

- `AbstractUser` 클래스를 사용해 인증기능이 개발되어있는 클래스로 개발합니다.
- email을 아이디처럼 사용할 것이기 때문에 `unique = True` 옵션을 주었습니다.

- USERNAME_FIELD : 로그인시 form에서 전송할 username에 대한 값을 email로 넘겨줄 것이라고 명시
- REQUITRED_FIELD: 필수요소 설정. USERNAME_FIELD로 된 변수는 제외해야 합니다.

```python
# user.models.py
from django.db import models
from django.contrib.auth.models import AbstractUser # django의 인증기능이 적용된 모델

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)
    registered_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email' #인증시 username으로 들어갈 column 설정
    REQUIRED_FIELDS = [] #필수 요소 설정가능
    
    def __str__(self):
        return self.name
```

- models.py에 변경사항이 있으면 반드시 db에 반영해주어야 합니다.

> python manage.py makemigrations
> python manage.py migrate

### 유저 뷰 : view.py

- 회원가입, 로그인, 로그아웃에 대한 처리를 구현합니다.
- 각 기능에서 get, post가 필요한지 고민하고 구현합니다.

1. 회원가입
  - 회원가입 페이지를 보여주는 것과 유저 정보가 db에 저장되는것이 필요하므로 get과 post 둘다 필요합니다.
  - 회원정보 입력할 form 생성해서 view에서 보여주고 유효성검사합니다.

2. 로그인
  - 로그인 화면을 보여주는 것과 입력한 id, pw를 전달해야 하므로 get과 post 둘다 필요합니다.
  - email, pw를 입력할 form 필요합니다.

3. 로그아웃
  - 아직 제대로 구현되지 않았습니다.
  

```python
# View를 사용할것이므로 
from django.views import View #일반 뷰 임포트
from .models import User

class Registration(View):
  ...

class Login(View):
  ...

class Logout(View):
  ...
  
```

### 로그인 기능

- 아래 함수들을 이용해서 차례대로 계정인증, 로그인, 로그아웃 기능을 쉽게 구현할 수 있습니다.

```python
from django.contrib.auth import authenticate, login, logout
```

- authenticate()
- 입력된 email(id), password가 DB에 존재하고 일치하는지 인증하는 함수입니다.

```python
## view.py 로그인 post 처리

# models.py에 USERNAME_FIELD, REQUIRED_FIELDS 설정필요
# 등록된 유저면 True, 없으면 False가 리턴됨
user = authenticate(username=email, password=password)

if user:
    login(request, user)
    return redirect('blog:list')

# 폼에 에러를 추가해줍니다.
form.add_error(None, '아이디가 없습니다.')
```

- django auth 로그인은 세션을 통해서 로그인을 유지시켜줍니다. >> http_cookie_session.md 에 정리
- 세션으로 로그인이 되어있어서 로그인 확인 처리를 안하면 로그인 화면에 들어갔을 때 이미 있는 아이디라고 오류가 났다고 이해해주세요.
- 로그인이 되어있을 경우 return을 해주는 코드를 추가해주어야 합니다.

```python
## views.py 로그인 기능 시 로그인이 이미 되어있는 상태일 경우 바로 redirect
if request.user.is_authenticated:
    return redirect('blog:list')
```

## 경로설정 : urls.py

- path함수를 이용해서 패턴, 매핑 해줍니다.

---

# user 기능추가로 blog 변경

- blog의 DB에 작성자 column 에는 user가 들어가도록 수정했습니다.

## Update를 뷰로

- update는 작성 페이지에 빈 form이 출력되는 것이 아니라 기존에 작성된 값이 들어있어야 합니다.
- 왜냐하면 수정되어야지 모두 다시 작성하는것은 '수정'요청에 맞지 않기 때문입니다.

- 또한 Update는 수정 페이지를 불러오고, 수정된 내용을 저장해야 하기 때문에 `get`과 `post` 둘다 필요합니다.

- form의 초기값은 DB Post에서 해당 post를 받아와서 해당 내용을 작성한 폼(PostForm()) 의 `initial` 키워드 변수에 dictionary로 전달해주면 됩니다.

```python
class Update(View):
    def get(self, request, pk): # pk = post_id 상세페이지에서 넘어가기 때문에 pk 있음
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'content':post.content})
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context=context)
        
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', post_id=pk)
        
        form.add_error(None, '폼이 유효하지 않습니다.')
        context ={
            'form':form
        }
        return render(request, 'blog/form_error.html', context=context)
```

### form 활용
- form을 전달하는 경우에 실패 시에 어떤 에러가 났는지 알려주어야 합니다.
- `redirect`는 단순히 url만 전송하기 때문에 어떤 에러가 발생했는지 알 수 없습니다.
- 전달한 `form`에 `add_error`로 에러 내용을 추가한 뒤 `render`를 활용해서 context에 넣어 전달합니다.

```python
def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        if form.is_valid():
            ## 성공
        
        ## form 이 유효하지 않으면...
        form.add_error(None, '폼이 유효하지 않습니다.')
        context ={
            'form':form
        }
        return render(request, 'blog/form_error.html', context=context)
```

- 그 이후에 전달받은 template에는 전달받은 내용을 출력하는 부분을 작성해줍니다.

```html
<!-- form에 에러 내용이 있으면 에러 표현하는 템플릿에 넣어서 표현 -->
{% if form.errors %}
    {% include 'blog/form_error.html' %}
{% else %}
 ...

{% endif %}
```


---

# auth 기능

- `from django.contib.auth ` 로 시작하는 기능들입니다.
- 장고에서 제공하는 기본 인증 시스템입니다. 로그인, 회원가입, 로그아웃 등의 기능을 사용할 때 유용하게 활용할 수 있는 미리 개발된 기능입니다.

```python
# django의 인증기능이 적용된 모델
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.utils import timezone # django의 시간확인 유틸모듈
```

- auth 기능에 `User`클래스를 바로 사용해도 되지만 유연성이 부족합니다. 그래서 `AbstractUser`를 보통 사용합니다.

## Auth 활용한 User 개발 : models.py

- `AbstractUser` 는 인증기능을 사용해 사용자를 쉽게 모델링 하기 위한 클래스 입니다.

  > 기본적인 User Model. AbstractUser에 필수여부 O인것들은 미리 선언되어있습니다.
  >  칼럼명 -	설명 - 	필수여부 -	데이터타입
  > 1	id	PK	O	int
  > 2	username	이름(전체)	O	char
  > 3	first_name	성	X	char
  > 4	last_name	이름	X	char
  > 5	email	이메일	X	char
  > 6	password	암호화된 비밀번호	O	char
  > 7	is_staff	admin접속 가능 여부	O	bool
  > 8	is_activate	계정 활성 여부	O	bool
  > 9	is_superuser	모든 권한 활성 여부	O	bool
  > 10	last_login	마지막으로 로그인한 시간	O	datetime
  > 11	date_joined	계정이 생성된 날짜	O	datetime

- `BaseUserManager`는 `AbstractUser`를 상속한 클래스로 유저를 생성, 삭제, 수정 등의 동작을 할 때 도움을 주는 헬퍼 클래스입니다.

- AbstractUser에 사용하라고 미리 할당된 변수들이 있는데 보통 id는 `username`으로 사용합니다.
- 우리 프로젝트에서는 email 주소를 아이디로 사용하고 싶었습니다. 그렇기 때문에 `email` 멤버를 username처럼 사용하기 위해 `BaseUserManager`를 상속한 클래스를 생성해 메서드를 오버라이드합니다.

```python
# BaseUserManager에는 아래 주석처럼 함수가 2개 있는데 둘 다 오버라이드 해서 재정의해줍니다.
class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('User must have an email')
        now = timezone.now() ## 현재 시간을 편리하게 확인해서 넣어줄 수 있습니다.
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_active = True,
            is_superuser = is_superuser,
            last_login = now,
            date_joined = now
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
        
    # BaseUserManger함수 1 : create_user
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)
    
    # BaseUserManger함수 2 : create_superuser
    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

```

- `User` 모델에 USERNAME_FIELD, EMAIL_FIELD, REQUIRED_FIELDS 를 설정하고, 변경한 `BaseUserManager`를 object로 적용합니다.
- 그리고 우리 프로젝트에서 username은 사용하지 않을 것이기 때문에 `username = None`으로 설정해 주어야 username이라는 column이 생성되지 않습니다.

> `username`이 생성되어버리면 로그인 폼(AuthenticationForm 을 상속한) 에서 유저를 확인할 때 `username`을 우선적으로 확인합니다.
> 그런데 회원가입을 할 때 이메일만 등록하고 `username`은 없는 상태이기 때문에 로그인이 되지 않습니다.

```python
# model
class User(AbstractUser):
    username = None # username으로 인한 오류 방지. email을 아이디로 쓸거라 그럼.
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=50, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateField(null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    
    # authenticate의 username kwargs 에 email이 들어갈 것이라는 걸 미리 알려줌
    # 유일한 값인 email 이므로 id처럼 쓸수있음
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # BaseUserManager를 오버라이드한 클래스UserManager를 설정해줍니다.
    objects = UserManager()

```

### 다른 앱에서도 auth 적용한 유저를 사용하기

- settings.py에 아래와 같이 경로를 등록해주어야 합니다.
- `user` 앱에 `User` 모델을 다른 앱에서 사용하도록 등록한 것입니다.

```python
# settings.py
AUTH_USER_MODEL = 'user.User'
```

- User 모델을 사용할 곳에 아래와 같이 import하고, User를 사용하면 됨

```python
# blog.models.py
from django.contrib.auth import get_user_model

## auth를 확장된 모델을 가져오게 됩니다.
User = get_user_model()
```

## Auth 활용한 Form 개발 : forms.py

- Auth 기능을 활용한 객체를 form을 통해 입력/확인하고 싶을때 Auth의 form을 사용해야 합니다.

- 아래 모듈을 임포트해서 사용합니다.
- 회원가입과 로그인 동작에 대한 폼이 필요하니까 각각 `UserCreationForm`, `AuthenticationForm`이 필요합니다.
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
```

- 또한 외부에서 User를 사용하도록 설정한 것을 불러올때는 아래와 같이 불러올 수 있습니다.
```python
#인증을 받아서 확장한 모델 불러옴. settings.py의  AUTH_USER_MODEL.
from django.contrib.auth import get_user_model  

## auth를 확장된 모델을 가져오게 됩니다.
User = get_user_model()
```

- `UserCreationForm`, `AuthenticationForm`를 상속해서 Form을 만들어줍니다.
- `AbstractUser`에서 필수인 부분을 자동으로 전달하므로 fields를 설정할 필요가 없습니다. 다만 아이디로 사용하려고 했던 `email`은 필수가 아니기 때문에 아래와 같이 추가해주어야 합니다.

```python
# user.forms.py
class RegisterForm(UserCreationForm):
    
    class Meta():
        model = User
        # 필수부분만 자동으로 하기 때문에 email도 추가함
        fields = UserCreationForm.Meta.fields + ('email',)

class LoginForm(AuthenticationForm):
    
    class Meta():
        model = User

```

- 하지만, 진행한 프로젝트에서는 아이디인 `username`이 없고 대신 `eamil`을 사용합니다.
- 그런데 `UserCreationForm`을 상속하면 기본적으로 `username`이 생성되기 때문에 사용할 필드를 직접 지정해주어야 합니다.

```python
# user.forms.py
class RegisterForm(UserCreationForm):
    
    class Meta():
        model = User
        # 필수부분만 자동으로 하기 때문에 email도 추가함
        # fields = UserCreationForm.Meta.fields + ('email',)
        # UserCreationForm, AuthenticationForm에는 username을 사용해버리기 때문에 fields를 지정
        fields = ['email']

class LoginForm(AuthenticationForm):
    
    class Meta():
        model = User
        fields = ['email', 'password']

```


## User가 필요한 모델에 User column 추가하기
```python
## blog.models.py
from django.contrib.auth import get_user_model

## auth를 확장된 모델을 가져오게 됩니다.
User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # User와 Post는 1:N 관계이므로 ForeignKey를 사용합니다.
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
```



## Auth 기능의 Mixin을 활용 :  Views.py

- 다중 상속
- mixin은 추가 기능이 필요한 클래스에 상속해서 유연성 있게 사용하는 것입니다.
- 보일러 플레이트(변화없이 여러 군데에서 반복되는 코드)를 줄일 수 있습니다.

- 다른객체가 가진 기능을 내가 사용하는 객체에 사용하게 하려면 상속을 해야 합니다.


### Mixin이란
- django에서 미리 정의된 클래스
- 인증, 권한, 폼 등 하나의 부가 기능들을 추가로 사용할 수 있게 제공
  - LoginRequiredMix: 인증(로그인), 인증되지 않은 경우 로그인 페이지로 리디렉션
  - PermissionRequiredMixin: 권한, 사용자에게 필요 권한이 없으면 엑세스 거부 (HTTP 403 Forbidden)
  - UserPassesTestMixin: 사용자가 특정 조건을 통과할 수 잇는지 테스트
  - FormMixin: 폼 처리 기능 >> 나중에 정리
  - genericView: TemplateView, DetailView, CreateView, UpdateView, DeleteView ...


### LoginRequiredMixin

- 글쓰기 기능은 글(Post)에 작성자(writer)가 반드시 들어가야 하므로 로그인이 되어있는 상태에서 접근이 가능해야 합니다.
- 그러한 기능을 제공하기 위해 미리 제공된 클래스 `LoginRequiredMixin` 를 Write에 상속해서 사용하면 자동으로 로그인된 상태가 아니면 동작이 안되도록 만들어줍니다.

```python
# auth의 mixin 기능
from django.contrib.auth.mixins import LoginRequiredMixin

class Write(LoginRequiredMixin, View):
    # Mixin : LoginREquiredMixin
    def get(self, request):
        ...
    
    def post(self, request):
        ...

```

- `LoginRequiredMixin`을 통과하지 못하면 `settings.py` 안에 있는 `LOGIN_URL` 경로로 사용자를 보내줍니다. 
- 이 부분은 아직 `settings.py`에 해당 상수를 설정하지 않았기 때문에 설정이 안 된 상태입니다.
- 만약 다른 경로로 보내주고 싶으면 `LoginRequiredMixin` 을 상속한 클래스 안에서 `redirect_filed_name`을 설정해줘서 다른 경로로 보내줄 수 있습니다.

- views.py에 설정하는 방법

```python
# blog.view.py

class Write(LoginRequiredMixin, View):
    # Mixin : LoginRequiredMixin -> 로그인 되어있지 않은 사용자는 로그인페이지로 보내줌
    login_url ='/user/login' # 개별적으로 입력.
    
    def get(self, request):
        ...
        pass
    
    def post(self, request):
        ...
        pass
```

- settings.py에 설정하는 방법
```python
# settings.py
# Login URL
LOGIN_URL = '/user/login'
```

- 만약 `LoginRequiredMixin`를 통과하지 못했을 때 다음 경로를 다른 경로로 지정해주고 싶을 때는 해당 클래스로 접근하는 동작이 일어나는 화면 속 GET 요청의 render 부분에서 아래와 같이 작성합니다.

- 

```html
<input type=hidden name=“next” value=“{{ request.get_full_path }}”>
```

- 이런식으로 input에서 next 같은 이름으로 보내줄 경로를 입력해주면 다음 POST 요청에서 해당 값을 이용해서(next_url 키워드) 원하는 경로로 보내줄 수 있습니다.

---


# request
- views.py에는 클라이언트에서 요청한 http형식 request가 전달됩니다.
- 그래서 FBV든 CBV든 함수의 인자에 `request`가 필수로 들어갑니다.
  - view에서 받는 class와 함수에는 항상 request (http객체)르 반드시 받음.

- request에는 여러가지 정보가 담겨있는데 대표적으로 http요청을 보낸 유저가 누구인지 정보가 담겨있습니다.

```python
## 게시물을 작성하는 write요청의 request를 출력해보았습니다.
def post(self, request):
        print("request", request)
        print("request", dir(request))
        print("request.user", request.user)
        print("request.body", request.body)
        print("request.environ", request.environ)
        print("request.FILES", request.FILES)
        print("request.method", request.method)
        print("request.content_type", request.content_type)
```

```python
## 출력
request <WSGIRequest: POST '/blog/write/'>
request ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_body', '_cached_user', '_current_scheme_host', '_encoding', '_files', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_post', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']
request.user admin@email.com
request.body b'csrfmiddlewaretoken=rg9uS3tId5kgjjCFQarmAITz3McDhHrpQKaGaGFvL3a1Qjlp34fedvhOe7KT6ulZ&title=t4&content=c4'
request.environ {'ACLOCAL_PATH': 'C:\\Program Files\\Git\\mingw64\\share\\aclocal;C:\\Program Files\\Git\\usr\\share\\aclocal', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\ABO\\AppData\\Roaming', 'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\LOCAL\\crashpad_13876_XDMTBRITEMGBUYZN', 'COLORTERM': 'truecolor', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 
'DESKTOP-C8VM12G', ... }
request.FILES <MultiValueDict: {}>
request.method POST
request.content_type application/x-www-form-urlencoded
```

## request.user

- 요청을 보낸 유저 정보를 가지고 있습니다.

- 비 로그인시 : request.user > Anonymous User
- 로그인시 : request.user > id

- django auth
  - login(request, user) -> 여기 인자의 user는 auth.models.User
  - logout(request) -> 
  - authenticate(request, username, password)

- request.user.is_authenticated : True, False. 로그인 여부
- request.user type `<class 'django.utils.functional.SimpleLazyObject'>`

## request에서 알아야 하는 것.

- `FILES`, `GET`, `POST`

TODO - get_full_path 공부하기
- `get_full_path`


### POST

- 아래와 같이 post로 보낸 csrf토큰값, 폼에서 input으로 받은 name과 value를 key:value로 가지고 있습니다.

```python
<QueryDict: {'csrfmiddlewaretoken': ['PeTb3GWNutfBXUcgCcRxf9xtCcKiOCTA6oyskB4R3hVRF84mNsEqA652TVCo6pUY'], 'content': ['aaaa'], 'index': ['2']}>
```

---

## Server - Session, Cookie
- 서버의 상태 유지를 위한 두 가지 도구 입니다.

- 공통점
  - 목적: 데이터 저장 -> 사용자와 서버 사이에 원활한 통신을 위해

- Session : 서버 쪽에 저장 => 보안이 필요한 정보
- Cookie : 클라이언트 쪽에 저장 (브라우저) => 사라져도 괜찮은 정보 (가지고 있으면 편한)

- HTTP통신의 특징
  - Stateless : 요청 -> 응답 하면 끝 ==> 편리하게 상태를 유지하기위해 session, cookie를 사용합니다.

- ex) 서버를 껐다 켰을 때 로그인되어있음 --> 장고에서 기본으로 설정한 세션을 사용하기 때문에 세션id가 꼐속 유지되서 그럼

- 만료 조건이나 기간을 설정해서 브라우저를 닫거나 하루동안만 유지된다던가 하는식으로 개발할 수 있습니다.


### 세션 동작
- 세션은 서버에 있고
- 쿠키안에 세션ID(서버에서 발급해준)를 넣어줌

- 클라이언트는 http 헤더에 쿠키를 같이 넣어서 요청을 보냄
- 서버에서는 요청을 보고 헤더에서 쿠키를 확인. 서버에서 발급한 세션 ID가 있는지 - 확인해서 로그인 되어있는지 확인할 수 있음


## 보완하기 위한 기술 localstorage
- 브라우저의 localstorage 는 cookie를 보완하기 위해 나온 것. 
통신에 사용되지는 않지만 값을 저장해두고 싶을 때 사용하는 기능

## 그 이외에..

- JWT, OAuth를 사용할 때에는 다른 모듈을 설치해서 INSTALLED_APPS에 넣어주면 됨.

??궁금?? 서버에서 세션의 동작이 궁금합니다. 세션이 생성되고 사라지는 조건, 서버에서 어떻게 활용되는지, 어떤 데이터를 가지고있는지

## Server - Cache

- 목적: 데이터 저장 -> 사용자와 서버 사이에 원활한 통신을 위해

- Cache(저장소): 자주 사용되는(용량이 큰, 자주 바뀌지 않는) 데이터를 미리 불러와서 저장해놓는 곳

- CSS, JS, image 파일들 -> 브라우저 안에 캐시 저장소 or 캐시 서버



---

# Django ORM

- ORM은 Object Related Model 로, DB에 전달할 쿼리를 프레임워크에서 지원하는 것을 의미합니다.
- Django에서 DB에 따로 접근할 필요 없이 python 언어로 DB에 쿼리를 요청할 수 있습니다.
- SQL을 파이썬 문법으로 사용 가능하게 도와주는 기능들만


## QuerySet 이란?

- 장고에서 DB로 보낸 요청의 응답.

- 쿼리함수는 SQL 구문으로 바뀜 
- Django QuerySet   >>   SQL 구문
- get, all                SELECT
- create, bulk_create     INSERT
- update, ...save         UPDATE
- delete                  DELETE


## select query

- class.objects.all() : 데이터의모든 데이터 조회 -> `<Query Set []>`
- class.objects.get() : 하나의 행(row)만 조회 -> `<Object: 'result'>`
- class.objects.filter() : 해당 조건에 맞는 데이터만 조회  -> `<Query Set []>`
- class.objects.exclude() : 해당 조건을 제외한 데이터만 조회 -> `<Query Set []>`
- class.objects.count() : 해당 조건을 가진 데이터 개수 -> `int`
- class.objects.exists() : 조건에 해당하는 데이터 유무 -> `boolean`.
 HashTag.objects.filter(post=post).exists() # 이렇게 사용 가능
 
- class.objects.values() : 테이블의 값을 리스트 속 딕셔너리로 반환 ->`<QuerySet [{'key':'value'}]>`
- class.objects.values_list() : 테이블의 값을 리스트 속 튜플로 반환 -> `<QuerySet [(), ()]>`
- class.objects.order_by() : 특정 필드를 기준으로 정렬. 조건에 (-필드명:내림차순) (필드명:오름차순) ->`<Query Set []>`
- class.objects.fist(), last() : 쿼리셋 결과 중 가장 첫 번째, 마지막 결과 -> `<Object: 'result'>`
- class.objects.aggregate() : 집계함수 적용 시 사용(GROUP BY). 조건에 집계함수를 넣어줌 -> `<Query Set []>`
 User.objects.aggregate(Avg('age'))

- class.objects.annotate() : 컬럼 별로 주석을 달아 집계 함수 적용시 사용(AS) -> `<Query Set []>`
  - Post.objects.annotate(title=F("post__comment").value('title'))
  - F(): ORM을 사용할 때, 파이썬 메모리 효율을 위해 사용하는 메서드입니다.
    foreignkey로 연결된 것을 접근할 때 __ 로 접근할 수 있습니다.
    데이터베이스에서 두 테이블을 연결하는 쿼리 동작 후 결과만 전달받음. (파이썬에서 join할필요없음)


- Chaining : 쿼리함수 이어서 사용 가능
  Post.objects.filter(writer=user).count()
- Slicing : 쿼리셋은 list이므로 python 에서 슬라이싱이 가능합니다.
  Post.objects.all()[:3]


- filter, exclude 필터에 조건주기
  - __startswith : 특정 문자로 시작
  - __endwith : 특정 문자로 끝남
  - __contains : 특정 문자로 포함(대소문자 구분)
  - __icontains : 특정 문자로 포함(대소문자 구분X)
  - __gt : 특정 값보다 큼
  - __lt : 특정 갑보다 작음
  - __in : 특정 문자가 있는지
  - __isnull : 널인지?
  - __year : 특정 년도
  - __month : 특정 월
  - __day : 특정 일
  - __date : 특정 날짜(YY-MM-DD)
  
  - ex) User.objects.filter(date_joined__year="2023")
   date_joined 컬럼의 year가 2023인거 찾기. 이렇게 컬럼 뒤에 조건추가할수있습니다.


- filter()
  - 논리연산자 사용해서 조건 여러개
    - AND
      Comment.objects.filter(post=post)&Comment.objects.filter(writer=writer)
    - OR
      Comment.objects.filter(post=post)|Comment.objects.filter(writer=writer)
    - NOT
      !(Comment.objects.filter(post=post))
  - Q() 조건문 (import해줘야함)
    - AND
      Comment.objects.filter(Q(post=post)&Q(writer=writer))
    - OR
      Comment.objects.filter(Q(post=post)|Q(writer=writer))
    - NOT
      Comment.objects.filter(!Q(post=post))
      Comment.objects.filter(Q(post!=post))
  

- get()은 조건에 일치하는 객체가 없으면 오류가 발생합니다.
  - `get_object_or_404(Class, 조건)` 사용
- filter는 조건에 맞는 객체들이 없어도 오류가 발생하지 않습니다.
  - 빈 쿼리셋이 리턴됨


## Insert쿼리
- 객체(row) 혹은 객체들을 생성하는 쿼리

- 하나의 객체 생성
  - Class.objects.create() : 
  - Post.objects.create(title=...)

- 여러개의 객체 생성. 클래스로 객체
  - Class.objects.bulk_create([]) :  생성해서 괄호 안에 넣어줘야함
  - Post.objects.bulk_create([Post(title='t1', writer='w1',content='c1'), Post(...), ...])

- 조건에 맞는 데이터가 있으면 get 없으면 create
  - Class.objects.get_or_create(): 
  - Post.objects.get_or_create(title='t1', writer='w1', content='c1')

### Insert 쿼리 사용시 주의!
- 생성시 unique column과 같은 값이 있으면 에러가 발생합니다.
- create시 unique가 중복될 때, 필드가 비었을 때(null=True가 아닌 column), 외래키 관련 데이터베이스 오류 >> 에러발생

- 그래서 get_or_create() 사용합니다.
  - get_or_create() -> 2가지 리턴값
    comment, created = Comment.objects.get_or_create(post=post, content=content, writer=writer)
    이미 있어서 get으로 가져오게 되면 comment에 가져온 row가 들어가고, 생성이 되면 comment에 생성한 row가 들어간다.
    create : 생성이 되면 True, get 했으면 False

```python
# 이런식으로 사용할 수 있음. id가 unique.이고 생성한다면 defaults의 값을 넣어서 생성해줍니다.
obj, created = Person.objects.get_or_create(
    id='John',
    defaults={'birthday': date(1940, 10, 9)},
)
```

  - 예시로 회원가입할때 아이디가 겹치서 오브젝트가 받아지면 다른아이디 해달라고 알림주고 없으면 생성되는 식으로 짜면 될듯.
            

## Update 쿼리  
  - 업데이트할 객체를 변수에 저장해서 각 필드에 접근
    post = Post.object.get(pk=pk) # row객체를 불러옴
    post.title='new title' # 값 변경은 내 코드 안에서만...
    post.save() # 이 시점에 데이터베이스에 반영됨
  - 업데이트할 객체에 직접 접근  
    Post.objects.get(pk=pk).update(content='new content') # 바로 업데이트가 됨


## Delete 쿼리
  - 변수에 저장해서 삭제. 저장할 필요 없음
    
    ```python
    post = Post.objects.get(pk=pk)
    post.delete()
     혹은
    post = Post.objects.get(pk=pk).delete()
    ```

  - Delete 실무 구현
    - delete는 바로 삭제가 되어버리기 때문에 실무에서는 살짝 다르게 사용합니다.
    - User: removed_user(flag) -> boolean 0,1
      유저에 삭제유저 column을 추가하고, 해당 column의 row값이 0이면 현재유저, 1이면 삭제된 유저로 사용이 안되도록 함.
      휴면계정, 삭제계정 이런걸.. django에서는 AbstractUser 에 is_activate 가 있음



- 쿼리 고도화(JOIN)
단일 쿼리 -> 관계가 있는 데이터를 가지고 온다.
데이터베이스에 갔다올 때 최소한으로 갔다오는게 효율적. 그렇기 때문에 단일 쿼리를 날릴 수 있는 JOIN을 사용하는게 좋은데
그것은 아래 두 개로 사용할 수 있습니다.

  - select_related( JOIN ) : DB상에서 join을 한 후에 가져옴 (F()메서드처럼)
    쿼리를 날리는 횟수가 적습니다. 하지만 적다고 효율적인 것은 아닙니다.
    
  - prefetch_related( JOIN ) : join할 대상을 DB에서 가지고 온 후 join 해줌. 
    메모리에 각 테이블을 저장해두기 때문에 자주 사용하는 테이블들은 이게 더 효율적일 수 잇음.
    
    위 함수는 쿼리 안에서 (정)참조, 역참조 두 가지 모두 표현이 가능합니다.


## 정참조 역참조

```python
# models.py
class Post
    title = ...
    content = ...
    writer = ...
    created_at = ...
    updated_at = ...


class Comment
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    content = ...
    created_at = ...
    writer = ...
```

- Comment에서 Post를 불러오는 것은 Comment의 column 에 post가 외래키로 지정되어있음. 또한 1:N 관계에서 N에서 1을 참조하는것 : 정참조
- Post에서 Comment를 불러오는 것은 아무런 키가 지정되어 있지 않음. 또한 1:N 관계에서 1에서 N을 참조하는 것 : 역참조

- Class.objects.select_relate('column')
- 클래스에 정의된 column이고 외래키로 지정되어 있는 경우에만 불러올 수 있습니다.

- 게시글(Post)에 달린 Comment를 불러오기 위해서는 역참조를 해야 하는데 두 가지 방법이 있습니다.
  1. [Class]_set 사용하기
    -  호출할 때 Post.[Class]_set.all()로 가능

  2. models.py에 `related_name` 설정하기
    - Comment의 Post에 `related_name`을 설정해줍니다.
    - 호출할 때 Post.related_name.all()로 가능
    - related_name을 설정하면 [classname]_set.all() 은 불가능합니다.
    - view 단에서는 post.post_comment.all(), 
    template에서 {{ post.post_comment.all }} 을 하면 해당 게시글에 달린 모든 댓글(comment) 오브젝트들을 지정할 수 있습니다.


- ForeignKey에 related_names를 무조건 지정할 필요는 없습니다.
- django의 syntax를 보면 _set 을 붙이는 경우가 더 많았고, 그에 따라 일종의 코드 규칙처럼 정해진 느낌도 있습니다. 
- 하지만 위 테이블 예시와 같이 특정 모델에서 서로 다른 두 컬럼(속성, 필드)이 같은 테이블(모델)를 참조하는 경우 는 필수로 써야합니다.

TODO 더 공부해야 함.
## Django ORM으로 JOIN
- 참조링크 : https://wave1994.tistory.com/70

- Select_related

OneToOne 관계 / OneToMany 관계에서 M(Many)이 사용할 수 있다.
또한 Sql 기능 중 하나인 join기능을 활용할 수 있게 도와주는 QuerySet이라 할 수 있는데
Sql Query 문의 Join 과 Foreign_key(OTO, OTM) 사용하여 정참조 할 시 DB에 접근하여 QuerySet을 가져올때 미리 related  objects 까지 불러오는 메서드이다.
비록 Query가 복잡해지지만 한번 DB에 접근하여 불러온 Data는 database 서버가 종료되기 전까지 Cache에 남아 있어
매 Query 마라 DB에 접근하지 않아도 된다
즉, Select_related를 사용함으로서 DB 접근 빈도를 줄여 자원 낭비를 줄일 수 있다. (불필요한 접근 및 부하) 

- Perfetch_related
Select_related 의 범위에서 더 나아가 ManyToMany 등 대부분 모든 관계에서 사용 할 수 있다.
OneToMany 관계에서 O(One)이 사용 할 수 있다.
Select_related와 마찬가지로 related objects를 함께 불러오는 메서드이다. 
동일하게 Cache에 남아있게 하여 DB에 불필요한 접근을 줄여준다.

- Select_related 와 Prefetch_related 차이

정참조, 역참조의 차이도 있지만 실제 Join 을 어디서 하냐의 차이가 있다. 
select_related 같은경우 DB에서 Join 을 한 채로 가져오고, 
prefetch 는 가져와서 Python 으로 Join 을 하게 된다. 
정말 간단하게는 Select는 DB에서 join 기능을 수행한 후 가져오므로 1 Query가 실행된다면
Prefetch는 python에서 join 기능을 수행하므로 불러올때 1 Query를 실행하고 불러온 후 1 Query를 한번더 실행한다.
즉, 가급적 Select_related를 사용하는것이 효율적이라 할 수 있겠다.

