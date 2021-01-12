from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    author = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=512)
    content = models.TextField()

    def __str__(self):
        return self.author.username + ": " + self.title
