# Generated by Django 2.2.2 on 2019-06-21 18:27

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "external_id",
                    models.SmallIntegerField(
                        help_text="user path", unique=True, verbose_name="external id"
                    ),
                ),
                (
                    "internal_data",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict, verbose_name="internal data"
                    ),
                ),
                (
                    "external_data",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict, verbose_name="external data"
                    ),
                ),
                (
                    "is_enabled",
                    models.BooleanField(default=False, verbose_name="is enabled"),
                ),
            ],
        )
    ]