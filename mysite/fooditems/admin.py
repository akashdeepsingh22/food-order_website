from django.contrib import admin
from .models import fooditems,Order, cartitems


# Register your models here.
admin.site.register(fooditems)
admin.site.register(Order)
admin.site.register(cartitems)