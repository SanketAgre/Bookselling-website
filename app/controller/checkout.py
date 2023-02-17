from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import login_required


@login_required(login_url="loginpage")
def checkout(request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            return redirect("/cart")
    cartitems= Cart.objects.filter(user=request.user)
    total_price= 0
    for item in cartitems:
        total_price= total_price + item.product.selling_price * item.product_qty

    # userprofile=Profile.objects.filter(user=request.user).first()

    context={'cartitems':cartitems, 'total_price':total_price,  }
    return render(request, 'checkout/checkout.html',context)