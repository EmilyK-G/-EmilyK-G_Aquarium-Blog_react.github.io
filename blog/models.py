from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    author = models.CharField(max_length=100) # models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_posted',]

 