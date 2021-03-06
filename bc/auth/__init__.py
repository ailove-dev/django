import typing

if typing.TYPE_CHECKING:
    from rest_framework.request import Request

USER_AUTH_TOKEN_COOKIE_NAME = "gbc_user_token"


def get_auth_token(request: "Request") -> typing.Optional[str]:
    return request.COOKIES.get(USER_AUTH_TOKEN_COOKIE_NAME)
