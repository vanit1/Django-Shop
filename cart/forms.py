from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label='Кількість', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(label='Оновити кількість', required=False, initial=False)