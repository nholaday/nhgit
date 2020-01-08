# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from LunaApp.models import Person, FavFoods, Age

# Register your models here.
admin.site.register(Person)
admin.site.register(FavFoods)
admin.site.register(Age)
