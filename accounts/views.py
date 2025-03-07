from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CreateUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response(
                    {**serializer.data, "is_superuser": user.is_superuser},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivationView(APIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data["username"])
        Adminuser = authenticate(
            request,
            username=request.data["adminUsername"],
            password=request.data["adminPassword"],
        )
        if (
            Adminuser is not None
            and Adminuser.is_superuser
            and Adminuser.is_staff
            and user is not None
            and user.check_password(request.data["password"])
        ):
            user.is_active = True
            user.type = int(request.data["type"])
            if request.data["access"] == "write":
                user.is_superuser = True
            user.save()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ResetPassword(APIView):
    def post(self, request, *args, **kwargs):
        user = authenticate(
            request,
            username=request.data["username"],
            password=request.data["oldPassword"],
        )
        if user is not None:
            user.set_password(request.data["newPassword"])
            user.save()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_401_UNAUTHORIZED)
