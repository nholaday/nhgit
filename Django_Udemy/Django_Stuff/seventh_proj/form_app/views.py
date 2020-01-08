# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from form_app.models import User
from form_app.forms import UserForm

# Create your views here.
def index(request):
    users = User.objects.all()

    return render(request, 'index.html', context={'users':users})

def form_view(request):
    fo = UserForm()
    if request.method == "POST":
        fo = UserForm(request.POST)
        if fo.is_valid():
            print("Name: " + fo.cleaned_data['name'])
        fo.save()
    return render(request, 'form_app/fill.html', context={'form':fo})