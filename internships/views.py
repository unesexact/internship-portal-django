from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from applications.models import Application

from .models import Internship
from .services import (
    get_student_internships,
    get_company_internships,
    get_public_internships,
    create_internship,
    remove_internship,
    update_internship,
    toggle_internship_status
)



def internship_list(request):

    if request.user.is_authenticated and hasattr(request.user, 'profile'):

        role = request.user.profile.user_type

        if role == 'student':
            internships = get_student_internships()

        elif role == 'company':
            internships = get_company_internships(request.user)

        else:
            internships = get_public_internships()

    else:
        internships = get_public_internships()

    return render(request, 'internships/list.html', {
        'internships': internships
    })



def internship_detail(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)

    already_applied = False

    if request.user.is_authenticated and hasattr(request.user, "profile"):
        if request.user.profile.user_type == "student":
            already_applied = Application.objects.filter(
                student=request.user,
                internship=internship
            ).exists()

    return render(request, 'internships/detail.html', {
        'internship': internship,
        'already_applied': already_applied
    })



@login_required
def create_internship(request):

    if not hasattr(request.user, 'profile'):
        return redirect('/')

    if request.user.profile.user_type != 'company':
        return redirect('/')

    if request.method == "POST":
        title = request.POST['title']
        location = request.POST['location']
        description = request.POST['description']

        Internship.objects.create(
            title=title,
            location=location,
            description=description,
            company=request.user
        )
        messages.success(request, "Internship created successfully!")
        return redirect('/internships/')

    return render(request, 'internships/create.html')



@login_required
def edit_internship(request, internship_id):

    internship = get_object_or_404(Internship, id=internship_id)

    if internship.company != request.user:
        return redirect('/')

    if request.method == "POST":
        update_internship(
            internship,
            request.POST['title'],
            request.POST['location'],
            request.POST['description']
        )
        messages.success(request, "Internship updated successfully!")
        return redirect('/internships/')

    return render(request, 'internships/edit.html', {
        'internship': internship
    })



@login_required
def delete_internship(request, internship_id):

    internship = get_object_or_404(Internship, id=internship_id)

    if internship.company != request.user:
        return redirect('/')

    if request.method == "POST":
        remove_internship(internship)
        messages.success(request, "Internship deleted successfully!")
        return redirect('/internships/')

    return redirect('/internships/')



@login_required
def toggle_status(request, internship_id):

    internship = get_object_or_404(Internship, id=internship_id)

    if internship.company != request.user:
        return redirect('/')

    toggle_internship_status(internship)
    messages.success(request, "Internship deleted successfully!")
    return redirect('/internships/')