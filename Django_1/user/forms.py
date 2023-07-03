# from django import forms
# user를 auth를 사용해서 개발했으니 폼도 auth에서 제공하는 form을 사용해야 합니다.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from .models import User
from django.contrib.auth import get_user_model  
#인증을 받아서 확장한 모델 불러옴. settings.py의  AUTH_USER_MODEL.

## auth를 확장된 모델을 가져오게 됩니다.
User = get_user_model()


class RegisterForm(UserCreationForm):
    
    class Meta():
        model = User
        # fields = ['email', 'name', 'password']
        # 필수부분만 자동으로 하기 때문에 email도 추가함
        fields = UserCreationForm.Meta.fields + ('email',)


class LoginForm(AuthenticationForm):
    
    class Meta():
        model = User
        # fields = ['email', 'password']
        # widget = {
        #     'email': forms.EmailField(attrs={'placeholder':'email'}),
        #     'password': forms.PasswordInput(attrs={'placeholder':'password'})
        # }