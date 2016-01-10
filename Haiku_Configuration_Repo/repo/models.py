from __future__ import unicode_literals

from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=200)
    is_working = models.CharField(max_length=10)
    rating = models.IntegerField()

    def __str__(self):
        return self.name
