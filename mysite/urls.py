# urls.py

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from tutorial import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutorial.urls')),
    path('', views.index, name='index'),
]

# Adicionar configuração de arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
