from django.contrib.auth.models import User
from Products.models import *
from Products.context_process import balance
from cart.context_processors import cart
from Products.models import Product



def check_balance(cart_us, balance):
    if balance - cart_us.get_total_price() < 0:
        return False
    return True

def change_bal(request, cart_us, balance):
    us = User.objects.get(username=request.user.username)
    us_det = UserDetail.objects.get(user_old=us)
    us_det.change_balance(balance - cart_us.get_total_price())
    us_det.save()

def off_products(cart_us):
    res_dct = {}
    for item in cart_us:
        res_dct[item['product'].id] = item['quantity']
    for product_id in res_dct:
        pr = Product.objects.get(id=int(product_id))
        if pr.quantity == 1:
            pr.is_publish = False
            pr.save()
        else:
            if pr.quantity - res_dct[product_id] <= 0:
                pr.is_publish=False
            else:
                pr.quantity -= res_dct[product_id]
            pr.save()