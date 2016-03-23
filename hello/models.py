from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    name = models.CharField(default='', max_length=200)
    notes = models.CharField(default='', max_length=500)
    is_working = models.CharField(default='', max_length=10)
    rating = models.IntegerField()
    category = models.CharField(default='', max_length=100)
    
    author = models.CharField(default='', max_length=100)
    author_email = models.CharField(default='', max_length=100)
    
    date_created = models.DateTimeField('date created', auto_now=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

class Device(models.Model):
    name = models.CharField(default='', max_length=200)
    notes = models.CharField(default='', max_length=500)
    is_working = models.CharField(default='', max_length=10)
    rating = models.IntegerField()
    
    author = models.CharField(default='', max_length=100)
    author_email = models.CharField(default='', max_length=100)
    
    date_created = models.DateTimeField('date created', auto_now=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
    
    cpu = models.CharField(default='', max_length=100)
    motherboard = models.CharField(default='', max_length=100)
    hard_drive = models.CharField(default='', max_length=100)
    sound = models.CharField(default='', max_length=100)
    is_sound_working = models.CharField(default='', max_length=10)
    display = models.CharField(default='', max_length=100)
    display_configuration = models.CharField(default='', max_length=20)
    is_display_working = models.CharField(default='', max_length=10)
    graphics_card = models.CharField(default='', max_length=100)
    graphics_card_is_working = models.CharField(default='', max_length=10)
