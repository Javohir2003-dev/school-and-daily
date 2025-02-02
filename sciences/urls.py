from django.urls import path
from .views import classes_view


urlpatterns = [
    path('sinflar/', classes_view, name='classes' ),
    
]