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

> 기능정리 - model (데이터베이스) - URL - View 

- 데이터베이스를 먼저 하는 이유 : view에서 template를 만들어서 내보낼 때 model이 잘 안되어있으면 template가 계속 수정되어야 할수있음

- 장고는 관계형 데이터베이스를 사용해야 함.
- 관계형 데이터베이스 (RDBMS) - 테이블, 엑셀
- migrations에 저장된 데이터베이스 상태로 되돌릴 수 있다.( 장고의 강력한 장점 중 하나)
- python manage.py migrate (특정시점) : 특정시점의 데이터베이스로 이동함


## URL 설정하기
- url 설정에는 하트코딩 방법과 별칭 방법으로 나뉩니다.
- `path()`에 url pattern과 url mapping 으로 ulr를 설정해줍니다.

1. 하드코딩
- 하드코딩의 경우 일반적인 URL 형태로 작성되기 때문에 직관적으로 표현할 수 있습니다.

- template에서 하드코딩은 일반적인 url작성 형식과 비슷합니다.

```html
{% for post in posts %} 
    <tr>
        <td><a href="/blog/detail/{{post.pk}}/">{{ post.title }}</a></td>
    </tr>
{% endfor %}
```

2. 별칭
- 개발 단계에서 URL을 리팩토링 하는 경우가 빈번하게 발생하는데, 별칭을 사용하면 URL 변경시 모든 파일을 찾아가며 수정해야 하는 일을 줄일 수 있습니다. 즉 **유지보수 측면에서 월등**합니다.

- 별칭을 사용하기 위해서는 urls.py파일에 앱 별칭(별칭 namespace)과 `urlpatterns` 요소마다 `name` 속성에 별칭으로 쓸 str를 할당하면 됩니다.

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

## View
- 요청에 따른 응답을 정리해두는 부분
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

-view를 표현하는 방법은 다양하게 준비되어있고, generic view 는 자주 사용하는 기능들을 편리하게 사용하도록 만들어 둔 기능입니다. 그래서 일반 View를 상속해서 사용하는 것 보다 생략된 부분이 많아 처음 사용하면 동작을 이해하기 어려운 경우가 있습니다.

- generic view를 제외하고, 요청을 처리하는 함수들의 첫 인자는 `request`로 지정합니다.


1. 함수형
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


2. 클래스형

- urls.py 에 매핑할 클래스를 정의합니다. urls.py에서는 클래스이름.as_view() 를 전달합니다.

- HTTP 메서드는 클래스의 메서드 이름으로 구분합니다.

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
    path("", index), ## 도메인 요청시 index 호출!
]
```

## generic View

- **Django** 에서 미리 구현해 놓은 간결하지만 강력한 View 클래스들입니다.

- `django.views.generic`에서 필요한 generic view를 import하면 됩니다.

```python
#generic view
from django.views.generic import ListView, CreateView, DetailView 
```


## template
- 전체 프로젝트에 영향이 가는걸 변경했으면 항상 setting 에 가서 적용해야합니다.
- 전체 템플릿에 추가할 것이므로 `settings.py`파일의 `TEMPLATES` 에 `DIRS`에 추가해줘야 합니다.
- 공용 template는 에러화면이나, html을 고정시킬때? 많이 사용합니다.

- 템플릿 태그 {%%} 사용해서 편리하게 개발할 수 있습니다.


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


## forms.py

- 폼 형태를 지정해서 Database에 값을 손쉽게 전달할 수 있게 만들어줍니다.
- 뷰 레이어(views.py) 에서 정의해둔 form의 인스턴스를 생성해서 입력에 대한 유효성 검사를 하기 위해 사용합니다.

- 일반 form 과 modelform이 있습니다.


1. 일반 form
  - HTML 에 있는 form 태그를 가리킵니다.

2. ModelForm
  - models.py에 정의한 클래스(DB테이블)을 이용해서 form을 정의합니다.

```python
# blog/forms.py
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

- views.py에서..

```python
# 뷰 단에서는 이렇게 사용합니다.

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

- templates 파일

```html
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