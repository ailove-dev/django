from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    modules = serializers.ListField()
    duration = serializers.IntegerField()
