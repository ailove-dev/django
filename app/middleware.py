from django import http
from django.conf import settings

XHR_SHARING_ALLOWED_ORIGINS = getattr(settings, "XHR_SHARING_ALLOWED_ORIGINS", "*")
XHR_SHARING_ALLOWED_HEADERS = getattr(
    settings,
    "XHR_SHARING_ALLOWED_HEADERS",
    ["X-Requested-With", "X-File-Name", "Content-Type", "X-CSRFToken"],
)
XHR_SHARING_ALLOWED_METHODS = getattr(
    settings, "XHR_SHARING_ALLOWED_METHODS", ["POST", "GET", "OPTIONS", "PUT", "DELETE"]
)
XHR_SHARING_ALLOWED_CREDENTIALS = getattr(
    settings, "XHR_SHARING_ALLOWED_CREDENTIALS", "true"
)


class XhrSharingMiddleware(object):
    @staticmethod
    def process_request(request):
        if "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META:
            response = http.HttpResponse()
            response["Access-Control-Allow-Origin"] = XHR_SHARING_ALLOWED_ORIGINS
            response["Access-Control-Allow-Headers"] = ",".join(
                XHR_SHARING_ALLOWED_HEADERS
            )
            response["Access-Control-Allow-Methods"] = ",".join(
                XHR_SHARING_ALLOWED_METHODS
            )
            response[
                "Access-Control-Allow-Credentials"
            ] = XHR_SHARING_ALLOWED_CREDENTIALS

            return response

        return None

    @staticmethod
    def process_response(request, response):
        if response.has_header("Access-Control-Allow-Origin"):
            return response

        response["Access-Control-Allow-Origin"] = XHR_SHARING_ALLOWED_ORIGINS
        response["Access-Control-Allow-Headers"] = ",".join(XHR_SHARING_ALLOWED_HEADERS)
        response["Access-Control-Allow-Methods"] = ",".join(XHR_SHARING_ALLOWED_METHODS)
        response["Access-Control-Allow-Credentials"] = XHR_SHARING_ALLOWED_CREDENTIALS

        return response
