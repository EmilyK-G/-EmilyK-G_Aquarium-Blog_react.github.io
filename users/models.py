from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    author = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
