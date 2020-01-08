# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("testing index page for project")

def LunIndex(request):
    insert_dict = {"injected_text": "This was injected from LunaApp views.py"}
    return render(request, 'temple.html', context=insert_dict)