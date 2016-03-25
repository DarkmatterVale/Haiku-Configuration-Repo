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


def list_all_components_view(request):
    all_components = Component.objects.all()
    context = { 'all_components' : all_components }

    return render(request, 'component_list.html', context)

def delete_component_view(request, component_id):
    try:
        Component.objects.filter(id=component_id).delete()
        messages.success(request, 'Successfully deleted test')
    except:
        messages.error(request, 'Could not delete test')
    
    return HttpResponseRedirect(reverse('index'))

def sort_all_components_view(request):
    sort_name = request.POST['name_to_sort']
    
    # sorting based on name
    all_components = Component.objects.all()
    sorted_components = []
    for grabbed_component in all_components:
        if sort_name in grabbed_component.name:
            sorted_components.append(grabbed_component)

    context = { 'all_components' : sorted_components }
    
    return render(request, 'component_list.html', context)

def component_details_view(request, component_id):
    myComponent = get_object_or_404(Component, pk=component_id)
    context = {
        'component_name' : myComponent.name,
        'all_components' : [myComponent]
    }

    return render(request, 'component.html', context)

def edit_component_view(request, component_id):
    myComponent = get_object_or_404(Component, pk=component_id)
    context = {
        'component_name' : myComponent.name,
        'component' : myComponent
    }

    return render(request, 'edit_component.html', context)

def save_component_view(request, component_id):
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
    
    try:
        component.save()
        messages.success(request, 'Successfully saved edits for component')
    except:
        messages.error(request, 'Could not save edits for component')

    return HttpResponseRedirect(reverse('index'))