from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'shop/index.html')

def register(request):
    return render(request,'shop/register.html')

def collections(request):
    categories = Category.objects.filter(status=False)  # fetch only visible categories
    return render(request, 'shop/collections.html', {"categories": categories})


def collectionsview(request, name):
    if Category.objects.filter(name=name, status=0).exists():
        products = Product.objects.filter(category__name=name, status=0)
        return render(request, 'shop/products/index.html', {"products": products, "category_name    ":name})
    else:
        messages.warning(request, "No such Category Found")
        return redirect('collections')
    
def cart(request):
    return render(request, 'shop/cart.html')