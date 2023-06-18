from django.urls import path, include, re_path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<slug:product_slug>', views.cart_add, name='cart_add'),
    path('remove/<slug:product_slug>', views.cart_remove, name='cart_remove'),
    path('cart_clear', views.cart_clear, name='cart_clear'),
]