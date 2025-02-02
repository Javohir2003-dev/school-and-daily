from django.urls import path
from web import settings
from django.conf.urls.static import static
from .views import home,index,TeacherView,ClassesDetailView,classes_detail

urlpatterns = [
    
     path('', home, name='bosh'),
     path('index/', index, name='index'),
     path("teacher/", TeacherView.as_view(), name='teacher'),
     path('siflar/<int:id>/', classes_detail, name='class_detail'),
     # path("sinf/<int:id>/", ClassesDetailView.as_view(), name="class_detail"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)