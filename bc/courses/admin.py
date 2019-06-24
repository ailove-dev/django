from django.contrib import admin

from . import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("external_id", "is_enabled")
    list_editable = ("is_enabled",)
