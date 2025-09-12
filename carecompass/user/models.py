from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('volunteer', 'Volunteer'),
        ('ngo', 'NGO'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)

    @property
    def is_volunteer(self):
        return self.role == 'volunteer'

    @property
    def is_ngo(self):
        return self.role == 'ngo'

    def __str__(self):
        return self.username
