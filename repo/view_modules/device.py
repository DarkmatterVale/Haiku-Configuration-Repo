import django

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout

from ..models import Device


def deviceList(request):
    all_devices = Device.objects.all()
    context = {'all_devices' : all_devices}

    return render(request, 'repo/device_list.html', context)

def sortDevices(request):
    sort_name = request.POST['name_to_sort']

    # sorting based on name
    all_devices = Device.objects.all()
    sorted_devices = []
    for grabbed_device in all_devices:
        if sort_name in grabbed_device.name:
            sorted_devices.append(grabbed_device)

    context = {'all_devices' : sorted_devices}

    return render(request, 'repo/device_list.html', context)

def deviceDetail(request, device_id):
    myDevice = get_object_or_404(Device, pk=device_id)
    context = {
        'device_name' : myDevice.name,
        'all_devices' : [myDevice]
    }

    return render(request, 'repo/device.html', context)
