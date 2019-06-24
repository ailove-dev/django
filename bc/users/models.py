from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    avatar = models.URLField(
        verbose_name=_("avatar"), help_text=_("last fetched avatar image"), blank=True
    )
    course_path = models.SmallIntegerField(
        verbose_name=_("course path"), help_text=_("user course path"), null=True
    )

    def attach_course_path(self, course_path, commit=True):
        self.course_path = course_path
        if commit:
            self.save()
