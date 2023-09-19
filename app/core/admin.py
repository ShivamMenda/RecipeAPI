"""
Django admin custom
"""

from django.contrib import admin # noqa
from django.contrib.auth.admin import UserAdmin

from core import models

class UserAdminManager(UserAdmin):
    """Define the admin pages for users"""
    ordering=['id']
    list_display=['email','name']
    fieldsets = (
        (None, {
            "fields": (
                'email','password'
            ),
        }),
        (('Permissions'), {
            "fields": (
                'is_active','is_staff','is_superuser'
            ),
        }),
         (('Important dates'), {
            "fields": (
                'last_login',
            ),
        }),
        
    )
    readonly_fields=['last_login']
    add_fieldsets=(
         (None, {
            "fields": (
                'email','password1','password2','name','is_active','is_staff','is_superuser'
            ),
        }),
    )
    


admin.site.register(models.User,UserAdminManager)
admin.site.register(models.Recipe)

