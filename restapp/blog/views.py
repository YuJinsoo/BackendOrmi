from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views import View

# auth의 mixin 기능
from django.contrib.auth.mixins import LoginRequiredMixin

# django 예외
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from .models import Post, Comment, HashTag
from .forms import PostForm, CommentForm, HashTagForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializer, CommentSerializer, HashTagSerializer

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
            post = serializer.save(writer = request.user)
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Update(APIView):
    # 기존 값을 먼저 보내서 뿌려주고, 그걸 수정한값을 post로 받는 식.
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post) # 1개이기 때문에 many=True 는 안했음.
        return Response(serializer.data)
        
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Delete(APIView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        # if serializer.is_valid():
        #     post.delete()
        #     return Response(serializer.data, status=status.status_HTTP_204_NO_CONTENT)
        post.delete()
        return Response({'message': f'Post no.{pk} Deleted'}, status=status.status_HTTP_204_NO_CONTENT)


### Comment
class CommentWrite(APIView):
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(writer=request.user)
            comment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDelete(APIView):
    def post(self, request, pk): # comment_id
        
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        
        if serializer.is_valid():
            comment.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
    
### Hashtag
class HashTagWrite(APIView):
    def post(self, request, pk):
        serializer = HashTagSerializer(data=request.data)
        if serializer.is_valid():
            hashtag = serializer.save(writer=request.user)
            hashtag.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentDelete(APIView):
    def post(self, request, pk): # comment_id
        
        hashtag = HashTag.objects.get(pk=pk)
        serializer = HashTagSerializer(hashtag)
        
        if serializer.is_valid():
            hashtag.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)