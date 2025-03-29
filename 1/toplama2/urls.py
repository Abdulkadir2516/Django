from django.urls import path
from . import views

urlpatterns = [
    path('', views.veri_al, name='veri_al'),
]