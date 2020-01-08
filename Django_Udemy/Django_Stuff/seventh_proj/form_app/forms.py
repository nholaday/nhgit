from django import forms
from form_app.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
