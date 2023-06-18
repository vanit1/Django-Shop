from .models import UserDetail
from django.contrib.auth.models import User

def balance(request):
    if request!=None and request.user.is_authenticated:
        us = User.objects.get(username=request.user.username)
        if UserDetail.objects.filter(user_old=us):
            return {'balance': UserDetail.objects.get(user_old=us).balance}
        else:
            return {'balance': ''}
    else:
        return {'balance': ''}