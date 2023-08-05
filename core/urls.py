from .configuracion import settings

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from apps.posts.views import NotFoundView


handler404 = NotFoundView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.posts.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)