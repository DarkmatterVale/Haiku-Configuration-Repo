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
def login_page(request):
    """
    Login page
    """
    return login_index(request)

def signup_page(request):
    """
    Signup page
    """
    return signup_index_view(request)

def authenticate_login(request):
    """
    Log a user in to the web app
    """
    return authenticate_user_login_view(request)

def authenticate_signup(request):
    """
    Sign a user up
    """
    return authenticate_sign_up(request)

def logout(request):
    """
    Log a user out of the web app
    """
    return log_user_out_view(request)


# Component
def list_all_components(request):
    """
    List all of the components that are in the database
    """
    return list_all_components_view(request)

def sort_all_components(request):
    """
    Sorts all components for a component with a given name
    """
    return sort_all_components_view(request)

def component_details(request, component_id):
    """
    Displays the details of a specific component
    """
    return component_details_view(request, component_id)

def edit_component(request, component_id):
    """
    Allows a user to edit a specific test
    """
    return edit_component_view(request, component_id)

def save_component(request, component_id):
    """
    Save a component
    """
    return save_component_view(request, component_id)


# Device
def deviceList(request):
    """
    List all devices
    """
    return list_all_devices_view(request)

def sortDevices(request):
    """
    Sort the devices based on name
    """
    return sort_devices_view(request)

def deviceDetail(request, device_id):
    """
    Displays the device's details
    """
    return device_details_view(request, device_id)

def editDevice(request, device_id):
    """
    Allows a user to edit a specific test
    """
    return edit_device_view(request, device_id)

def saveDevice(request, device_id):
    """
    Save a device
    """
    return save_device_view(request, device_id)


# Test
def addTest(request):
    """
    Allows a user to add a test (if they have authenticated)
    """
    return add_test_view(request)

def add_component_test(request):
    """
    Allows the user to send a component test form
    """
    return add_component_test_view(request)

def add_device_test(request):
    """
    Allows the user to send a device test form
    """
    return add_device_test_view(request)

def createTest(request):
    """
    Creates a test
    """
    return create_test_view(request)

def myTests(request):
    """
    Displays all of the user's submitted tests
    """
    return my_tests_view(request)