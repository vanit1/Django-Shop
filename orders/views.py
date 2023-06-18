from django.shortcuts import render, redirect, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from Products.context_process import balance
from Products.models import *
from django.contrib.auth.models import User
from .change_balance import *


def order_create(request):
    cart = Cart(request)
    balance_user = balance(request)
    if request.method == 'POST':
        if check_balance(cart_us=cart, balance=balance_user['balance']):
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                request.session['order'] = order.id
                for item in cart:
                    data_accs = item['product'].psw_and_lg.split(":")
                    lst = []
                    count = 0
                    while len(lst)!=item['quantity']:
                        lst.append(data_accs[count])
                        del data_accs[count]
                        count+=1
                    item['product'].psw_and_lg = ':'.join(data_accs)
                    item['product'].save()
                    OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'],
                                            data_of_acc='\n'.join(lst))
                # очистка корзины
                change_bal(request, cart, balance_user['balance'])
                off_products(cart_us=cart)
                cart.clear()
                return render(request, 'orders/created.html',
                            {'order': order, 'title': 'Успішно'})
    else:
        form = OrderCreateForm()
        sum_bal = sum([item['price'] * item['quantity'] for item in cart])
        if sum_bal <= balance_user['balance']:
            context = {'cart': cart,
                    'form': form,
                    'title': 'Замовлення'}
        else:
            cart = Cart(request)
            return render(request, 'cart/detail.html', {'cart': cart,
                                                        'title': 'Корзина',
                                                        'cats': Category.objects.all(),
                                                        'error': 'Недостатньо коштів'})
    return render(request, 'orders/create.html', context=context)