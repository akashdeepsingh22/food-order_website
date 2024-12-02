from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'phone_number', 'address', 'items']
        widgets = {
            'items': forms.CheckboxSelectMultiple(),
        }