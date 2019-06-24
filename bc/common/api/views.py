from rest_framework.response import Response
from rest_framework.views import APIView

from bc.services.bc_v1.v3.api import BusinessClassAPI
from bc.services.bc_v1.v3.constants import PROGRAM_SOURCE_CHOICES


class AreaListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(BusinessClassAPI.areas())


class ProgramSourceListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(PROGRAM_SOURCE_CHOICES)
