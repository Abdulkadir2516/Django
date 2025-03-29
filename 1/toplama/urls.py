from django.urls import path
from . import views

urlpatterns = [
    path('', views.toplama, name='toplama'),
]