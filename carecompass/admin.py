from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'role', 'is_staff', 'date_joined']
    list_filter = ['role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('CareCompass Info', {
            'fields': ('role', 'phone', 'address', 'bio', 'profile_pic',
                       'organization_name', 'certificate', 'license_file', 'skills')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('CareCompass Info', {
            'fields': ('role', 'email', 'phone')
        }),
    )
