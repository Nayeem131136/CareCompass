from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username', 'email',
            'phone', 'role', 'password1', 'password2'
        ]

class CustomUserChangeForm(UserChangeForm):
    password = None  # Hide password field in profile form

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'address', 'bio',
            'profile_pic', 'organization_name',
            'certificate', 'license_file', 'skills'
        ]
