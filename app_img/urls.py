from django.urls import path
from . import views

app_name = 'app_img'

urlpatterns = [
    path('create/', views.image_create, name='create'),
]
