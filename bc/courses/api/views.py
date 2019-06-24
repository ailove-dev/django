from rest_framework import generics
from rest_framework.response import Response

from bc.auth import get_auth_token
from bc.services.bc_v1.v3.api import BusinessClassAPI
from .. import models
from . import serializers


class CourseListAPIView(generics.ListAPIView):
    queryset = models.Course.objects.filter(is_enabled=True)
    serializer_class = serializers.CourseSerializer
    paginator_class = None

    def get_queryset(self):
        return [
            {**obj.internal_data, **obj.external_data} for obj in super().get_queryset()
        ]

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.course_path:
            auth_token = get_auth_token(request)
            try:
                course = models.Course.objects.get(external_id=request.user.course_path)
            except models.Course.DoesNotExists:
                pass
            else:
                course_data = BusinessClassAPI.user_course(auth_token).serialize()
                course.external_data = course_data
                course.save()

        return super().get(request, *args, **kwargs)


class CourseModuleRetieveAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response(
            BusinessClassAPI.course_module(kwargs["module_id"], get_auth_token(request))
        )
