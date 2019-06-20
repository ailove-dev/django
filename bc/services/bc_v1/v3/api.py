import logging

import requests

logger = logging.getLogger(__name__)


class RequestError(Exception):
    pass


class RequestTimeout(RequestError):
    pass


class ServerError(RequestError):
    pass


class BusinessClassAPI:
    BASE_URL = "https://www.business-class.pro/api/v3/"
    REQUEST_TIMEOUT = 60  # 1 minute

    class AuthFailed(Exception):
        pass

    @classmethod
    def _send(cls, method, url, data=None, headers=None, timeout=REQUEST_TIMEOUT):
        try:
            return requests.post(f"{cls.BASE_URL}{url}", json=data, timeout=timeout)
        except requests.Timeout:
            raise RequestTimeout
        except requests.RequestException:
            raise ServerError

    @classmethod
    def login(cls, email: str, password: str):
        response = cls._send(
            "post", "auth/login", data={"email": email, "password": password}
        )
        if not response.ok:
            raise cls.AuthFailed

        return response.json()

    @classmethod
    def register(cls, data):
        response = cls._send("post", "auth/register", data=data)
        return response.json()

    @classmethod
    def restore_password(cls, email: str):
        response = cls._send("post", "restore/password", data={"email": email})
        return response.json()

    @classmethod
    def areas(cls):
        return cls._send("get", "core/areas")

    @classmethod
    def profile_short(cls, user_token):
        return cls._send(
            "get",
            "accounts/profile/short",
            headers={"Authorization": f"JWT {user_token}"},
        )

    @classmethod
    def user_modules(cls, user_token):
        return cls._send(
            "get", "modules", headers={"Authorization": f"JWT {user_token}"}
        )
