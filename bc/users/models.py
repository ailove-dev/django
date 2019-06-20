from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    avatar = models.URLField(
        verbose_name=_("avatar"), help_text=_("last fetched avatar image"), blank=True
    )
