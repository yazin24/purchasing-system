from django.urls import path
from . import views


urlpatterns = [
    #url for navbar
    
    path('', views.main_page, name = 'mainpage'),
    path('home/', views.purchasing_home_page, name = 'purchasinghomepage'),
    path('add-po/', views.purchasing_add_po, name = 'purchasingaddpo'),
    path('purchase-monitoring', views.purchasing_purchase_monitoring, name = 'purchasingpurchasemonitoring'),
    path('suppliers/', views.purchasing_suppliers, name = 'purchasingsuppliers'),
    path('products/', views.purchasing_products, name = 'purchasingproducts'),
    
    # url for functions
    
    
]