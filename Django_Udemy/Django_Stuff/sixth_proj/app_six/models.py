# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    text = models.CharField(max_length=10000)
    def __str__(self):
        return self.name + ": " + self.email