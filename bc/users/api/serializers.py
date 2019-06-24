from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(source="firstName")
    last_name = serializers.CharField(source="lastName")
    email = serializers.CharField()
    phone = serializers.CharField()
    avatar = serializers.CharField(source="photo")
    is_email_verified = serializers.BooleanField(source="isEmailVerified")
