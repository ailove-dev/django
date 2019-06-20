from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import set_rollback


def exception_handler(exc, context):
    """Partly rewritten default rest_framework.views.exception_handler

    Changed `detail` to `message` and wrap
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

        if isinstance(exc.detail, (list, dict)):
            if isinstance(exc, exceptions.ValidationError):
                data = {"validation_errors": exc.detail, "message": exc.default_detail}
            else:
                data = exc.detail
        else:
            data = {"message": exc.detail}

        set_rollback()
        return Response(
            {**data, "error_code": exc.default_code},
            status=exc.status_code,
            headers=headers,
        )

    return None
