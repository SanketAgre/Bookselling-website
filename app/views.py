from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'app/index.html')

def collections(request):
    category=Category.objects.filter(status=0)
    contex={'category':category}
    return render(request, "product/category.html", contex)

def collectionviews(request,slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products=Product.objects.filter(category__slug=slug, status=0)
        category=Category.objects.filter(slug=slug).first()

        context={'products':products, 'category':category}
    else:
        messages.error(request, 'Category not found')
        return redirect("/collections")
    return render(request, "product/categoryview.html", context)
