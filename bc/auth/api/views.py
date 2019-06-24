from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bc.auth import USER_AUTH_TOKEN_COOKIE_NAME
from bc.services.bc_v1.v3.api import BusinessClassAPI
from . import exceptions, serializers


class LoginAPIView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer
    permission_classes = (~IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            bc_response = BusinessClassAPI.login(**serializer.validated_data)
        except BusinessClassAPI.AuthFailed:
            raise exceptions.AuthException

        username, token = bc_response["username"], bc_response["token"]
        user = authenticate(username=username, password=None)

        login(request, user)
        response = Response()
        response.set_cookie(USER_AUTH_TOKEN_COOKIE_NAME, token)
        return response


class LogoutAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie(USER_AUTH_TOKEN_COOKIE_NAME)
        logout(request)
        return response
