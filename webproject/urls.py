from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('users/', include('webpost.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^$', RedirectView.as_view(url='/users/', permanent=True)),
    *static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT),
    *static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    # path()はプログラムファイル,static()はCSS等の静的ファイルを呼び出す
    # staticはリスト型が返ってくるから"*"で展開する
]# settings内のmedia_urlが合致した際にdocument_rootで定義した画像を呼び出す