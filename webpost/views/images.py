from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from ..models import ImageModel, CategoryModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# トップページ
def top(request):
    return render(request, 'top.html')

# ユーザーごとのホームページ（カテゴリー名も表示しておく）
def user(request, username):
    # ユーザーのカテゴリーデータをuser.htmlに送らなくてはならない
    user = User.objects.filter(username=username)
    category_list = CategoryModel.objects.filter(author_id = user[0])
    return render(request, 'user.html', {'object_list': category_list})

# 写真のリスト表示
def images_listview(request, username):
    # ユーザーを取得
    user = User.objects.filter(username=username)
    # そのユーザーの画像を取得、カテゴリーモデルから写真のリストを取得する
    image_list = ImageModel.objects.filter(author_id=user[0])
    return render(request, 'images_list.html', {'object_list': image_list})

# 写真リスト内の写真をタップすると写真を拡大する
def imageview(request, pk):
    object = ImageModel.objects.get(pk = pk)
    #username = object.author.username
    return render(request, 'image.html', {'object': object})

# 新しいカテゴリーを作成した後
class CreateCategory(CreateView): 
    template_name = 'create_category.html'
    model = CategoryModel
    fields = ('name', 'author_id', 'description1', 'description2', 'language')
    success_url = reverse_lazy('user.html')

class CreateImage(CreateView):
    template_name = 'create_image.html'
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