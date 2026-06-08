from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Profile


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']

        user = User.objects.create_user(username=username, password=password)

        Profile.objects.create(user=user, user_type=user_type)

        login(request, user)
        return redirect('/')

    return render(request, 'users/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'users/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')