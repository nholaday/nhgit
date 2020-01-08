# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from users_app.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def UsersView(request):
    users_list = User.objects.all()
    users_dict = {'UserInject': users_list}
    return render(request, 'users.html', context=users_dict)
