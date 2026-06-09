from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from internships.models import Internship
from users.forms import RegisterForm
from .models import Profile


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():

          user = form.save()

          user_type = form.cleaned_data['user_type']

          user.profile.user_type = user_type
          user.profile.save()

          login(request, user)
          messages.success(request, "Welcome! Your account was created.")

          return redirect('/users/profile/')

    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {
        'form': form
    })


def user_login(request):

    # 🔥 IF USER ALREADY LOGGED IN → REDIRECT TO DASHBOARD
    if request.user.is_authenticated:
        return redirect('/users/dashboard/')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("/users/dashboard/")

        else:
            return render(request, "users/login.html", {
                "error": "Invalid credentials"
            })

    return render(request, "users/login.html")

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('/users/login/')

@login_required
def profile(request):
    return render(request, 'users/profile.html', {
        'profile': request.user.profile
    })
    
    
@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":

        # Student fields
        profile.full_name = request.POST.get("full_name", "")
        profile.university = request.POST.get("university", "")
        profile.degree = request.POST.get("degree", "")
        profile.skills = request.POST.get("skills", "")
        profile.bio = request.POST.get("bio", "")

        # Company fields
        profile.company_name = request.POST.get("company_name", "")
        profile.industry = request.POST.get("industry", "")
        profile.website = request.POST.get("website", "")
        profile.location = request.POST.get("location", "")
        
        if request.FILES.get("cv"):
           profile.cv = request.FILES["cv"]

        profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("/users/profile/")

    return render(
        request,
        "users/edit_profile.html",
        {"profile": profile}
    )
    


def public_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if user.profile.user_type != "student":
        return redirect("dashboard")

    return render(request, 'users/public_profile.html', {
        'profile_user': user,
        'profile': user.profile
    })
    
@login_required
def dashboard(request):
    profile = request.user.profile

    if profile.user_type == "student":
        return render(request, "users/dashboard_student.html")

    # COMPANY DASHBOARD DATA
    company_internships = Internship.objects.filter(company=request.user)

    total_internships = company_internships.count()
    active_internships = company_internships.filter(status="active").count()
    closed_internships = company_internships.filter(status="closed").count()

    return render(request, "users/dashboard_company.html", {
        "internships": company_internships,
        "total_internships": total_internships,
        "active_internships": active_internships,
        "closed_internships": closed_internships,
    })