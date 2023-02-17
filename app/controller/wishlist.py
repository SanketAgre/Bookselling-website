from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from app.models import *
from app.forms import *
from django.contrib.auth.decorators import login_required

def wishlist(request):
    wishlist=Wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlist}
    return render(request, "wishlist/wishlist.html", context)

def addtowishlist(request):
    if request.method == 'POST':
        if(request.user.is_authenticated):
            prod_id=int(request.POST.get('product_id'))
            prod_check=Product.objects.get(id=prod_id)
            if(prod_check):
                if(Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':"Product already in Whishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':"Product added in Whishlist"})
            else:
                return JsonResponse({'status':"Product not found"})
        else:
            return JsonResponse({'status':"Login to continue"})

    else:
        return redirect("/")


def deletewishlistitem(request):
    if(request.method == 'POST'):
        prod_id=request.POST.get('product_id')
        prod_check=Wishlist.objects.get(user=request.user, product_id=prod_id)
        if(prod_check):
            prod_check.delete()
            return JsonResponse({'status':'Product deleted Successfuly'})
        else:
            return JsonResponse({'status':'Product not found'})