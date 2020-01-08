# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name

class FavFoods(models.Model):
    person = models.ForeignKey(Person)
    food = models.CharField(max_length=264)

    def __str__(self):
        return "yummy " + self.food

class Age(models.Model):
    person = models.ForeignKey(Person)
    age = models.IntegerField()
    
    def __str__(self):
        return "{} is {} years old".format(self.person, self.age)

