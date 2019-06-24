from rest_framework import serializers

from .. import models


class CourseModuleSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    duration = serializers.IntegerField()
    title = serializers.CharField()
    info = serializers.CharField()
    state = serializers.CharField(required=False)
    lessons_count = serializers.IntegerField(source="lessonsCount", required=False)
    completed_lessons_count = serializers.IntegerField(
        source="completedLessonsCount", required=False
    )


class CourseSerializer(serializers.ModelSerializer):
    modules = CourseModuleSerializer(source="external_data.modules", many=True)
    duration = serializers.IntegerField(source="external_data.duration")

    class Meta:
        model = models.Course
        fields = ("modules", "duration")
