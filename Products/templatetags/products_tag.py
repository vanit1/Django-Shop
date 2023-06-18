from django import template
from ..product_formulas import sale_of_product


register = template.Library()

@register.filter
def go_sale(object):
    return sale_of_product(object)

@register.filter
def ret_price(dicter):
    return f"кол-во {dicter['quantity']}; сума {dicter['quantity']*dicter['price']}"
