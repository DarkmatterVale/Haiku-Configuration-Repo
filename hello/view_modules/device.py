import django

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from ..models import Device


def list_all_devices_view(request):
    all_devices = Device.objects.all()
    context = {'all_devices' : all_devices}

    return render(request, 'device_list.html', context)

def sort_devices_view(request):
    sort_name = request.POST['name_to_sort']

    # sorting based on name
    all_devices = Device.objects.all()
    sorted_devices = []
    for grabbed_device in all_devices:
        if sort_name in grabbed_device.name:
            sorted_devices.append(grabbed_device)

    context = {'all_devices' : sorted_devices}

    return render(request, 'device_list.html', context)

def device_details_view(request, device_id):
    myDevice = get_object_or_404(Device, pk=device_id)
    context = {
        'device_name' : myDevice.name,
        'all_devices' : [myDevice]
    }

    return render(request, 'device.html', context)

def edit_device_view(request, device_id):
    myDevice = get_object_or_404(Device, pk=device_id)
    context = {
        'device_name' : myDevice.name,
        'device' : myDevice
    }
    
    return render(request, 'edit_device.html', context)

def save_device_view(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    
    device.notes = request.POST['device_notes']
    
    cpu = request.POST['device_cpu']
    motherboard = request.POST['device_motherboard']
    hard_drive = request.POST['device_hard_drive']
    sound = request.POST['device_sound']
    display_name = request.POST['device_display_name']
    display_config = request.POST['device_display_config']
    graphics_card = request.POST['device_dedicated_graphics']
    
    try:
        if str(request.POST['group9']) == "on":
            device.is_working = "Passed"
    except:
        device.is_working = "Failed"
    
    try:
        if str(request.POST['group3']) == "on":
            device.is_sound_working = "Passed"
    except:
        device.is_sound_working = "Failed"
    
    try:
        if str(request.POST['group5']) == "on":
            device.is_display_working = "Passed"
    except:
        device.is_display_working = "Failed"
    
    try:
        if str(request.POST['group7']) == "on":
            device.graphics_card_is_working = "Passed"
    except:
        device.graphics_card_is_working = "Failed"
    
    if cpu == "":
        pass
    else:
        device.cpu = cpu
    
    if motherboard == "":
        pass
    else:
        device.motherboard = motherboard
    
    if hard_drive == "":
        pass
    else:
        device.hard_dive = hard_drive
    
    if sound == "":
        pass
    else:
        device.sound = sound
    
    if display_name == "":
        pass
    else:
        device.display = display_name
    
    if display_config == "":
        pass
    else:
        device.display_configuration = display_config
    
    if graphics_card == "":
        pass
    else:
        device.graphics_card = graphics_card

    try:
        device.save()
        messages.success(request, 'Successfully saved edits to desktop/notebook')
    except:
        messages.error(request, 'Could not save edits for desktop/notebook')

    return HttpResponseRedirect(reverse('index'))