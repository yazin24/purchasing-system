from django.shortcuts import render, redirect, get_object_or_404

def main_page(request):
    
    return render(request, 'receiving_body.html')
