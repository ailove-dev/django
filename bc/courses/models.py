from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    external_id = models.SmallIntegerField(
        verbose_name=_("external id"), help_text=_("user path"), unique=True
    )
    internal_data = JSONField(verbose_name=_("internal data"), default=dict, blank=True)
    external_data = JSONField(verbose_name=_("external data"), default=dict, blank=True)
    is_enabled = models.BooleanField(verbose_name=_("is enabled"), default=False)

    def __str__(self):
        return self.external_id
