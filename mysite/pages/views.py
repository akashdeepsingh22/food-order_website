from django.shortcuts import render

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
