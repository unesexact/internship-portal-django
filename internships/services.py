from .models import Internship


def get_student_internships():
    return Internship.objects.filter(status="active")


def get_company_internships(user):
    return Internship.objects.filter(company=user)


def get_public_internships():
    return Internship.objects.filter(status="active")


def create_internship(user, title, location, description):
    return Internship.objects.create(
        title=title, location=location, description=description, company=user
    )


def update_internship(internship, title, location, description):
    internship.title = title
    internship.location = location
    internship.description = description
    internship.save()
    return internship


def remove_internship(internship):
    internship.delete()


def toggle_internship_status(internship):
    if internship.status == "active":
        internship.status = "closed"
    else:
        internship.status = "active"
    internship.save()
    return internship
