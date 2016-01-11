from django.contrib import admin

from .models import Component
from .models import Device

admin.site.register(Component)
admin.site.register(Device)
