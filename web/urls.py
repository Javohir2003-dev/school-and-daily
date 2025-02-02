
from django.contrib import admin
from django.urls import path,include
from web import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('sciences.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
