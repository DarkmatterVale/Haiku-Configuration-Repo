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

def delete_device_view(request, device_id):
    try:
        Device.objects.filter(id=device_id).delete()
        messages.success(request, 'Successfully deleted test')
    except:
        messages.error(request, 'Could not delete test')

    return HttpResponseRedirect(reverse('index'))

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
        'device' : myDevice
    }

    return render(request, 'device.html', context)

def edit_device_view(request, device_id):
    myDevice = get_object_or_404(Device, pk=device_id)
    context = {
        'device' : myDevice,
        'loop' : range(0,11)
    }
    
    return render(request, 'edit_device.html', context)

def save_device_view(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    
    device.notes = request.POST['device_notes']
    
    cpu = request.POST['device_cpu']
    motherboard = request.POST['device_motherboard']
    hard_drive = request.POST['device_hard_drive']
    sound = request.POST['device_sound']
    display_config = request.POST['device_display_config']
    graphics_card = request.POST['device_dedicated_graphics']
    manufacturer = request.POST['device_manufacturer']
    lan_chipset = request.POST['device_lan_network_chipset']
    wlan_chipset = request.POST['device_wlan_network_chipset']
    haiku_revision = request.POST['device_haiku_revision']
    haiku_architecture = request.POST['device_haiku_architecture']
    category = request.POST['device_category']
    rating = request.POST['device_rating']
    
    try:
        if str(request.POST['group9']) == "on":
            device.is_working = "Passed"
    except:
        try:
            if str(request.POST['group10']) == "on":
                device.is_working = "Failed"
        except:
            device.is_working = "Not Specified"
    
    try:
        if str(request.POST['group3']) == "on":
            device.is_sound_working = "Passed"
    except:
        try:
            if str(request.POST['group4']) == "on":
                device.is_sound_working = "Failed"
        except:
            device.is_sound_working = "Not Specified"
    
    try:
        if str(request.POST['group5']) == "on":
            device.is_display_working = "Passed"
    except:
        try:
            if str(request.POST['group6']) == "on":
                device.is_display_working = "Failed"
        except:
            device.is_display_working = "Not Specified"
    
    try:
        if str(request.POST['group7']) == "on":
            device.graphics_card_is_working = "Passed"
    except:
        try:
            if str(request.POST['group8']) == "on":
                device.graphics_card_is_working = "Failed"
        except:
            device.graphics_card_is_working = "Not Specified"

    try:
        if str(request.POST['device_usb2_pass']) == "on":
            device.does_usb2_work = "Passed"
    except:
        try:
            if str(request.POST['device_usb2_fail']) == "on":
                device.does_usb2_work = "Failed"
        except:
            device.does_usb2_work = "Not Specified"
        
    try:
        if str(request.POST['device_usb3_pass']) == "on":
            device.does_usb3_work = "Passed"
    except:
        try:
            if str(request.POST['device_usb3_fail']) == "on":
                device.does_usb3_work = "Failed"
        except:
            device.does_usb3_work = "Not Specified"
        
    try:
        if str(request.POST['device_optical_drive_pass']) == "on":
            device.does_optical_drive_work = "Passed"
    except:
        try:
            if str(request.POST['device_optical_drive_fail']) == "on":
                device.does_optical_drive_work = "Failed"
        except:
            device.does_optical_drive_work = "Not Specified"
        
    try:
        if str(request.POST['device_card_reader_pass']) == "on":
            device.does_card_reader_work = "Passed"
    except:
        try:
            if str(request.POST['device_card_reader_fail']) == "on":
                device.does_card_reader_work = "Failed"
        except:
            device.does_card_reader_work = "Not Specified"

    device.cpu = cpu
    device.motherboard = motherboard
    device.hard_dive = hard_drive
    device.sound = sound
    device.display_configuration = display_config
    device.graphics_card = graphics_card
    device.manufacturer = manufacturer
    device.lan_network_chipset = lan_chipset
    device.wlan_network_chipset = wlan_chipset
    device.haiku_arch = haiku_architecture
    device.haiku_revision = haiku_revision
    device.category = category
    device.rating = rating

    try:
        device.save()
        messages.success(request, 'Successfully saved edits to desktop/notebook')
    except:
        messages.error(request, 'Could not save edits for desktop/notebook')

    return HttpResponseRedirect(reverse('index'))