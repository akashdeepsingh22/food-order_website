from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect 
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

# View for the home page
def index(request):
    return render(request, 'pages/index.html')

# View for the menu page

def menu(request):
    return render(request, 'pages/menu.html')

# View for the order page
def order(request):
    return render(request, 'pages/order.html')

# View for the contact page
def contact(request):
    return render(request, 'pages/contact.html')

# View for the login page
def login(request):
    return render(request, 'pages/login.html')
