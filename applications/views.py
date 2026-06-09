from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Application
from internships.models import Internship


@login_required
def apply_internship(request, internship_id):

    internship = get_object_or_404(Internship, id=internship_id)

    application, created = Application.objects.get_or_create(
        student=request.user,
        internship=internship
    )

    if not created:
        pass

    return redirect('/internships/')


@login_required
def my_applications(request):

    applications = Application.objects.filter(student=request.user)

    return render(request, 'applications/my_applications.html', {
        'applications': applications
    })


@login_required
def company_applications(request):

    applications = Application.objects.filter(
        internship__company=request.user
    )

    return render(request, 'applications/company_applications.html', {
        'applications': applications
    })

@login_required
def update_application(request, app_id, status):

    application = get_object_or_404(Application, id=app_id)

    # only owner company can manage
    if application.internship.company != request.user:
        return redirect('/')

    if status in ['accepted', 'rejected']:
        application.status = status
        application.save()

    return redirect('/applications/company/')