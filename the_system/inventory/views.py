from django.shortcuts import render, redirect, get_object_or_404

def main_page(request):
    return render(request, 'inventory_body.html')

def home_page(request):
    return render(request, 'home_inventory.html')

def items_monitoring(request):
    return render(request, 'items_monitoring.html')

def suppliers(request):
    
    return render(request, 'suppliers.html')

def receiving_history(request):
    
    return render(request, 'receiving_history.html')
