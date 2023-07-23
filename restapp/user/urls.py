from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # user/
    # 회원가입
    path("register/", views.Registration.as_view(), name='register'),
    # 로그인
    path("login/", views.Login.as_view(), name='login'),
    # 로그아웃
    path("logout/", views.Logout.as_view(), name='logout'),
    # 프로필 정보 가져오기
    path("profile/", views.ProfileView.as_view(), name='pf-get'),
    # 프로필 생성
    path("profile/write/", views.ProfileWrite.as_view(), name='pf-write'),
    # 프로필 변경
    path("profile/update/", views.Logout.as_view(), name='pf-update'),
    # 프로필 삭제
    path("profile/delete/", views.Logout.as_view(), name='pf-delete'),
]
