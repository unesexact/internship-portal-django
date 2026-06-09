from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("profile/<int:user_id>/", views.public_profile, name="public_profile"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
