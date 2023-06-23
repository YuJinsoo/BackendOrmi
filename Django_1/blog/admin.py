from django.contrib import admin
from .models import Post, Comment, HashTag # 작성한 models 임포트

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(HashTag)