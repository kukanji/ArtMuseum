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
    # objectsは、データベースのテーブルに対応するモデルクラスのマネージャー
    user = User.objects.get(username=username)
    categories = Category.objects.filter(author = user)
    user_home = UserHome.objects.get(author = user)
    return render(request, 'user.html', {'categories': categories, 
                                         'user_home': user_home,
                                         'username': username})

# 写真のリスト表示
def images_list(request, username, category_name):
    category = Category.objects.get(name = category_name)
    # そのユーザーの画像を取得、カテゴリーモデルから写真のリストを取得する
    image_list = Image.objects.filter(category = category)
    # ユーザーを取得
    user = User.objects.get(username=username)
    categories = Category.objects.filter(author = user)
    category = Category.objects.get(name = category_name)
    return render(request, 'images_list.html', {
        'image_list': image_list,
        'category': category,
        'categories': categories,
        'username': username,
        })