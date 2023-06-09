from django.db import models

from django.contrib.auth import get_user_model

## auth를 확장된 모델을 가져오게 됩니다.
User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    # 생성될 때 자동으로 날짜를 저장함.
    created_at = models.DateTimeField(auto_now_add=True)
    # 생성, 수정, 저장될 때의 날짜/시간을 저장함
    updated_at = models.DateTimeField(auto_now=True)
    
    # def __str__(self):
    #     return f'{self.pk}.{self.title}'


class Comment(models.Model):
    # 변수 명을 post로 주면 table에서 column이 post_id로 생성됨
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content


class HashTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name