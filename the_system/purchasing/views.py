from django.shortcuts import render, redirect, get_list_or_404

#purchasing navbar
def main_page(request):
    
    return render(request, 'main_body.html')

def purchasing_home_page(request):
    
    return render(request, 'home_purchasing.html')

def purchasing_add_po(request):
    
    return render(request, 'add_p.o.html')

def purchasing_purchase_monitoring(request):
    
    return render(request, 'purchase_monitoring.html')

def purchasing_suppliers(request):
    
    return render(request, 'suppliers.html')

def purchasing_products(request):
    
    return render(request, 'products.html')

#purchasing functions 

def supplier_form(request):
    
    return render(request, 'add_supplier_form.html')