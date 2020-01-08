from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=128)
    text = forms.CharField(widget=forms.Textarea)

