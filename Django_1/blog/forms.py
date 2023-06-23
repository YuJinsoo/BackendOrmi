# blog/forms.py
from django import forms
from .models import Post, Comment, HashTag

# Form : tuple
# 일반 form. html에 있는 form 태그

# Model Form :  list
# models를 사용하는 form

## 장고의 form을 사용하는 것은 사용자 입력에 대한 유효성 검사를 위해 사용합니다.
## 유효성 검사를 하는 이유는
## sql injection, 데이터베이스와 일치하는 데이터인지 검사
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':'2', 'cols':'40'})
        }


class HashTagForm(forms.ModelForm):
    
    class Meta:
        model = HashTag
        fields = ['name']