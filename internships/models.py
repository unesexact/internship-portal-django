from django.db import models
from django.contrib.auth.models import User


class Internship(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("closed", "Closed"),
    )

    title = models.CharField(max_length=200)
    company = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="internships"
    )
    location = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company.username}"
