import django

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout

from ..models import Component
from ..models import Device

def display_index_page(request):
    recent_components = Component.objects.all().order_by('-date_modified')[:5]
    recent_devices = Device.objects.all().order_by('-date_modified')[:5]
    context = {
        'recent_devices' : recent_devices,
        'recent_components' : recent_components
    }
    
    return render(request, 'repo/index.html', context)
