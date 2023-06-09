from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_At = models.DateTimeField(default=datetime.now, blank=True)
    post_read = models.IntegerField()
    post_img = models.ImageField(upload_to="BlogPostImg")