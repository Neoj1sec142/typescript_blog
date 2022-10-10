from django.db import models
from users.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(default='Needs description', blank=True, null=True)
    img_url = models.URLField(max_length=512, blank=True, null=True, default='https://www.demo.com/')
    date_created = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.title

