from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name = 'mainpage'),
    path('home/', views.home_page, name = 'homepage'),
    path('add-po/', views.add_po, name = 'addpo'),
    path('purchase-monitoring', views.purchase_monitoring, name = 'purchasemonitoring'),
    path('suppliers/', views.suppliers, name = 'suppliers'),
    path('products/', views.products, name = 'products'),
]