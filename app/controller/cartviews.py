from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="loginpage")
def addtocart(request):
    if request.method == 'POST':
        try:
            if request.user.is_authenticated:
                prod_id= int(request.POST.get('product_id'))
                product_check=Product.objects.get(id=prod_id)
                if(product_check):
                    if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                        return JsonResponse({'status':'product already in cart'})  
                    else:
                        prod_qty=int(request.POST.get('product_qty'))
                        if product_check.quantity >= prod_qty:
                            Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty )
                            return JsonResponse({'status':'Product added Successfuly' })  
                        else:
                            return JsonResponse({'status':'only '+ str(product_check.quantity) + ' quantity is avilable' })  
                else:
                    return JsonResponse({'status':'product not found'})  
            else:
                return JsonResponse({'status':'Login to continue'})
        except Exception as e:
            return JsonResponse({'status':'Retry'})
    else:
        return redirect('/')

@login_required(login_url="loginpage")
def cart(request):
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request, "cart/cartview.html", context)


@login_required(login_url="loginpage")
def updatecart(request):
    if request.method == 'POST':
        prod_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty=int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty=prod_qty
            cart.save()
            return JsonResponse({'status':"Update Successfully"})
    else:
        return redirect("/")  

@login_required(login_url="loginpage")
def deletecartitem(request):
    if request.method == 'POST':
        prod_id=request.POST.get('product_id')
        if(Cart.objects.filter(user=request.user, product_id=prod_id)):
            cart=Cart.objects.filter(user=request.user, product_id=prod_id)
            cart.delete()
        return JsonResponse({'status':"Deleted Successfully"})
    else:
        return redirect("/") 

   
    