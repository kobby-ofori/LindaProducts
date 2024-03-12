from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {'products': products})


def product_page(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "product_page.html", {'product': product})


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "log-in successful")
            return redirect('home')
        else:
            messages.success(request, "Credentials error, please try again")
            return redirect('signin')
    else:
        return render(request, "signin.html", {})


def signup(request):
    return render(request, "signup.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "log-out successful")
    return redirect('home')
