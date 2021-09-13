from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Blog,BlogCategory,Like,Comment

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class BlogCategorySerializer(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'