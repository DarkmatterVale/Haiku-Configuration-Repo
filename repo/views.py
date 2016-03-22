import django

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout

from .models import Component
from .models import Device

from view_modules import *


# General
def index(request):
    """
    Create the view for the index page
    """
    return display_index_page(request)


# Authentication
def loginIndex(request):
    return render(request, 'repo/login.html', {})

def authenticateLogin(request):
    """
    Log a user in to the web app
    """
    return authenticateUserLogin(request)

def logMeOut(request):
    """
    Log a user out of the web app
    """
    return logUserOut(request)


# Component
def componentList(request):
    """
    List all of the components that are in the database
    """
    return listComponents(request)

def sortComponents(request):
    """
    Sorts all components for a component with a given name
    """
    return sortAllComponents(request)

def componentDetail(request, component_id):
    """
    Displays the details of a specific component
    """
    return detailsOfComponent(request, component_id)

def editComponent(request, component_id):
    """
    Allows a user to edit a specific test
    """
    return editAComponent(request, component_id)

def saveComponent(request, component_id):
    """
    Save a component
    """
    return save_component(request, component_id)


# Device
def deviceList(request):
    """
    List all devices
    """
    return listDevices(request)

def sortDevices(request):
    """
    Sort the devices based on name
    """
    return sort_devices(request)

def deviceDetail(request, device_id):
    """
    Displays the device's details
    """
    return device_details(request, device_id)

def editDevice(request, device_id):
    """
    Allows a user to edit a specific test
    """
    return edit_device(request, device_id)

def saveDevice(request, device_id):
    """
    Save a device
    """
    return save_device(request, device_id)


# Test
def addTest(request):
    """
    Allows a user to add a test (if they have authenticated)
    """
    return add_test(request)

def createTest(request):
    """
    Creates a test
    """
    return create_test(request)

def myTests(request):
    """
    Displays all of the user's submitted tests
    """
    return my_tests(request)
