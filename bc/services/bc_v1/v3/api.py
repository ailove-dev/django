import logging

import requests

from .utils import CourseData, UserData

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
            response = requests.api.request(
                method,
                f"{cls.BASE_URL}{url}",
                json=data,
                headers=headers,
                timeout=timeout,
            )
            logger.debug(response.text)
            return response
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
        return cls._send("post", "auth/restore/password/", data={"email": email})

    @classmethod
    def areas(cls):
        return cls._send("get", "core/areas").json()

    @classmethod
    def profile_short(cls, user_token: str) -> UserData:
        return UserData(
            cls._send(
                "get",
                "accounts/profile/short",
                headers={"Authorization": f"JWT {user_token}"},
            ).json()
        )

    @classmethod
    def user_course(cls, user_token: str) -> CourseData:
        return CourseData(
            cls._send(
                "get", "modules", headers={"Authorization": f"JWT {user_token}"}
            ).json()
        )

    @classmethod
    def course_module(cls, module_id: int, user_token: str):
        return cls._send(
            "get",
            f"modules/{module_id}",
            headers={"Authorization": f"JWT {user_token}"},
        ).json()
