from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Show these fields in admin list
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_volunteer', 'is_ngo', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')

    # Fields to display when editing a user
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'bio', 'profile_pic')}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Optional: fields for adding new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )


# Register the CustomUser model with this admin
admin.site.register(CustomUser, CustomUserAdmin)
