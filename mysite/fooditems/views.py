from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import fooditems,Order,cartitems

def profile(request):
    # Any additional context data for the profile page can be added here
    return render(request, 'fooditems/profile.html')

@login_required(login_url='/login/')
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

    # Get previously selected items (if any)
    selected_items = request.POST.getlist('selected_items')  # Get a list of selected item IDs

    # Return the food items and previously selected items to the template
    return render(request, 'fooditems/manu.html', {
        'manuitems': manuitems,
        'selected_items': selected_items,
    })

# Create your views here.
def manu(request):
    manuitems = fooditems.objects.all()
    user = request.user
    return render(request, 'fooditems/manu.html', {'manuitems': manuitems, 'user': user})


@login_required(login_url='/login/')
def buy_items(request):
    if request.user.is_authenticated:  # Check if the user is authenticated
        print("buy items view-------------------")
        if request.method == 'POST':
            print("post method buy items view-------------------") 
            selected_item_ids = request.POST.getlist('selected_items')  # Get list of selected item IDs
            selected_items = fooditems.objects.filter(id__in=selected_item_ids)  # Query items based on the selected IDs 
            total_price = 0  # Variable to store total price
            
            request.session['selected_items'] = selected_item_ids
            # Calculate total price based on the quantity of each selected item
            for item in selected_items:
                quantity = int(request.POST.get(f'quantity_{item.id}', 1))  # Get the quantity for the item, default to 1
                item.total_price = item.price * quantity  # Add total price to item
                total_price += item.total_price  # Accumulate the total price

            return render(request, 'fooditems/order_success.html', {
                'selected_items': selected_items,
                'total_price': total_price  # Pass the total price to the template
            })
        else:
            # Handle GET request (if any)
            return redirect('selectsuccess')  # You can redirect back to menu or show an appropriate page
    else:
        return redirect('login') 
def select_success(request):
    # Fetch the selected items and total price
    selected_items = request.session.get('selected_items', [])
    total_price = request.GET.get('total_price', 0)  # Get total price from URL or session

    # Query items from the database based on selected item IDs
    items = fooditems.objects.filter(id__in=selected_items)

    return render(request, 'fooditems/order_success.html', {
        'selected_items': items,
        'total_price': total_price  # Pass the total price to the template
    })    

@login_required(login_url='/login/')
def order_items(request):
    print("order items view=============")
    # Fetch all items to display on the page
    items = fooditems.objects.all()
    selected_item_ids = request.session.get('selected_items', [])
    selected_items = fooditems.objects.filter(id__in=selected_item_ids)

    # Process the order

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        for item in selected_items:
            print("item id",item.id,type(item))
            order = Order.objects.create(
                user=request.user,
                item=item,
                name=name,
                address=address,
                phone=phone,
                email=email
            )
            order.save()
        messages.success(request, 'Order placed successfully!')
        return redirect('selectsuccess')  # Redirect to an order success page

    # Pass the items to the template
    return render(request, 'pages/order_items.html', {'items': items})
def selectsuccess(request):
    order_item_ids = request.session.get('selected_items', [])
    order_items = fooditems.objects.filter(id__in=order_item_ids)
    total_price = 0
    for item in order_items:
        total_price += item.price
    return render(request, 'fooditems/selectsuccess.html',{'order_items': order_items,'total_price': total_price})
from django.shortcuts import render, redirect
from .models import cartitems, fooditems

@login_required(login_url='/login/')
def cart_view(request):
    user = request.user
    items = cartitems.objects.filter(user=user)
    
    if not items:
        return render(request, 'fooditems/cart.html', {'message': 'Your cart is empty.', 'user': user})

    return render(request, 'fooditems/cart.html', {'items': items, 'user': user})

@login_required(login_url='/login/')
def add_to_cart(request, item_id):
    user = request.user
    item = fooditems.objects.get(id=item_id)
    cart_item, created = cartitems.objects.get_or_create(user=user, item=item)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required(login_url='/login/')
def remove_from_cart(request, item_id):
    user = request.user
    item = fooditems.objects.get(id=item_id)
    cart_item = cartitems.objects.get(user=user, item=item)
    cart_item.delete()  # Remove item from cart
    return redirect('cart')

@login_required(login_url='/login/')
def update_quantity(request, item_id):
    user = request.user
    item = fooditems.objects.get(id=item_id)

    # Get or create the cart item for the given user and item
    cart_item, created = cartitems.objects.get_or_create(user=user, item=item)

    if 'increase' in request.POST:
        cart_item.quantity += 1  # Increase the quantity of the item in the cart
    elif 'decrease' in request.POST and cart_item.quantity > 1:
        cart_item.quantity -= 1  # Decrease the quantity, ensuring it doesn't go below 1
    
    # Save the updated cart item
    cart_item.save()

    # Redirect to the cart page after updating the quantity
    return redirect('cart')

