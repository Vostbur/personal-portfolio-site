from datetime import date

from django.db import models


class Author(models.Model):
    avatar = models.ImageField(upload_to='static/img/avatars')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_at = models.DateField(default=date.today)
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=5000)

    def __str__(self):
        return self.title
