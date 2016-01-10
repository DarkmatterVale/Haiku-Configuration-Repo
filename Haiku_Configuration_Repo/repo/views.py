from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Component

def index(request):
    return render(request, 'repo/index.html', {})

def componentList(request):
    all_components = Component.objects.all()
    context = { 'all_components' : all_components }

    return render(request, 'repo/component_list.html', context)

def deviceList(request):
    all_components = Component.objects.all()
    context = { 'all_components' : all_components }

    return render(request, 'repo/device_list.html', context)

def componentDetail(request, component_id):
    myComponent = get_object_or_404(Component, pk=component_id)
    context = {
        'component_name' : myComponent.name,
        'all_components' : [ myComponent ]
    }

    return render(request, 'repo/component.html', context)

def addTest(request):
    return render(request, 'repo/add_test.html', {})

def createComponent(request):
    name = request.POST['component_name']
    rating = request.POST['rating']
    is_working = "Failed"
    notes = request.POST['test_notes']

    author_first_name = request.POST['tester_first_name']
    author_last_name = request.POST['tester_last_name']
    author_email = request.POST['tester_email']

    try:
        if str(request.POST['group1']) == "on":
            is_working = "Passed"
    except:
        pass

    newComponent = Component(name = name,
        rating = rating,
        is_working = is_working,
        notes = notes,
        author_first_name = author_first_name,
        author_last_name = author_last_name,
        author_email = author_email)
    newComponent.save()

    return HttpResponseRedirect(reverse('repo:index'))
