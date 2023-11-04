from django.shortcuts import render, redirect, get_object_or_404

def main_page(request):
    
    return render(request, 'receiving_body.html')

def home_page(request):
    
    return render(request, 'home_receiving.html')

def receiving_monitoring(request):
    
    return render(request, 'receiving_body.html')

def received_po(request):
    
    return render(request, 'received_po.html')

def items(request):
    
    return render(request, 'items.html')

def undelivered(request):
    
    return render(request, 'undelivered.html')
