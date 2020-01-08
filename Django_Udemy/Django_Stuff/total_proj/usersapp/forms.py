from django import forms
from django.contrib.auth.models import User
from usersapp.models import UserProfileInfo, FavoritePlayer


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username", "email", "password")


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ("portfolio", "profile_pic")


class FavoritePlayerForm(forms.ModelForm):
    class Meta:
        model = FavoritePlayer
        fields = ("player_name", "reason")