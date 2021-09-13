from django.urls import path,include
from .views import BlogViewUser,BlogView,BlogCategoryView,DeleteBlogAPIView,UpdateBlogAPIView,LikeAPIView,CommentAPIView
urlpatterns = [
    path('category',BlogCategoryView.as_view()),
    path('blogs',BlogView.as_view()),
    path('myblogs',BlogViewUser.as_view()),
    path('myblogs/update/<int:blog_id>',UpdateBlogAPIView.as_view()),
    path('myblogs/delete/<int:blog_id>',DeleteBlogAPIView.as_view()),
    path('myblogs/like/<int:blog_id>',LikeAPIView.as_view()),
    path('myblogs/comments/<int:blog_id>',CommentAPIView.as_view()),
]
