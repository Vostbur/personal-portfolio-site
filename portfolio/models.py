from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='static/img/portfolio')

    def __str__(self):
        return self.name
