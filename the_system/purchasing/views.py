from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponseBadRequest
from .forms import SupplierForm, ItemForm

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

def add_supplier(request):
    if request.method == 'POST':
        
        supplier_form = SupplierForm(request.POST)
        
        if not supplier_form.is_valid():
            return HttpResponseBadRequest('Invalid supplier data. Please try again.')
        