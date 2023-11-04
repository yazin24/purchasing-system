from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name = 'mainpage'),
    path('home/', views.home_page, name = 'homepage'),
]