from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class RestorePasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
