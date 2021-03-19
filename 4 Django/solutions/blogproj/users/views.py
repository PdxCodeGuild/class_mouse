from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

from blog.models import BlogPost
# Create your views here.


def signup_user(request):
    if request.method == "POST":
        form = request.POST
        username = form['username']
        email = form['email']
        password = form['password']
        password2 = form['password2']

        if not User.objects.filter(username=username).exists():
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()
            # user = User.objects.create_user(username, email, password)

            login(request, user)

            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print("User exists already.")

    return render(request, 'users/signup.html')


def login_user(request):
    if request.method == "POST":
        form = request.POST
        username = form['username']
        password = form['password']
        user = authenticate(request, username=username, password=password)
        print(username, password, user)
        if user is not None:
            print('logging in user')
            login(request, user)
            return HttpResponseRedirect(reverse('users:profile'))

    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    blogs = BlogPost.objects.filter(user=request.user)
    context = {
        'blogs': blogs
    }

    return render(request, 'users/profile.html', context)
