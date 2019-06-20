from django.utils.translation import gettext_lazy as _
from rest_framework import status

from bc.exceptions import BadRequestWithMessage


class AuthException(BadRequestWithMessage):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = "invalid_credentials"
    default_detail = _(
        "Invalid credentials. Please, check your data and try to resubmit again."
    )
