from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#EVALUATION_CHOICES = [('良い', '良い'), ('悪い', '悪い')]

"""class ReviewModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='')
    useful_review = models.IntegerField(null = True, blank = True, default = 0)
    useful_review_record = models.TextField()
    evaluation = models.CharField(max_length=10, choices = EVALUATION_CHOICES) 
"""
# pretty picture や colorful pictureなどのカテゴリーテーブル
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description1 = models.TextField()
    description2 = models.TextField()
    language = models.IntegerField(default=1)
    def __str__(self):
        return self.categoryName

# 写真のモデル（テーブル）
class Image(models.Model):
    image = models.ImageField(upload_to='images')
    category = models.ManyToManyField(Category)
    imageName = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.imageName

# Homeの部分
class UserHome(models.Model):
    #name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_home')
    userHomeName = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description1 = models.TextField()
    description2 = models.TextField()
    def __str__(self):
        return self.userHomeName