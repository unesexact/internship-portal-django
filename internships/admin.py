from django.contrib import admin
from .models import Internship


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "status", "created_at")
    list_filter = ("status", "location")
    search_fields = ("title", "description")
