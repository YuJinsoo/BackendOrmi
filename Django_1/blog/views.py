from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView #generic view
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.

## 함수형
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index page GET')
#     # 나머지 요청
#     # 에러, 예외처리
#     return HttpResponse('No!!!')

## 클래스형
class Index(View):
    def get(self, request):
        # return HttpResponse('Indext page GET class')
        
        # 데이터베이스에 접근해서 값을 가져와야 합니다.
        # 게시판에 글들을 보여줘야 하기 때문에 데이터베이스에서 "값 조회"
        # MyModel.objects.all()
        post_objs = Post.objects.all()
        # context = DB에서 가져온 값
        context ={
            "posts": post_objs,
        }
        # print(post_objs) # Query_Set<1 ,2, 3, 4, 5>
        return render(request, 'blog/board.html', context)
    

# write
# post - form
# 글 작성 화면 및 글 작성 요청 FBV
def write(request):
    if request.method == "POST":
        #form 확인
        form = PostForm(request.POST)
        if form.is_valid():
            post= form.save()
            # 값 전달 없이 url만 바뀔 때 redirect 씀
            # return redirect('/blog')
            return redirect('blog:list')
        
    form = PostForm() # 빈 폼 생성
    return render(request, 'blog/write.html', {'form': form})


# Django 자체의 클래스 뷰 기능도 강력, 편리
# model, template_name, context_object_name, 
# paginate_by (페이징처리), form_class, form_valid(), 
# django.views.generic -> ListView
class List(ListView):
    model = Post # 어떤 models의 테이블 사용할지 설정
    template_name = 'blog/post_list.html' # 템플릿 지정
    context_object_name = 'posts' # 템플릿으로 넘어갈때 변수이름

# CBV, django.views.generic -> CreateView
class Write(CreateView):
    model = Post #모델
    form_class = PostForm # 폼
    success_url = reverse_lazy('blog:list') # 성공시 보내줄 url


class Detail(DetailView):
    model = Post #모델
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    