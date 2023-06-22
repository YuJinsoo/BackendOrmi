from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView #generic view
from django.urls import reverse_lazy, reverse

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

### Post

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
        context = {
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
    return render(request, 'blog/post_form.html', {'form': form}) #생성한 form이 렌더링됨


# Django 자체의 뷰 기능도 강력, 편리 (generic View)
# model, template_name, context_object_name, 
# paginate_by (페이징처리), form_class, form_valid(), 
# django.views.generic -> ListView
class List(ListView):
    model = Post # 어떤 models의 테이블 사용할지 설정
    template_name = 'blog/post_list.html' # 템플릿 지정
    context_object_name = 'posts' # 템플릿으로 넘어갈때 변수이름

# CBV, django.views.generic -> CreateView
# get일때는 PostForm을 보고 form과 input을 렌더링하고, post일때는 그 form에서 요청을 전송한다.
class Write(CreateView):
    model = Post #모델
    form_class = PostForm # 폼
    # template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list') # 성공시 보내줄 url


class Detail(DetailView):
    model = Post #모델
    template_name = 'blog/post_detail.html'
    context_object_name = 'post' # render의 context로 넘겨줄 key 이름


#일반 View 로 Detail다시한번..
class DetailView(View):
    # 여기 들어오은 변수는 kwargs로 들어오기 때문에 url에서 설정한 변수 이름과 일치시켜줘야함
    def get(self, request, post_id):
        #db에서 값 가져오기
        # 해당 글 가져오기
        post = Post.objects.get(pk=post_id)
        # 이 글에 해당하는 댓글 가졍괴
        comments = Comment.objects.all()
        print(type(request))
        context = {
            'post' : post,
            'comments' : comments,
        }
        return render(request, 'blog/post_detail.html', context)

class Update(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content'] # Post 객체의 수정할 필드
    # success_url = reverse_lazy('blog:list')
    
    # initial 기능 : 업데이트시 form안에 초기값(원래 있던 값)을 템플릿에 전달하는 기능
    def get_initial(self) -> Dict[str, Any]:
        initial = super().get_initial() #UpdateView에서 제공하는 get_initial().리턴이 dictionary 형태
        post = self.get_object() # pk 기반으로 객체를 가져옵니다.
        initial['title'] = post.title
        initial['content'] = post.content
        return initial
    
    def get_success_url(self): 
        post = self.get_object()
        # 함수에서 사용하므로 reverse() 사용
        return reverse('blog:detail', kwargs={'pk': post.pk}) #reverse를 사용하면 url에 값을 전달해줄수있음
    
    # 이것도 많이 사용합니다.
    # def get_absolute_url(self):


class Delete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')

## generic view의 편한점은 post요청이 아니면 자동으로 화면이동(get)으로 처리해줌

### Comment
class CommentWrite(View):
    # def get(self, request):
    #     pass
    def post(self, request, post_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            # cleaned_data[field]로 가지고와야 폼에 있는 값이 정확하게 가져와집니다.
            # 폼이 유효하다면
            # 1. 사용자에게 댓글 내용을 받아옴
            # 2. 댓글을 달 게시물을 지정해줌
            # 이걸 왜하나? 댓글 객체를 생성하기 위해서
            content = form.cleaned_data['content']
            post = Post.objects.get(pk=post_id)
            # 댓글객체 생성. db에 접근해서 create()로 할 경우 .save()를 안해줘도 됩니다.
            # 크래스로 생성할 경우에는 생성된 instance에 .save()를 해줘야 합니다.
            comment = Comment.objects.create(post=post, content=content)
            return redirect('blog:detail', pk=post_id)
