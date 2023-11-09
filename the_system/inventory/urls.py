from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name = 'mainpage'),
    path('home/', views.inventory_home_page, name = 'inventoryhomepage'),
    path('items-monitoring/', views.inventory_items_monitoring, name = 'inventoryitemsmonitoring'),
    path('suppliers/', views.inventory_suppliers, name = 'inventorysuppliers'),
    path('receiving-history/', views.inventory_receiving_history, name = 'inventoryreceivinghistory'),
]