from django.urls import path
from .views import signupview, loginview, logoutview, listview, detailview, CreateClass, evaluationview

urlpatterns = [
    # 管理画面
    path('signup',  signupview, name = 'signup'),
    path('login', loginview, name = 'login'),
    path('logout', logoutview, name = 'logout'),

    # 非管理画面
    path('<str:username>/images/list', listview, name = 'list'),
    path('images/<int:pk>', detailview, name = 'detail'),
    path('images/create', CreateClass.as_view(), name = 'create'),
    path('evaluation/<int:pk>', evaluationview, name = 'evaluation')
]