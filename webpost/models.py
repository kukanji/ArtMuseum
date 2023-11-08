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
class category(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description_top = models.TextField('description_top', null=False, default="", blank=True)
    description_bottom = models.TextField('description_bottom', null=False, default="", blank=True)
    language = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# 写真のモデル（テーブル）
class image(models.Model):
    image = models.ImageField(upload_to='images')
    category = models.ManyToManyField(category)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# Homeの部分
class user_home(models.Model):
    #name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_home')
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description_top = models.TextField('description_top', null=False, default="", blank=True)
    description_bottom = models.TextField('description_bottom', null=False, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name