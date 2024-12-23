from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import forms
from fooditems.models import fooditems

def place_order(request):
    if request.method == 'POST':
        form = forms(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('order_success')  # Redirect to success page
        else:
            print(form.errors)  # Print any form validation errors
    else:
        form = forms()

    return render(request, 'place_order.html', {'form': form})
def search_items(request):
    query = request.GET.get('query', '')  # Get the search query from the GET request
    if query:
        # Filter the food items based on the query (case-insensitive search)
        manuitems = fooditems.objects.filter(name__icontains=query)
    else:
        manuitems = fooditems.objects.all()  # Show all items if no query is provided

    return render(request, 'fooditems/manu.html', {'manuitems': manuitems})

# Create your views here.
def manu(request):
    manuitems = fooditems.objects.all()
    return render(request, 'fooditems/manu.html', {'manuitems': manuitems})


def buy_items(request):
    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')  # Get list of selected item IDs
        selected_items = fooditems.objects.filter(id__in=selected_item_ids)

        # You can add logic here to process the purchase (e.g., create an order, charge the user, etc.)
        # For now, we'll just redirect to a success page
        return render(request, 'fooditems/order_success.html', {'selected_items': selected_items})
    return redirect('manu')  # If not POST, redirect to the menu page


def order_success(request):
    # Get the selected items passed from the previous page
    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')
        selected_items = fooditems.objects.filter(id__in=selected_item_ids)
        
        # Store the selected items in the session or pass it to the context
        request.session['selected_items'] = selected_item_ids
        
        return render(request, 'fooditems/order_success.html', {'selected_items': selected_items})
    
    return redirect('menu')  # If not POST, redirect to menu page

def selectsuccess(request):
    return render(request, 'selectsuccess.html')