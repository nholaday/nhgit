# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    inject_dict = {
        "inject_text":"Milk was a bad choice",
        "inject_num":5,
    }
    return render(request, 'index.html', context=inject_dict)

def blog_index(request):
    return render(request, 'blogapp/blog_index.html')

def relative(request):
    return render(request, 'blogapp/relative_url_template.html')

def media(request):
    return render(request, 'blogapp/media.html')
