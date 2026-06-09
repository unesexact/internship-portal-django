from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Application, Notification
from internships.models import Internship


@login_required
def apply_internship(request, internship_id):

    internship = get_object_or_404(Internship, id=internship_id)

    application, created = Application.objects.get_or_create(
        student=request.user, internship=internship
    )

    if not created:
        pass

    if created:
        messages.success(request, "Application submitted successfully!")
        Notification.objects.create(
            user=internship.company,
            message=f"New application received for {internship.title}",
        )
    else:
        messages.info(request, "You already applied to this internship.")

    return redirect("/internships/")


@login_required
def my_applications(request):

    applications = Application.objects.filter(student=request.user)

    return render(
        request, "applications/my_applications.html", {"applications": applications}
    )


@login_required
def company_applications(request):

    applications = Application.objects.filter(internship__company=request.user)

    return render(
        request,
        "applications/company_applications.html",
        {"applications": applications},
    )


@login_required
def update_application(request, app_id, status):

    application = get_object_or_404(Application, id=app_id)

    # only owner company can manage
    if application.internship.company != request.user:
        return redirect("/")

    if status in ["accepted", "rejected"]:
        application.status = status
        application.save()

        Notification.objects.create(
            user=application.student,
            message=f"Your application for {application.internship.title} was {status}",
        )

    messages.success(request, f"Application {status} successfully!")

    return redirect("/applications/company/")


@login_required
def mark_notifications_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)

    return redirect(request.META.get("HTTP_REFERER", "/"))
