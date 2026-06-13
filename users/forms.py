from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=[("student", "Student"), ("company", "Company")],
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "user_type"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"}),
        }