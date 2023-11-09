from django.shortcuts import render, redirect, get_object_or_404

def main_page(request):
    
    return render(request, 'receiving_body.html')

def receiving_home_page(request):
    
    return render(request, 'home_receiving.html')

def receiving_receiving_monitoring(request):
    
    return render(request, 'receiving_monitoring.html')

def receiving_received_po(request):
    
    return render(request, 'received_po.html')

def receiving_items(request):
    
    return render(request, 'items.html')

def receiving_undelivered(request):
    
    return render(request, 'undelivered.html')
