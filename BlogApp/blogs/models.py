from django.db import models
import datetime

from django.db.models.deletion import CASCADE
# Create your models here.
from accounts.models import User
class BlogCategory(models.Model):
    category_name = models.CharField(max_length=25)
class Blog(models.Model):
    category = models.ForeignKey(BlogCategory,on_delete=CASCADE)
    blog_title = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(default='default.jpg',auto_created=True)
    posted_on = models.DateTimeField(auto_created=True,default=datetime.datetime.now)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.blog_title} {self.posted_by}'


class Like(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} liked by {self.liked_by}'

class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    context = models.TextField()
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} liked by {self.posted_by}'