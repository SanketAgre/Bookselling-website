from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request,'app/index.html')

def category(request):
    category=Category.objects.filter(status=0)
    contex={category:'category'}
    return render(request, "product/category.html", contex)