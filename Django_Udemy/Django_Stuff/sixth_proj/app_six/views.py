# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app_six.forms import MyForm
from app_six.models import Person

# Create your views here.
def index(request):
    test_dict = {'test_key': 'Here is some test text'}
    return render(request, 'index.html', context=test_dict)


def form_view(request):
    if request.method == "POST":
        fo = MyForm(request.POST)
        if fo.is_valid():
            print("Form Validated")
            print("Name: {}".format(fo.cleaned_data['name']))
            print("Email: {}".format(fo.cleaned_data['email']))
            print("Text: {}".format(fo.cleaned_data['text']))

            person = Person.objects.get_or_create(name=fo.cleaned_data['name'])[0]
            person.email = fo.cleaned_data['email']
            person.text = fo.cleaned_data['text']
            person.save()
            print("Person = {}".format(vars(person)))
    else:
        fo = MyForm()

    persons = Person.objects.all()
    context = {
        'form':fo,
        'persons':persons,
    }
    return render(request, 'form_page.html', context=context)

