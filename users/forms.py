from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    user_type = forms.ChoiceField(choices=[
        ('student', 'Student'),
        ('company', 'Company')
    ])

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type']