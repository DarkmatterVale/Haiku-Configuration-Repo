from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Component

def index(request):
    latest_question_list = Component.objects.order_by('-rating')[:5]
    context = { 'latest_question_list' : latest_question_list }

    return render(request, 'repo/index.html', context)

def componentList(request):
    return render(request, 'repo/component_list.html', {})

def componentDetail(request, component_id):
    myComponent = get_object_or_404(Component, pk=component_id)
    context = { 'component' : myComponent }
    return render(request, 'repo/component.html', context)

def deviceList(request):
    return render(request, 'repo/device_list.html', {})
