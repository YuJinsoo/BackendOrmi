from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager # django의 인증기능이 적용된 모델
from django.utils import timezone

# Create your models here.

'''
Auth User Model
- 생성
- 삭제
- 수정
--> UserManager helper class 도움주는 클래스
'''

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('User must have an email')
        now = timezone.now() # 현재시간 -> UTC
        # now = timezone.localtime() # 현재 위치 시간으로 기록됨
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

    
class User(AbstractUser):
    # email 이 중복되면 안되는 옵션. unique
    # 한 테이블에 unique는 1개만 있을 수 있습니다.
    username = None # username으로 인한 오류 방지. email을 아이디로 쓸거라 그럼.
    email = models.EmailField(unique=True, max_length=255)
    
    # null과 blank 허용. 보통 둘다 사용함
    name = models.CharField(max_length=50, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateField(null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    
    # authenticate의 username kwargs 에 email이 들어갈 것이라는 걸 미리 알려줌
    # 유일한 값인 email 이므로 id처럼 쓸수있음
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    
    # USERNAME_FIELD로 지정한 column은 없어야함
    REQUIRED_FIELDS = [] #필수 요소 설정가능
    
    objects = UserManager()
    
    # def __str__(self):
    #     return self.name