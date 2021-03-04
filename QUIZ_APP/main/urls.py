from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', views.home, name="home"),
    path('list/', views.test, name="list"),
    path('view/<str:pk>/', views.view, name="view")
]