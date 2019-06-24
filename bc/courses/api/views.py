import logging

from rest_framework import generics
from rest_framework.response import Response

from bc.auth import get_auth_token
from bc.services.bc_v1.v3.api import BusinessClassAPI
from .. import models
from . import serializers

logger = logging.getLogger(__name__)


class CourseListAPIView(generics.ListAPIView):
    queryset = models.Course.objects.filter(is_enabled=True)
    serializer_class = serializers.CourseSerializer
    paginator_class = None

    def get_user_course(self):
        user = self.request.user
        if not user.is_authenticated:
            return

        auth_token = get_auth_token(self.request)

        if not user.course_path:
            user_data = BusinessClassAPI.profile_short(auth_token)
            user = user_data.update_user(user)

        course = BusinessClassAPI.user_course(auth_token)
        course.attach_external_id(user.course_path)
        return course

    def get_queryset(self):
        user_course = self.get_user_course()
        qs = super().get_queryset()

        for course in qs:
            if user_course and course.external_id == user_course.external_id:
                course.external_data = user_course.common_data
                course.save()
                course.external_data.update(user_course.data)
            yield course


class CourseModuleRetieveAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        return Response(
            BusinessClassAPI.course_module(kwargs["module_id"], get_auth_token(request))
        )
