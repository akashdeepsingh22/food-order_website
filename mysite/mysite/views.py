from django.shortcuts import render, redirect
from .models import MenuItem, Order
from .forms import OrderForm
from django.http import Http404

# View to display the menu
def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'restaurant/menu.html', {'items': items})

# View to handle the order submission
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_success', order_id=order.id)
    else:
        form = OrderForm()

    return render(request, 'restaurant/place_order.html', {'form': form})

# View to display a successful order
def order_success(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        raise Http404("Order not found")
    
    return render(request, 'restaurant/order_success.html', {'order': order})