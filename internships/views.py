from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

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


# =========================
# LIST
# =========================

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


# =========================
# DETAIL
# =========================

def internship_detail(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    return render(request, 'internships/detail.html', {
        'internship': internship
    })


# =========================
# CREATE
# =========================

@login_required
def create_internship(request):

    # check role safely
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

        return redirect('/internships/')

    return render(request, 'internships/create.html')


# =========================
# EDIT
# =========================

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
        return redirect('/internships/')

    return render(request, 'internships/edit.html', {
        'internship': internship
    })


# =========================
# DELETE
# =========================

@login_required
def delete_internship(request, internship_id):

    internship = get_object_or_404(Internship, id=internship_id)

    if internship.company != request.user:
        return redirect('/')

    remove_internship(internship)

    return redirect('/internships/')


# =========================
# TOGGLE STATUS
# =========================

@login_required
def toggle_status(request, internship_id):

    internship = get_object_or_404(Internship, id=internship_id)

    if internship.company != request.user:
        return redirect('/')

    toggle_internship_status(internship)

    return redirect('/internships/')