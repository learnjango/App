from django.shortcuts import render
from vending_app.models import Products

# Create your views here.
def sandwiches(request):
    products = Products.objects.all()
    context = {
        'pr': products
    }
    return render(request, 'sandwiches.html', context) 

def salads(request):
    products = Products.objects.all()
    context = {
        'pr': products
    }
    return render(request, 'salads.html', context) 

def snacks(request):
    products = Products.objects.all()
    context = {
        'pr': products
    }
    return render(request, 'snacks.html', context) 

def drinks(request):
    products = Products.objects.all()
    context = {
        'pr': products
    }
    return render(request, 'drinks.html', context) 

def sweets(request):
    products = Products.objects.all()
    context = {
        'pr': products
    }
    return render(request, 'sweets.html', context) 