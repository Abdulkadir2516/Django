from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('artir/', views.sayaci_artir, name='sayaci_artir'),
]
