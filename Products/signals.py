# from django.db.models.signals import post_save, pre_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import *

# @receiver(pre_save, sender=Product)
# def create_user_models(instance, **kwargs):
#     if instance.sale > 0:
#         sale = float(instance.sale)
#         price = instance.price
#         pr_ot_ch = (price * sale) / 100
#         instance.price = round(price - pr_ot_ch, 1)