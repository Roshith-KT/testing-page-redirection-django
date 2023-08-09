from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

def redirect_page(request):
    return render(request, 'redirect_page.html')

