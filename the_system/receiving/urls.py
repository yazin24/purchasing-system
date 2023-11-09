from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name = 'mainpage'),
    path('home/', views.receiving_home_page, name = 'receivinghomepage'),
    path('receiving-monitoring/', views.receiving_receiving_monitoring, name = 'receivingreceivingmonitoring'),
    path('received-po/', views.receiving_received_po, name = 'receivingreceivedpo'),
    path('all-items/', views.receiving_items, name = 'receivingallitems'),
    path('undelivered/', views.receiving_undelivered, name = 'receivingundelivered'),
]