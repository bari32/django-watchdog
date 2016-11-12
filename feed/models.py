from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class post (models.Model):
    title = models.CharField(max_length =200)
    body = models.TextField()
    author = models.ForeignKey(User, related_name='feed_post')
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)
def __str__(self):
    return self.title
    