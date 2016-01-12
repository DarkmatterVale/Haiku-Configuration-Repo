from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    """User profile.  Contains some basic configurable settings"""

    user = models.OneToOneField(User, unique=True)
    password = models.CharField(max_length=256, blank=True, default='')

class Component(models.Model):
    name = models.CharField(default='', max_length=200)
    notes = models.CharField(default='', max_length=500)
    is_working = models.CharField(default='', max_length=10)
    rating = models.IntegerField()
    category = models.CharField(default='', max_length=100)

    author_first_name = models.CharField(default='', max_length=50)
    author_last_name = models.CharField(default='', max_length=50)
    author_email = models.CharField(default='', max_length=100)

    date_created = models.DateTimeField('date created', auto_now=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

class Device(models.Model):
    name = models.CharField(default='', max_length=200)
    notes = models.CharField(default='', max_length=500)
    is_working = models.CharField(default='', max_length=10)
    rating = models.IntegerField()

    author_first_name = models.CharField(default='', max_length=50)
    author_last_name = models.CharField(default='', max_length=50)
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
