from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name = 'mainpage'),
    path('home/', views.home_page, name = 'homepage'),
    path('receiving-monitoring/', views.receiving_monitoring, name = 'receivingmonitoring'),
    path('received-po/', views.received_po, name = 'receivedpo'),
    path('all-items/', views.items, name = 'allitems'),
    path('undelivered/', views.undelivered, name = 'undelivered'),
]