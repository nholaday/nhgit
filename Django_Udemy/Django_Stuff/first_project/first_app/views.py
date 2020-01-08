# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.filter().order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)
    # my_dict = {'insert_me':'This was inserted from views.py yo!'}
    # return render(request, 'first_app/index.html',context=my_dict)
