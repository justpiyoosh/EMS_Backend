from django.db import models

from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    content = models.TextField()
