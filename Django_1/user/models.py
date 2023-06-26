from django.db import models
from django.contrib.auth.models import AbstractUser # django의 인증기능이 적용된 모델

# Create your models here.
class User(AbstractUser):
    # email 이 중복되면 안되는 옵션. unique
    # 한 테이블에 unique는 1개만 있을 수 있습니다.
    email = models.EmailField(unique=True, max_length=255)
    
    # null과 blank 허용. 보통 둘다 사용함
    name = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)
    registered_date = models.DateTimeField(auto_now_add=True)
    
    # authenticate의 username kwargs 에 email이 들어갈 것이라는 걸 미리 알려줌
    # 유일한 값인 email 이므로 id처럼 쓸수있음
    USERNAME_FIELD = 'email'
    
    # USERNAME_FIELD로 지정한 column은 없어야함
    REQUIRED_FIELDS = [] #필수 요소 설정가능
    
    def __str__(self):
        return self.name