from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    USER_TYPES = (
        ("student", "Student"),
        ("company", "Company"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    # ===== STUDENT FIELDS =====
    full_name = models.CharField(max_length=100, blank=True)
    university = models.CharField(max_length=100, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    skills = models.TextField(blank=True)
    bio = models.TextField(blank=True)

    # ===== COMPANY FIELDS =====
    company_name = models.CharField(max_length=100, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    cv = models.FileField(upload_to="cvs/", blank=True, null=True)

    profile_picture = models.ImageField(
        upload_to="profile_pictures/", blank=True, null=True
    )

    def __str__(self):
        return self.user.username
