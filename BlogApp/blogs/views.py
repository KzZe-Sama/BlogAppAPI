import re
from .models import Blog,BlogCategory, Comment, Like
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import BlogCategorySerializer,BlogSerializer, CommentSerializer, LikeSerializer
from accounts.models import User
from rest_framework import status

class BlogCategoryView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAuthenticated]

    
class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]


class BlogViewUser(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self,user):
        return Blog.objects.filter(posted_by=user)

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset(request.user)
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['posted_by'] = User.objects.get(email=request.user).id
        print(request.FILES)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DeleteBlogAPIView(generics.DestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]
    
    def destroy(self, request, blog_id,*args, **kwargs):
        instance = Blog.objects.get(id=blog_id)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateBlogAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, blog_id):
        print(blog_id)
        instance = Blog.objects.get(id=blog_id)
        serializer = BlogSerializer(instance,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class LikeAPIView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class= LikeSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request,blog_id):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = Like.objects.filter(post_id=blog_id)
        serializer = LikeSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request,blog_id,*args, **kwargs):
        data = request.data
        data['post'] = blog_id
        data['liked_by'] = User.objects.get(email=request.user).id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class= CommentSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request,blog_id):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = Comment.objects.filter(post_id=blog_id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request,blog_id,*args, **kwargs):
        data = request.data
        data['post'] = blog_id
        data['posted_by'] = User.objects.get(email=request.user).id
        print(request.user)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)