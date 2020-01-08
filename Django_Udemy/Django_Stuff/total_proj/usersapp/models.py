# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create a non-User Model with User as ForeignKey
# Extend the User model using a user = models.OneToOneField(User)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username


class FavoritePlayer(models.Model):
    player_name = models.CharField(max_length=256)
    reason = models.TextField(max_length=2058)

    def __str__(self):
        return self.player_name
