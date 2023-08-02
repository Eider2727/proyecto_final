from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categoria/', views.categoria, name='categoria'),
    path('autor/', views.autor, name='autor'),
    path('articulo/', views.articulo, name='articulo'),
    path('archivo/', views.archivo, name='archivo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
