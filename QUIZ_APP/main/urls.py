from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', views.home, name="home"),
    path('test/', views.test)
]