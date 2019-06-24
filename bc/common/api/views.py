from rest_framework.response import Response
from rest_framework.views import APIView

from bc.services.bc_v1.v3.api import BusinessClassAPI


class AreaListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(BusinessClassAPI.areas())
