from django.db import models
from django.contrib.auth.models import User
from internships.models import Internship


class Application(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE, related_name="applications")

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'internship')  # 🚀 prevents duplicates

    def __str__(self):
        return f"{self.student.username} → {self.internship.title}"
    


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message    