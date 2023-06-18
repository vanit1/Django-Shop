from .models import *
from django.contrib.auth.models import User

class DataMixin:
    def context_object_return(self, req=None, **kwargs):
        context = kwargs
        context['cats'] = Category.objects.all()
        return context