import django

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def login_index(request):
    return render(request, 'login.html', {})

def signup_index_view(request):
    return render(request, 'signup.html', {})

def my_account_view(request):
    return render(request, 'my_account.html', {})

def authenticate_user_login_view(request):
    username = password = ""

    if request.POST:
        username = request.POST.get('login_email')
        password = request.POST.get('login_password')

        logout(request)

        user = authenticate(username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            messages.success(request, 'Successfully logged in')
        else:
            messages.error(request, 'Could not authenticate...Please try again')
    
    return HttpResponseRedirect(reverse('index'))

def authenticate_sign_up(request):
    username = request.POST.get('signup_username')
    email = request.POST.get('signup_email')
    password = request.POST.get('signup_password')
    confirmation_password = request.POST.get('confirmation_password')
    
    User.objects.create_user(username, email, password)
    messages.success(request, 'Successfully signed up; please log in to verify account has been created')

    return HttpResponseRedirect(reverse('index'))

def log_user_out_view(request):
    if request.user.is_authenticated():
        try:
            logout(request)
            messages.success(request, 'Successfully logged out')
        except:
            messages.error(request, 'Could not log out')

    return HttpResponseRedirect(reverse('index'))
