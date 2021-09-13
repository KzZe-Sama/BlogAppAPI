from django.contrib import admin
from .models import Blog,BlogCategory,Comment,Like
# Register your models here.

admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Comment)
admin.site.register(Like)