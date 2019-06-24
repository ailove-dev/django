from rest_framework.response import Response
from rest_framework.views import APIView

from bc.auth import get_auth_token
from bc.services.bc_v1.v3.api import BusinessClassAPI


class UserRetrieveAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(BusinessClassAPI.profile_short(get_auth_token(request)))
