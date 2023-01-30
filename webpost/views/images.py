from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from ..models import Image, Category, UserHome
from django.views.generic import CreateView
from django.urls import reverse_lazy

# トップページ
def top(request):
    author_list = User.objects.all()
    return render(request, 'top.html', {'author_list': author_list})

# ユーザーごとのホームページ（カテゴリー名も表示しておく）
def user(request, username):
    # ユーザーのカテゴリーデータをuser.htmlに送らなくてはならない
    user = User.objects.get(username=username)
    category_list = Category.objects.filter(author = user)
    user_home = UserHome.objects.get(author = user)
    return render(request, 'user.html', {'category_list': category_list, 
                                         'user_home': user_home,
                                         'username': username})

# 写真のリスト表示
def images_list(request, username, category_name):
    category = Category.objects.get(name = category_name)
    # そのユーザーの画像を取得、カテゴリーモデルから写真のリストを取得する
    image_list = Image.objects.filter(category = category)
    # ユーザーを取得
    #user = User.objects.get(username=username)
    #category_list = Category.objects.filter(author = user)
    category = Category.objects.get(name = category_name)
    return render(request, 'images_list.html', {
        'image_list': image_list,
        'category': category,
        'username': username,
        })

# 写真リスト内の写真をタップすると写真を拡大する
#def imageview(request, pk):
#    object = Image.objects.get(pk = pk)
#    #username = object.author.username
#    return render(request, 'image.html', {'object': object})

# 新しいカテゴリーを作成した後
#class CreateCategory(CreateView): 
#    template_name = 'create_category.html'
#    model = Category
#    fields = ('name', 'author_id', 'description1', 'description2', 'language')
#    success_url = reverse_lazy('user.html')
#
#class CreateImage(CreateView):
#    template_name = 'create_image.html'
#    model = Image
#    fields = ('image', 'category_id', 'author_id')
#    success_url = reverse_lazy('images_list')



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