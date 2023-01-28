from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webpost.urls')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # settings内のmedia_urlが合致した際にdocument_rootで定義した画像を呼び出す
