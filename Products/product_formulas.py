def sale_of_product(obj):
    sale = float(obj.sale)
    price = obj.price
    pr_ot_ch = (price * sale) / 100
    return round(price - pr_ot_ch, 1)