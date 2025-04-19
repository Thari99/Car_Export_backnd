from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from .permissions import IsSuperAdmin, IsAdmin, IsNormalUser,IsAdminOrSuperAdmin

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        })

class SuperAdminOnlyView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get(self, request):
        return Response({"message": "Hello Super Admin!"})

class AdminOnlyView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Hello Admin!"})

class AdminOrSupperAdminOnlyView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrSuperAdmin]

    def get(self, request):
        return Response({"message": "Hello!"})

class UserOnlyView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsNormalUser]

    def get(self, request):
        return Response({"message": "Hello User!"})