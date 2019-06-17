import logging

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from .base import *  # noqa

CONFIG = __import__("app.config").config

DEBUG = False


SENTRY_DSN = CONFIG.env("SENTRY_DSN")
SENTRY_LOG_LEVEL = CONFIG.env.int("DJANGO_SENTRY_LOG_LEVEL", logging.INFO)

sentry_logging = LoggingIntegration(
    level=SENTRY_LOG_LEVEL,  # Capture info and above as breadcrumbs
    event_level=logging.ERROR,  # Send errors as events
    environment="production",
)
sentry_sdk.init(dsn=SENTRY_DSN, integrations=[sentry_logging, DjangoIntegration()])
