from users.models import User
from django.db import models


# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_liked_by')
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='liked_blog')
    is_liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
