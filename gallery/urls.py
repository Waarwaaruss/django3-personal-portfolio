from django.urls import path 
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('<int:gallery_id>/', views.details, name='details'),
]
