import django

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_index(request):
    return render(request, 'login.html', {})

def signup_index_view(request):
    return render(request, 'signup.html', {})

def authenticate_user_login_view(request):
    username = password = ""

    if request.POST:
        username = request.POST.get('login_email')
        password = request.POST.get('login_password')

        logout(request)

        user = authenticate(username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)

    return HttpResponseRedirect(reverse('index'))

def authenticate_sign_up(request):
    username = request.POST.get('signup_username')
    email = request.POST.get('signup_email')
    password = request.POST.get('signup_password')
    confirmation_password = request.POST.get('confirmation_password')
    
    User.objects.create_user(username, email, password)

    return HttpResponseRedirect(reverse('index'))

def log_user_out_view(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect(reverse('index'))
