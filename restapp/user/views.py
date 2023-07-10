# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.views import View # 뷰 임포트
# from django.contrib.auth import authenticate, login, logout

# # from .models import User ## from django.contrib.auth import get_user_model
# from .forms import RegisterForm, LoginForm

# # Create your views here.
# #user 관련된 기능

# #회원가입
# #로그인
# #로그아웃


# ### Registration
# class Registration(View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             return redirect('blog:list')
        
#         # 회원가입 페이지 - 정보를 입력할 form 보여주어야 합니다.
#         form = RegisterForm()
#         context = {
#             'form': form,
#             'title': 'User'
#         }
#         return render(request, 'user/user_register.html', context=context)
    
#     def post(self, request):
#         # form으로 입력된 정보 유효성을 확인하고, db에 저장한다.
        
#         # request의 post요청에 들어간 정보가 들어간걸 생성
#         form = RegisterForm(request.POST)
#         # print(form.is_valid())
#         # print(form.errors)
#         if form.is_valid(): # form의 유효성검사
#             user = form.save()
#             # 로그인 한다음 이동해도 됨
        
#         # return redirect('blog:list')
#         return redirect('user:login')


# class Login(View):
#     def get(self, request):
#         ## 추가
#         # 먼저 로그인이 되어 있는 경우 바로 return 해줌
#         # 유저 정보가 request에 있으면 로그인이 되어있는것
#         if request.user.is_authenticated:
#             return redirect('blog:list')
        
#         togo = None
        
#         if "next" in request.GET.keys() :
#             togo = "/"+"/".join(request.GET["next"].split("/")[1:4])
        
#         form = LoginForm()
#         context = {
#             'form':form,
#             'title': 'User',
#             'togo': togo
#         }
#         return render(request, 'user/user_login.html', context=context)
    
#     def post(self, request):
#         ## 추가
#         # 먼저 로그인이 되어 있는 경우 바로 return 해줌
#         # 유저 정보가 request에 있으면 로그인이 되어있는것
        
#         if request.user.is_authenticated:
#             return redirect('blog:list')
        
#         form = LoginForm(request, request.POST)
#         if form.is_valid():
#             # form안에 있는 값을 가져올때는 cleand_data[key]
#             email = form.cleaned_data['username'] # 폼에서는 username을 보내줌... why? 폼에서 widget으로 이름 바꿔줄 수 있음.
#             password = form.cleaned_data['password']
            
#             # authenticate를 사용하지 않는다면
#             # email(id)와 password를 비교해서 일치하는것과 일치하지 않는 것의 분기처리 해주어야 합니다.
            
#             # models.py에 USERNAME_FIELD, REQUIRED_FIELDS 설정필요
#             # 등록된 유저면 True, 없으면 False가 리턴됨
#             user = authenticate(username=email, password=password) # 아이디, 패스워드
            
#             if user:
#                 login(request, user)
                
#                 # print(form.cleaned_data['next']) # input에 next있지만 form으로는 검색안됨. form filed에 추가해도안됨
                
#                 if request.POST['next'] != "None":
#                     return redirect(request.POST['next'])
                
#                 return redirect('blog:list')
            
#             # 폼에 에러를 추가해줍니다.
#             form.add_error(None, '아이디가 없습니다.')
        
#         context = {
#             'form': form, ## 에러가 들어간 폼
#             'title': 'User',
#             'togo': None
#         }
#         return render(request, 'user/user_login.html', context=context)
    

# ### Logout
# class Logout(View):
    
#     # logout은 get일까 post일까?
#     def get(self, request):
#         # logout은 login이 되어있는 상태인 것이 전제입니다.
#         # 그래서 request 안에 유저 정보가 이미 있기 때문에 post로 유저 정보를 받아오지 않아도 됩니다.
#         # logout함수는 request에 있는 유저를 로그아웃 시킵니다.
        
#         if request.user.is_authenticated:
#             print('hello')
#             logout(request)
        
#         ## logout이 없다면 object로 로그인한 오브젝트를 받아와서 상태를 로그아웃으로 바꿔줘야 합니다.
#         return redirect('blog:list')
    
    
    

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer, UserSerializer

from .models import User, Profile
from .forms import RegisterForm, LoginForm

# Create your views here.
# user 관련된 기능
# 회원가입
# 로그인
# 로그아웃

### Registration
class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        # 회원가입 페이지
        # 정보를 입력할 폼을 보여주어야 한다.
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')


### Login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password) # True, False
            
            if user:
                login(request, user)
                return redirect('blog:list')
            
        form.add_error(None, '아이디가 없습니다.')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)


### Logout
class Logout(View):
    def get(self, request):
        serializer = UserSerializer(request.data.user)
        logout(request)
        # return redirect('blog:list')
        return Response(serializer.data)
    
    

### Profile
class ProfileWrite(APIView):
    # def get(self, request):
    #     pass
    
    def post(self, request):
        user = request.data.get('user')
        image = request.data.get('image')
        age = request.data.get('age')
        
        profile = Profile.objects.create(user=user, image=image, age=age)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

## TODO 과제
class ProfileUpdate(APIView):
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    

class ProfileDelete(APIView):
    # request 에 user를 사용할 수 있는 이유가 auth 때문?
    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)

        if serializer.is_valid():
            profile.delete()
            return Response(serializer.data, status=status.status_HTTP_204_NO_CONTENT)