from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description1 = models.TextField()
    description2 = models.TextField()
    language = models.IntegerField(default=1)
    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class UserHome(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_home')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description1 = models.TextField()
    description2 = models.TextField()
    def __str__(self):
        return self.name