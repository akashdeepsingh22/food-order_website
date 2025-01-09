from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import forms
from fooditems.models import fooditems,Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    user = request.user
    return render(request, 'fooditems/manu.html', {'manuitems': manuitems, 'user': user})



def buy_items(request):
    print("buy items view")
    if request.user.is_authenticated: 
        if request.method == 'POST':
            selected_item_ids = request.POST.getlist('selected_items')  # Get list of selected item IDs
            selected_items = fooditems.objects.filter(id__in=selected_item_ids)  # Query items
            total_price = sum(item.price for item in selected_items)  # Calculate total price

            # Render the order success page with the selected items and total price
            return render(request, 'fooditems/order_success.html', {
                'selected_items': selected_items,
                'total_price': total_price
            })
        return render('fooditems/oder_items.html', {'selected_items': selected_items}, {'total_price': total_price})  # If not POST, redirect to the menu page
    else:
        return redirect('login')  # If user is not authenticated, redirect to login page


@login_required
def order_items(request):
    print("order items view")
    # Fetch all items to display on the page
    items = fooditems.objects.all()

    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')  # Get list of selected item IDs
        quantities = []

        # Loop through selected items to fetch the corresponding quantity
        for item_id in selected_item_ids:
            quantity_key = f"quantity_{item_id}"
            quantity = request.POST.get(quantity_key, 1)  # Default to 1 if no quantity is provided
            quantities.append(int(quantity))

        # Process the purchase (create orders)
        for item_id, quantity in zip(selected_item_ids, quantities):
            item = fooditems.objects.get(id=item_id)
            order = Order.objects.create(
                user=request.user,
                item=item,
                quantity=quantity,
                name=request.user.username,
                email=request.user.email,
                address=request.POST.get('address'),
                phone=request.POST.get('phone')
            )
            order.save()

        messages.success(request, 'Order placed successfully!')
        return redirect('selectsuccess')  # Redirect to an order success page

    # Pass the items to the template
    return render(request, 'pages/order_items.html', {'items': items})

def order_success(request):
    print("order success view")
    # Get the selected items passed from the previous page
    if request.method == 'POST':
        selected_item_ids = request.POST.getlist('selected_items')
        selected_items = fooditems.objects.filter(id__in=selected_item_ids)
        
        # Store the selected items in the session or pass it to the context
        request.session['selected_items'] = selected_item_ids
        
        return render(request, 'fooditems/order_success.html', {'selected_items': selected_items})
    
    return redirect('menu')  # If not POST, redirect to menu page

def selectsuccess(request):
    return render(request, 'fooditems/selectsuccess.html')