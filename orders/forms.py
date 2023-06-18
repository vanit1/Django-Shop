from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email']
        labels = {
            "name": "Телеграм",
            "email": "Пошта",
        }