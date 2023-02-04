from django.urls import path
from .views import images_list, top, user

urlpatterns = [
    # 管理画面
    #path('signup/',  signupview, name = 'signup'),
    #path('login/', loginview, name = 'login'),
    #path('logout/', logoutview, name = 'logout'),

    # 非管理画面
    path('', top, name = 'top'),
    path('<str:username>/', user, name = 'user'),
    path('<str:username>/<str:category_name>/', images_list, name = 'images_list'),
    #path('<str:category_name>/image/<int:pk>', imageview, name = 'image'),
    #path('image/create_image/', CreateImage.as_view(), name = 'create_image'),
    #path('<str:username>/create_category', CreateCategory.as_view(), name = 'create_cateroy'),
    #path('evaluation/<int:pk>', evaluationview, name = 'evaluation')
]