from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello, world. You're at the repo index.")
