from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from app.models import *
from app.forms import *
from django.contrib import messages


def register(request):
    form=CustomUserForm()
    try:
        if request.method=='POST':
            form=CustomUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "REGISTER SUCCESSFILY! login to continue")
                return redirect("/login")
    except Exception as e:
        messages.error(request, "RETRY")
    context={'form':form}
    return render(request,"auth/register.html", context)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are Already Logged in")
        return redirect("/")
    else:
        try:
            if request.method == 'POST':
                name=request.POST.get('username')
                passwd=request.POST.get('password')

                user = authenticate(request, username=name, password=passwd)

                if user is not None:
                    login(request, user)
                    messages.success(request, "You are logged in successfuly")
                    return redirect("/")
                else:
                    messages.warning(request, "Invalid Username or password")
                    return redirect("/login")
        except Exception as e:
            messages.error(request, "RETRY")

    return render(request, "auth/login.html")


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged Out Successfuly')
    return redirect("/")
