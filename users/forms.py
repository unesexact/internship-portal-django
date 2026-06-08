from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[
        ('student', 'Student'),
        ('company', 'Company')
    ])

    # 🧠 validation (LEVEL 3 magic)
    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")

        return username