from django.db import models
from django.contrib.auth.models import User

# Create your models here.

EVALUATION_CHOICES = [('良い', '良い'), ('悪い', '悪い')]

class ReviewModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='')
    useful_review = models.IntegerField(null = True, blank = True, default = 0)
    useful_review_record = models.TextField()
    evaluation = models.CharField(max_length=10, choices = EVALUATION_CHOICES) 

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_category')
    description1 = models.TextField()
    description2 = models.TextField()
    laugage = models.IntegerField(default=1)


class ImageModel(models.Model):
    image = models.ImageField(upload_to='')
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_image')
