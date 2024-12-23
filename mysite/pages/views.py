from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect 
from django.shortcuts import render, get_object_or_404
from .models import MenuItem
from django.http import HttpResponse 
def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')  # Use .get() to avoid KeyError
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('signup')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return HttpResponse('login')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'pages/loginpage.html')

def index(request):
    return render(request, 'pages/index.html')
    
def menu(request):
    return render(request, 'pages/menu.html')

def order(request):
    return render(request, 'pages/order.html')

def contact(request):
    return render(request, 'pages/contact.html')

def login(request):
    return render(request, 'pages/login.html')
def viewmanu(request):
    return render(request, 'pages/viewmanu.html')
def menu_item_detail(request, slug):
    menu_item = get_object_or_404(MenuItem, slug=slug)
    return render(request, 'menu_item_detail.html', {'menu_item': menu_item})


