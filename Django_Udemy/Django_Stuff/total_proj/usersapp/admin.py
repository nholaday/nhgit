# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from usersapp.models import FavoritePlayer, UserProfileInfo

# Register your models here.
admin.site.register(FavoritePlayer)
admin.site.register(UserProfileInfo)
