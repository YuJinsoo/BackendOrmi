from django.urls import path
from . import views


urlpatterns = [
    # path(패턴, 매핑)
    # 패턴에 아무것도 빈 str이면 index페이지를 의미합니다.
    # path("", views.index) # FBV 방식
    # 글 조회
    # 글 작성
    # 글 수정
    # 글 삭제
    # 코멘트 작성
    # 코멘트 삭제
    
    # CBV 방식
    # path("", Index.as_view()), 
    ## 이렇게 하려면 # from blog.views import Index #해줘야함
    path("", views.Index.as_view()),
    
]
