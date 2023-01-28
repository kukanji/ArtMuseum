#from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
#from django.db import IntegrityError
#from django.contrib.auth import authenticate, login, logout
##from ..models import ReviewModel
#from django.views.generic import CreateView
#from django.urls import reverse_lazy
#
## Create your views here.
#def signupview(request):
#    if request.method == 'POST':
#        username_data = request.POST['username_data']
#        password_data = request.POST['password_data']
#        try:
#            user = User.objects.create_user(username_data, '', password_data)
#        except IntegrityError:
#            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています。'})
#    else:
#        return render(request, 'signup.html', {})
#    # サインアップ後にサイトに遷移する
#    return render(request, 'signup.html', {})
#
#def loginview(request):
#    if request.method == 'POST':
#        username_data = request.POST['username_data']
#        password_data = request.POST['password_data']
#        # ユーザーデータが既に登録されているか照合している
#        user = authenticate(request, username = username_data, password = password_data)
#        # 照会先にユーザーデータが存在したら
#        if user is not None:
#            login(request, user)
#            return redirect('list')
#        else:
#            return redirect('login')
#    # ログイン用のボタンをサイトに設置しておいてログイン後はサイトに戻れるようにする
#    return render(request, 'login.html')
#
#def logoutview(request):
#    logout(request)
#    return redirect('login')


