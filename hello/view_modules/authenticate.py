import django

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from django.contrib.auth import authenticate, login, logout


def login_index(request):
    return render(request, 'login.html', {})

def authenticateUserLogin(request):
    username = password = ""

    if request.POST:
        username = request.POST.get('login_email')
        password = request.POST.get('login_password')

        logout(request)

        user = authenticate(username=username, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)

    return HttpResponseRedirect(reverse('hello:index'))

def logUserOut(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect(reverse('hello:index'))
