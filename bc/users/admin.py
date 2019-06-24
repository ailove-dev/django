from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        (_("Business Class"), {"fields": ("avatar", "course_path")}),
    )
    list_display = DjangoUserAdmin.list_display + ("course_path",)
