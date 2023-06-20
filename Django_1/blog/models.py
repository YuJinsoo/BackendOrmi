from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=10)
    # 생성될 때 자동으로 날짜를 저장함.
    created_at = models.DateTimeField(auto_now_add=True)
    # 생성, 수정, 저장될 때의 날짜/시간을 저장함
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content = models.TextField()
    writer = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)