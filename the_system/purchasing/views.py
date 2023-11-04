from django.shortcuts import render, redirect, get_list_or_404

def main_page(request):
    
    return render(request, 'main_body.html')

def home_page(request):
    
    return render(request, 'home_purchasing.html')

def add_po(request):
    
    return render(request, 'add_p.o.html')

def purchase_monitoring(request):
    
    return render(request, 'purchase_monitoring.html')

def suppliers(request):
    
    return render(request, 'suppliers.html')

def products(request):
    
    return render(request, 'products.html')