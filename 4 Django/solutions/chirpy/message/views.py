import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


from .models import Chirp


def index(request):

    chirps = Chirp.objects.order_by('-posted_date')[:20]

    context = {
        "chirps": chirps
    }

    return render(request, 'message/index.html', context)


def post(request):
    if request.user.is_authenticated:

        form = request.POST

        chirp = Chirp()
        chirp.message = form['message']
        chirp.author = request.user

        chirp.save()

        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))


def delete_chirp(request, id):
    chirp = Chirp.objects.get(id=id)
    if chirp.author == request.user:
        chirp.delete()

    return HttpResponseRedirect(reverse('index'))


def signup_user(request):
    if request.method == "GET":
        error = request.GET.get("error", "")
        username = request.GET.get("username", "")
        email = request.GET.get("email", "")
        context = {
            'error': error,
            'username': username,
            'email': email
        }
        return render(request, 'message/signup.html', context)

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm']
        email = request.POST['email']

        if password == confirm:
            User.objects.create_user(username, email, password)
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('signup') + f'?error=passwords do not match&username={username}&email={email}')


def login_user(request):
    if request.method == "GET":
        error = request.GET.get('error', '')
        context = {
            'error': error
        }
        return render(request, 'message/login.html', context)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('login') + '?error=Username or Password is incorrect.')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
