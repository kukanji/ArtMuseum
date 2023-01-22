from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from ..models import ImageModel, CategoryModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

def listview(request, username):
    # ユーザーを取得
    user = User.objects.filter(username=username)
    # そのユーザーの画像を取得
    object_list = CategoryModel.objects.filter(author=user[0])
    return render(request, 'list.html', {'object_list': object_list})


def imagesview(request, pk):
    object = ImageModel.objects.get(pk = pk)
    username = object.author.username
    return render(request, 'images.html', {'object': object, 'username': username})

# 新しいカテゴリーを作成した後
class CreateCategory(CreateView): 
    template_name = 'create.html'
    model = CategoryModel
    fields = ('name', 'author_id', 'description1', 'description2', 'language')
    success_url = reverse_lazy('users.html')

class CreateImage(CreateView):
    template_name = 'create.html'
    model = ImageModel
    fields = ('image', 'category_id', 'author_id')
    success_url = reverse_lazy('images_list')



"""def evaluationview(request, pk):
    post = ReviewModel.objects.get(pk = pk)
    author_name = request.user.get_username() + str(request.user.id)
    if author_name in post.useful_review_record:
        return redirect('list')
    else:
        post.useful_review = post.useful_review + 1
        post.useful_review_record = post.useful_review_record + author_name
        post.save()
        return redirect('list')
"""