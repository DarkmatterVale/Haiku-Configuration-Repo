import django

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout

from ..models import Component


def listComponents(request):
    all_components = Component.objects.all()
    context = { 'all_components' : all_components }

    return render(request, 'repo/component_list.html', context)

def sortAllComponents(request):
    sort_name = request.POST['name_to_sort']
    
    # sorting based on name
    all_components = Component.objects.all()
    sorted_components = []
    for grabbed_component in all_components:
        if sort_name in grabbed_component.name:
            sorted_components.append(grabbed_component)

    context = { 'all_components' : sorted_components }
    
    return render(request, 'repo/component_list.html', context)

def detailsOfComponent(request, component_id):
    myComponent = get_object_or_404(Component, pk=component_id)
    context = {
        'component_name' : myComponent.name,
        'all_components' : [myComponent]
    }

    return render(request, 'repo/component.html', context)

def editAComponent(request, component_id):
    myComponent = get_object_or_404(Component, pk=component_id)
    context = {
        'component_name' : myComponent.name,
        'component' : myComponent
    }

    return render(request, 'repo/edit_component.html', context)

def save_component(request, component_id):
    component = get_object_or_404(Component, pk=component_id)
    category = str(request.POST['component_category'])
    component.notes = request.POST['component_notes']
    
    if category == "":
        pass
    else:
        component.category = category
    
    try:
        if str(request.POST['group9']) == "on":
            component.is_working = "Passed"
    except:
        component.is_working = "Failed"
    
    component.save()

    return HttpResponseRedirect(reverse('repo:index'))