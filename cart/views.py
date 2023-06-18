from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from Products.models import Product
from .cart import Cart
from Products.models import *
from .forms import *


@require_POST
def cart_add(request, product_slug):
    cart = Cart(request)
    product = Product.objects.get(slug=product_slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart_now = request.session['cart']
        if not cd['update']:
            if (str(product.id) not in cart_now and cd['quantity']<=product.quantity)\
                or (str(product.id) in cart_now and cd['quantity']+cart_now[str(product.id)]['quantity'] <= product.quantity):
                cart.add(product=product,
                        quantity=cd['quantity'],
                        update_quantity=cd['update'])
            else:
                return render(request, 'Products/product_detail.html',
                          {'product': product,
                           'error': 'В наявності немає такої кількості',
                           'cats': Category.objects.all(),
                           'form': form})
        elif cd['update'] and cd['quantity']<=product.quantity:
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        else:
            return render(request, 'Products/product_detail.html',
                          {'product': product,
                           'error': 'В наявності немає такої кількості',
                           'cats': Category.objects.all(),
                           'form': form})
    return redirect('products:product', product.slug)


def cart_remove(request, product_slug):
    cart = Cart(request)
    product = Product.objects.get(slug=product_slug)
    cart.remove(product)
    if not request.session['cart']:
        return redirect('products:home')
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart, 'title': 'Корзина', 'cats': Category.objects.all()})



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('products:home')