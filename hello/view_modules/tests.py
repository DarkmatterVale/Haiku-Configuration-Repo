import django

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from ..models import Component
from ..models import Device


def add_test_view(request):
    return render(request, 'add_test.html', {})

def add_component_test_view(request):
    return render(request, 'add_test_component_form.html', {})

def add_device_test_view(request):
    return render(request, 'add_test_device_form.html', {})

def satisfy_test_requirements(data):
    means_for_failing = ""

    for element in data:
        if element == means_for_failing:
            return False

    return True

def create_test_view(request):
    if request.user.is_authenticated():
        try:
            component_name = request.POST['component_name']
            is_component = True
        except:
            is_component = False
        
        try:
            device_name = request.POST['device_name']
            is_device = True
        except:
            is_device = False

        author = request.user.username

        if is_component == True:
            rating = request.POST['component_rating']
            is_working = "Not Specified"
            notes = request.POST['component_test_notes']
            component_category = request.POST['component_category']
            manufacturer = request.POST['component_manufacturer']
            haiku_revision = request.POST['component_haiku_revision']
            haiku_architecture = request.POST['component_haiku_architecture']
            
            component_data = [
                component_category,
                manufacturer,
                haiku_revision,
                haiku_architecture
            ]
            
            if satisfy_test_requirements(component_data) == False:
                messages.error(request, 'Fields that were required were not filled out...please try again')
                
                return HttpResponseRedirect(reverse('index'))

            try:
                if str(request.POST['group1']) == "on":
                    is_working = "Passed"
            except:
                try:
                    if str(request.POST['group2']) == "on":
                        is_working = "Failed"
                except:
                    pass

            try:
                newComponent = Component(name = component_name,
                                         rating = rating,
                                         is_working = is_working,
                                         notes = notes,
                                         author = author,
                                         author_email = author_email,
                                         category = component_category,
                                         manufacturer = manufacturer,
                                         haiku_revision = haiku_revision,
                                         haiku_arch = haiku_architecture)
                newComponent.save()
    
                messages.success(request, 'Successfully created a new test')
            except:
                messages.error(request, 'Could not create a new test...please try again')

        if is_device == True:
            rating = request.POST['device_rating']
            notes = request.POST['device_test_notes']

            device_cpu = request.POST['device_cpu']
            device_motherboard = request.POST['device_motherboard']
            device_hard_drive = request.POST['device_hard_drive']
            device_sound = request.POST['device_sound']
            device_display_name = request.POST['device_display_name']
            device_display_config = request.POST['device_display_config']
            device_dedicated_graphics = request.POST['device_dedicated_graphics']
            is_dedicated_graphics_working = request.POST['device_dedicated_graphics']
            manufacturer = request.POST['device_manufacturer']
            lan_chipset = request.POST['device_lan_network_chipset']
            wlan_chipset = request.POST['device_wlan_network_chipset']
            haiku_revision = request.POST['device_haiku_revision']
            haiku_architecture = request.POST['device_haiku_architecture']

            try:
                if str(request.POST['device_category_desktop']) == "on":
                    category = "Desktop"
            except:
                try:
                    if str(request.POST['device_category_notebook']) == "on":
                        category = "Notebook"
                except:
                    category = "Not Specified"
            
            device_data = [
                rating,
                haiku_revision,
                haiku_architecture,
                manufacturer,
                device_cpu,
                device_motherboard,
                device_hard_drive,
                category
            ]
            
            if satisfy_test_requirements(device_data) == False:
                messages.error(request, 'Fields that were required were not filled out...please try again')
                
                return HttpResponseRedirect(reverse('index'))
            
            try:
                if str(request.POST['group9']) == "on":
                    is_working = "Passed"
            except:
                try:
                    if str(request.POST['group10']) == "on":
                        is_working = "Failed"
                except:
                    is_working = "Not Specified"

            try:
                if str(request.POST['group3']) == "on":
                    is_sound_working = "Passed"
            except:
                try:
                    if str(request.POST['group4']) == "on":
                        is_sound_working = "Failed"
                except:
                    is_sound_working = "Not Specified"

            try:
                if str(request.POST['group5']) == "on":
                    is_display_working = "Passed"
            except:
                try:
                    if str(request.POST['group6']) == "on":
                        is_display_working = "Failed"
                except:
                    is_display_working = "Not Specified"

            try:
                if str(request.POST['group7']) == "on":
                    is_dedicated_graphics_working = "Passed"
            except:
                try:
                    if str(request.POST['group8']) == "on":
                        is_dedicated_graphics_working = "Failed"
                except:
                    is_dedicated_graphics_working = "Not Specified"

            try:
                if str(request.POST['device_usb2_pass']) == "on":
                    usb2_works = "Passed"
            except:
                try:
                    if str(request.POST['device_usb2_fail']) == "on":
                        usb2_works = "Failed"
                except:
                    usb2_works = "Not Specified"

            try:
                if str(request.POST['device_usb3_pass']) == "on":
                    usb3_works = "Passed"
            except:
                try:
                    if str(request.POST['device_usb3_fail']) == "on":
                        usb3_works = "Failed"
                except:
                    usb3_works = "Not Specified"

            try:
                if str(request.POST['device_optical_drive_pass']) == "on":
                    optical_drive_works = "Passed"
            except:
                try:
                    if str(request.POST['device_optical_drive_fail']) == "on":
                        optical_drive_works = "Failed"
                except:
                    optical_drive_works = "Not Specified"

            try:
                if str(request.POST['device_card_reader_pass']) == "on":
                    card_reader_works = "Passed"
            except:
                try:
                    if str(request.POST['device_card_reader_fail']) == "on":
                        card_reader_works = "Failed"
                except:
                    card_reader_works = "Not Specified"

            try:
                newDevice = Device(name = device_name,
                                   rating = rating,
                                   is_working = is_working,
                                   notes = notes,
                                   author = author,
                                   author_email = author_email,
                                   cpu = device_cpu,
                                   motherboard = device_motherboard,
                                   hard_drive = device_hard_drive,
                                   sound = device_sound,
                                   is_sound_working = is_sound_working,
                                   display = device_display_name,
                                   display_configuration = device_display_config,
                                   is_display_working = is_display_working,
                                   graphics_card = device_dedicated_graphics,
                                   graphics_card_is_working = is_dedicated_graphics_working,
                                   manufacturer = manufacturer,
                                   does_usb2_work = usb2_works,
                                   does_usb3_work = usb3_works,
                                   lan_network_chipset = lan_chipset,
                                   wlan_network_chipset = wlan_chipset,
                                   does_optical_drive_work = optical_drive_works,
                                   does_card_reader_work = card_reader_works,
                                   haiku_revision = haiku_revision,
                                   haiku_architecture = haiku_architecture,
                                   category = category)
                newDevice.save()
                messages.success(request, 'Successfully created a new test')
            except:
                messages.error(request, 'Could not create a new test...please try again')

    return HttpResponseRedirect(reverse('index'))

def my_tests_view(request):
    all_components = Component.objects.all().filter(author=request.user.username)
    all_devices = Device.objects.all().filter(author=request.user.username)
    context = {
        'all_devices' : all_devices,
        'all_components' : all_components
    }

    return render(request, 'my_tests.html', context)
