from django.contrib import admin
from .models import fooditems
from .models import Order


# Register your models here.
admin.site.register(fooditems)
admin.site.register(Order)