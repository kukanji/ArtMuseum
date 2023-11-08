from django.shortcuts import render
from django.contrib.auth.models import User
from ..models import image, category, user_home
import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# トップページ
def top(request):
    author_list = User.objects.all()
    return render(request, 'top.html', {'author_list': author_list})

# ユーザーごとのホームページ（カテゴリー名も表示しておく）
def user(request, username):
    # ユーザーのカテゴリーデータをuser.htmlに送らなくてはならない
    # objectsは、データベースのテーブルに対応するモデルクラスのマネージャー
    logger.info("write logger under this comment")
    logger.info(f"username: {username}")
    user = User.objects.get(username=username)
    logger.info(f"user: {user}")
    categories = category.objects.filter(author = user)
    single_user_home = user_home.objects.get(author = user)
    return render(request, 'user.html', {'categories': categories, 
                                         'user_home': single_user_home,
                                         'username': username})

# 写真のリスト表示
def images_list(request, username, category_name):
    single_category = category.objects.get(name = category_name)
    # そのユーザーの画像を取得、カテゴリーモデルから写真のリストを取得する
    image_list = image.objects.filter(category = single_category)
    # ユーザーを取得
    user = User.objects.get(username=username)
    categories = category.objects.filter(author = user)
    return render(request, 'images_list.html', {
        'image_list': image_list,
        'category': category,
        'categories': categories,
        'username': username,
        })