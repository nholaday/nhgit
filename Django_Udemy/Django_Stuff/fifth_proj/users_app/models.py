# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=254)
    lastname = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname)

