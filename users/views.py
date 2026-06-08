from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from users.forms import RegisterForm
from .models import Profile


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']

            # 1. create user
            user = User.objects.create_user(
                username=username,
                password=password
            )

            # 2. set profile type (signal already created profile)
            user.profile.user_type = user_type
            user.profile.save()

            # 3. AUTO LOGIN (🔥 IMPORTANT PART)
            login(request, user)

            # 4. redirect to profile (or home)
            return redirect('/users/profile/')

    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {
        'form': form
    })


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

@login_required
def profile(request):
    return render(request, 'users/profile.html', {
        'profile': request.user.profile
    })