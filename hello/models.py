from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):
    name = models.CharField(default='', max_length=200)
    notes = models.CharField(default='', max_length=500)
    is_working = models.CharField(default='', max_length=10)
    rating = models.CharField(default='', max_length=100)
    manufacturer = models.CharField(default='', max_length=100)
    
    category = models.CharField(default='', max_length=100)
    
    author = models.CharField(default='', max_length=100)
    author_email = models.CharField(default='', max_length=100)
    
    date_created = models.DateTimeField('date created', auto_now=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    haiku_revision = models.CharField(default='', max_length=100)
    haiku_arch = models.CharField(default='', max_length=10)

class Device(models.Model):
    name = models.CharField(default='', max_length=200)
    notes = models.CharField(default='', max_length=500)
    is_working = models.CharField(default='', max_length=10)
    rating = models.CharField(default='', max_length=100)
    manufacturer = models.CharField(default='', max_length=100)
    
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

    lan_network_chipset = models.CharField(default='', max_length=100)
    wlan_network_chipset = models.CharField(default='', max_length=100)
    does_usb2_work = models.CharField(default='', max_length=10)
    does_usb3_work = models.CharField(default='', max_length=10)
    does_optical_drive_work = models.CharField(default='', max_length=10)
    does_card_reader_work = models.CharField(default='', max_length=10)

    haiku_revision = models.CharField(default='', max_length=100)
    haiku_arch = models.CharField(default='', max_length=10)

    category = models.CharField(default='', max_length=100)