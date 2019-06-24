from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from bc.auth import get_auth_token
from bc.services.bc_v1.v3.api import BusinessClassAPI
from . import serializers


class UserRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    def get_object(self):
        user_data = BusinessClassAPI.profile_short(
            user_token=get_auth_token(self.request)
        )
        user_data.update_user(self.request.user)

        return user_data
