from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name = 'mainpage'),
    path('home/', views.home_page, name = 'homepage'),
    path('items-monitoring/', views.items_monitoring, name = 'itemsmonitoring'),
    path('suppliers/', views.suppliers, name = 'suppliers'),
    path('receiving-history/', views.receiving_history, name = 'receivinghistory'),
]