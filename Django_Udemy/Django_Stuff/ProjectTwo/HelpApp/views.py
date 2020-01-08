# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def help(request):
    mydict = {"help_html": "<em>This is inserted via<strong>django</strong></em>"}
    return render(request, 'HelpApp/help.html', context=mydict)