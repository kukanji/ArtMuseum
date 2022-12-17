from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from ..models import ReviewModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

def listview(request, username):
    # ユーザーを取得
    user = User.objects.filter(username=username)
    # そのユーザーの画像を取得
    object_list = ReviewModel.objects.filter(author=user[0])
    return render(request, 'list.html', {'object_list': object_list})


def detailview(request, pk):
    object = ReviewModel.objects.get(pk = pk)
    return render(request, 'detail.html', {'object': object})


class CreateClass(CreateView):
    template_name = 'create.html'
    model = ReviewModel
    fields = ('title', 'content', 'author', 'images', 'evaluation')
    success_url = reverse_lazy('list')



def evaluationview(request, pk):
    post = ReviewModel.objects.get(pk = pk)
    author_name = request.user.get_username() + str(request.user.id)
    if author_name in post.useful_review_record:
        return redirect('list')
    else:
        post.useful_review = post.useful_review + 1
        post.useful_review_record = post.useful_review_record + author_name
        post.save()
        return redirect('list')
