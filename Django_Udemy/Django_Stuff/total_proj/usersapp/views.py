# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from usersapp.forms import FavoritePlayerForm, UserForm, UserProfileInfoForm
from usersapp.models import FavoritePlayer, UserProfileInfo

# Create your views here.
def index_view(request):
    return render(request, "index.html")


def form_index(request):
    fpf = FavoritePlayerForm()
    return render(request, "usersapp/form_index.html", context={"form":fpf})

def thank_you(request):
    fps = FavoritePlayer.objects.all()

    if request.method == "POST":
        fpf = FavoritePlayerForm(request.POST)
        if fpf.is_valid:
            fpf.save()

    return render(request, "usersapp/thankyou.html", context={"fps":fps})


def register_view(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user_form.save()

            upi = profile_form.save(commit=False)
            upi.user = user
            if 'profile_pic' in request.FILES:
                upi.profile_pic = request.FILES['profile_pic']
            upi.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    contextdict = {
        "user_form": user_form,
        "profile_form": profile_form,
        "registered": registered,
    }

    return render(request, "usersapp/register.html", context=contextdict)


def login_view(request):
    return render(request, "usersapp/login.html")


def logout_view(request):
    return render(request, "usersapp/logout.html")
