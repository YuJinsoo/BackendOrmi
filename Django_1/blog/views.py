from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView #generic view
from django.urls import reverse_lazy, reverse

# auth의 mixin 기능
from django.contrib.auth.mixins import LoginRequiredMixin

# django 예외
from django.core.exceptions import ValidationError, ObjectDoesNotExist


from .models import Post, Comment, HashTag
from .forms import PostForm, CommentForm, HashTagForm

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
        # MyModel.objects.all() SELECT * form post
        posts = Post.objects.all()
        ## post의 역참조 comment를 related_name으로 해봄.
        # for p in posts:
        #     ## related_name을 해주지 않으면 [클래스이름_set].all() 해야함
        #     comments = p.post_comment.all()
        #     print(p)
        #     print(comments)
        #     for c in comments:
        #         print(c)
                
        # context = DB에서 가져온 값
        context = {
            "posts": posts,
            'title': 'Blog'
        }
        # print(post_objs) # QuerySet<[post 1 ,2, 3, 4, 5]>
        return render(request, 'blog/post_list.html', context)


## 로그인시 리스트를 보여줄 때, 로그인한 계정의 글만 가져오는 방법
class IndexLogin(LoginRequiredMixin, View):
    def get(self, request):
        # Post-User연결(ForeignKey)
        # User를 이용해서 Poast를 가지고 온다.
        posts = Post.objects.filter(writer=request.user)
        context = {
            "posts": posts,
            'title': 'Blog'
        }
        return render(request, 'blog/post_list.html', context=context)



# # write
# # post - form
# # 글 작성 화면 및 글 작성 요청 FBV
# def write(request):
#     if request.method == "POST":
#         #form 확인
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post= form.save()
#             # 값 전달 없이 url만 바뀔 때 redirect 씀
#             # return redirect('/blog')
#             return redirect('blog:list')
        
#     form = PostForm() # 폼 생성
#     return render(request, 'blog/post_form.html', {'form': form}) #생성한 form이 렌더링됨


# Django 자체의 뷰 기능도 강력, 편리 (generic View)
# model, template_name, context_object_name, 
# paginate_by (페이징처리), form_class, form_valid(), 
# django.views.generic -> ListView
# class List(ListView):
#     model = Post # 어떤 models의 테이블 사용할지 설정
#     template_name = 'blog/post_list.html' # 템플릿 지정
#     context_object_name = 'posts' # 템플릿으로 넘어갈때 변수이름

# CBV, django.views.generic -> CreateView
# get일때는 PostForm을 보고 form과 input을 렌더링하고, post일때는 그 form에서 요청을 전송한다.
# class Write(CreateView):
#     model = Post #모델
#     form_class = PostForm # 폼
#     # template_name = 'blog/post_form.html'
#     success_url = reverse_lazy('blog:list') # 성공시 보내줄 url


# 이 클래스 동작 전제가 login이 되어있어야 동작하게 됩니다.
# 로그인 하지 않았으면 동작하지 않습니다.
class Write(LoginRequiredMixin, View):
    # Mixin : LoginRequiredMixin -> 로그인 되어있지 않은 사용자는 로그인페이지로 보내줌
    # login_url ='/user/login' 개별적으로 입력. settings.py에 LOGIN_URL 설정가능 
    # redirect_field_name = 'name' #로그인 페이지 말고 다른데로 보내주고 싶을때
    
    def get(self, request):
        form = PostForm()
        context = {
            'form': form,
            'title': 'Blog'
        }
        return render(request, 'blog/post_form.html', context=context)
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            # 가져온 내용을 객체로 저장하는데, (commit=False) 으로 할당만 하고 수정 가능한 상태
            post = form.save(commit=False) 
            post.writer = request.user
            post.save()
            return redirect('blog:list')
        
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form,
            'title': 'Blog'
        }
        return render(request, 'blog/post_form.html', context=context)


# class Detail(DetailView):
#     model = Post #모델
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post' # render의 context로 넘겨줄 key 이름

#일반 View 로 Detail다시한번..
class DetailView(View):
    # 여기 들어오은 변수는 kwargs로 들어오기 때문에 url에서 설정한 변수 이름과 일치시켜줘야함
    def get(self, request, post_id):
        #db에서 값 가져오기
        # 해당 글 가져오기
        # post = Post.objects.get(pk=post_id)
        # # 이 글에 해당하는 댓글 가져오기
        # comments = Comment.objects.filter(post=post)
        # # comment 생성할 Form
        # comment_form = CommentForm()
        # # 해쉬태그
        # hashtags = HashTag.objects.filter(post=post)
        # # 해쉬태그 Form
        # hashtag_form = HashTagForm()
        
        ## select_related. join 사용해보기
        post = Post.objects.get(pk=post_id)
        # comments = Comment.objects.select_related('writer').filter(post=post)
        ## post를 직접 불러오지 않아도 id만 알아도 불러올 수 있음.
        # comments = Comment.objects.select_related('writer').filter(post__pk=post_id)
        comments = Comment.objects.select_related('post').filter(post__pk=post_id)
        # comments = Comment.objects.select_related('post').first()
        
        # hashtags = HashTag.objects.select_related('writer').filter(post=post)
        # hashtags = HashTag.objects.select_related('writer').filter(post__pk=post_id)
        hashtags = HashTag.objects.select_related('post').filter(post__pk=post_id)
        
        comment_form = CommentForm()
        hashtag_form = HashTagForm()
        
        # print(post)
        # print(comments)
        # print(hashtags)
        # print(len(comments))
        # print(comments[0])
        # print(comments[0].writer.email)
        # print(comments[0].post.writer)
        # for com in comments:
        #     print(com)
        # print(comments[-1].post) # QuerySet은 이거는 안됨 
        
        context ={
            'post': post,
            'comments': comments,
            'hashtags': hashtags,
            'comment_form': comment_form,
            'hashtag_form': hashtag_form,
            'title': 'Blog'
        }
        # 수업... 에러
        # context = {
        #     'post_id' : post_id,
        #     'post_title' : comments[0].post.title,
        #     'post_content' : comments[0].post.content,
        #     'post_writer' : comments[0].post.writer,
        #     'post_created_at' : comments[0].post.created_at,
        #     'post_updated_at': comments[0].post.updated_at,
        #     'comments' : comments,
        #     'hashtags' : hashtags,
        #     'comment_form' : comment_form,
        #     'hashtag_form': hashtag_form,
        #     'title': 'Blog'
        # }

        # render에서 request를 같이 전달하기 때문에 template파일에서 request를 사용할 수 있음
        return render(request, 'blog/post_detail.html', context)


# class Update(UpdateView):
#     model = Post
#     template_name = 'blog/post_edit.html'
#     fields = ['title', 'content'] # Post 객체의 수정할 필드
#     # success_url = reverse_lazy('blog:list') # 포스트 요청에 대한 성공
    
#     # initial 기능 : 업데이트시 form안에 초기값(원래 있던 값)을 템플릿에 전달하는 기능
#     def get_initial(self) -> Dict[str, Any]:
#         initial = super().get_initial() #UpdateView에서 제공하는 get_initial().리턴이 dictionary 형태
#         post = self.get_object() # pk 기반으로 객체를 가져옵니다.
#         initial['title'] = post.title
#         initial['content'] = post.content
#         return initial
    
#     # post 요청 성공 시 수행할 메서드
#     def get_success_url(self): 
#         post = self.get_object()
#         # 함수에서 사용하므로 reverse() 사용
#         return reverse('blog:detail', kwargs={'pk': post.pk}) #reverse를 사용하면 url에 값을 전달해줄수있음
    
#     # 이것도 많이 사용합니다.
#     # def get_absolute_url(self):
class Update(View):
    def get(self, request, pk): # pk = post_id
        # get()은 조건에 해당하는 객체가 없으면 오류를 방생시킨다.
        post = Post.objects.get(pk=pk) # <Object: post>
        form = PostForm(initial={'title': post.title, 'content':post.content})
        context = {
            'form': form,
            'post': post,
            'title': 'Blog'
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
            'form':form,
            'title': 'Blog'
        }
        return render(request, 'blog/form_error.html', context=context)


# class Delete(DeleteView):
#     model = Post
#     success_url = reverse_lazy('blog:list')
## generic view의 편한점은 post요청이 아니면 자동으로 화면이동(get)으로 처리해줌
class Delete(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')
    
    # 클래스 자체에 아예 접근하지 못하게 하려면 -> LoginRequiredmixin
    # Login이 되었을 때 삭제 버튼이 보이게 (템플릿에서 처리)


### Comment
class CommentWrite(LoginRequiredMixin, View):
    # def get(self, request):
    #     pass
    
    ''' 고도화 할사람... 
    1. LoginRequiredMixin -> 삭제
    2. 비회원 유저 권한 User
    '''
    redirect_field_name = "next"
    
    def post(self, request, post_id):
        form = CommentForm(request.POST)
        hform = HashTagForm()
        
        # get 관련 쿼리들은 해당 데이터가 없을 때 오류 발생
        # get_or_404 를 사용하는걸 추천.
        post = Post.objects.get(pk=post_id)
        
        if form.is_valid():
            # cleaned_data[field]로 가지고와야 폼에 있는 값이 정확하게 가져와집니다.
            # 폼이 유효하다면
            # 1. 사용자에게 댓글 내용을 받아옴
            # 2. 댓글을 달 게시물을 지정해줌
            # 이걸 왜하나? 댓글 객체를 생성하기 위해서
            content = form.cleaned_data['content']
            
            # 유저 정보 가져오기
            writer = request.user
            
            try:
                # 댓글객체 생성. db에 접근해서 create()로 할 경우 .save()를 안해도 됨
                # 모델 클래스로 생성할 경우에는 생성된 instance에 .save()를 해줘야 함
                # 있는 값. unique 값이 중복이면 에러
                comment = Comment.objects.create(post=post, content=content, writer=writer)
                
            # 외래키 --> ObjectDoesNoeExist (post 없을 때)
            except ObjectDoesNotExist as e:
                print('Post does not exist.', str(e))
            
            # 필드가 비어있을 때 -> ValidationError
            except ValidationError as e:
                print('Validation failed.', str(e))

            return redirect('blog:detail', post_id=post_id)
        
        ## 첫번째 인자로 form의 필드를 지정할 수 있음. None 대신 'content'
        form.add_error('content','폼이 유효하지 않습니다.')
        context = {
            'title': 'Blog',
            'post': post,
            'comments' : post.post_comment.all(),
            'hashtags' : post.hashtag_set.all(),
            'comment_form': form,
            'hashtag_form': hform
        }
        return render(request, 'blog/post_detail.html', context=context)



class CommentDelete(View):
    def post(self, request, pk): # pk는 comment_id
        comment = Comment.objects.get(pk=pk)
        ## 상세 페이지로 돌아가기 위한 post id 접근 (삭제하기 전에 해야됨)
        post_id = comment.post.id
        # 코멘트 삭제
        comment.delete()
        return redirect('blog:detail', post_id=post_id)


### HashTag
class HashTagWrite(View):
    def post(self, request, post_id):
        #post
        post = Post.objects.get(pk=post_id)
        form = HashTagForm(request.POST)
        cform = CommentForm()
        
        if form.is_valid():
            name = form.cleaned_data['name']
            #작성자정보 가져오기
            writer = request.user
            hashtag = HashTag.objects.create(post=post, name=name, writer=writer)
            return redirect('blog:detail', post_id=post_id)
        
        form.add_error('name', '폼이 유효하지 않습니다.')
        context = {
            'title': 'Blog',
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': cform,
            'hashtag_form': form
        }
        return render(request, 'blog/post_detail.html', context=context)


class HashTagDelete(View):
    def post(self, request, tag_id):
        hashtag = HashTag.objects.get(pk=tag_id)
        post_id = hashtag.post.id # 태그가 달린 post를 찾아서 redirect
        hashtag.delete()
        return redirect('blog:detail', post_id=post_id)
