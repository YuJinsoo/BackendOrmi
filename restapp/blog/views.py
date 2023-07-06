from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views import View

# auth의 mixin 기능
from django.contrib.auth.mixins import LoginRequiredMixin

# django 예외
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from .models import Post, Comment, HashTag
# from .forms import PostForm, CommentForm, HashTagForm

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response, status

from .serializers import PostSerializer

# Create your views here.

### Post
class Index(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized_posts = PostSerializer(posts, many=True) # 직렬화
        return Response(serialized_posts.data)


class Write(APIView):
    # def get(self, request):
    #     # 게시글 작성 Form을 만들어서 보내줌.
    #     # 화면을 그려주지 않아도 되기 때문에 고려하지 않아도 됩니다.
    #     # restful 한 개발이면 프론트쪽은 개발이 되어있는 상태에서 데이터를 뿌려주는 것이므로
    #     pass
    
    def post(self, request):
        # request로 온 데이터를 역직렬화 해서 저장해야함
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            post = serializer.save(commit=False)
            post.writer = request.user
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
