# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from baseapp.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse


def index_view(request):
    inject_dict = {"inject_key":"Here's some injected text"}
    return render(request, "index.html", context=inject_dict)

def form_input_view(request):
    if request.method == "POST":
        userform = UserForm(data=request.POST)
        user = userform.save()
        user.set_password(user.password)
        user.save()

        upiform = UserProfileInfoForm(data=request.POST)
        upi = upiform.save(commit=False)
        upi.user = user
        upi.save()
    else:
        userform = UserForm()
        upiform = UserProfileInfoForm()

    formdict = {"userform":userform, "upiform":upiform}

    return render(request, "form_input.html", context=formdict)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Login failed, user not active")
        else:
            return HttpResponse("Login failed, invalid user")
    else:
        return render(request, 'baseapp/login.html')