from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user = {
            "id": user.id,
            "username": user.username,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
            "type": user.type,
        }
        token["user"] = user

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            is_active=False,
        )
        return user

    def validate_password(self, value):
        # You can add custom validation for password here
        return value


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
