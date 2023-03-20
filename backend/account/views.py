from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from utils import permission

from .models import User
from .serializers import UserRegisterSerializer, UserInfoSerializer


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered a new user"
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)

class RefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserInfoView(APIView):
    permission_classes = [permission.IsRightUser]

    def get_object(self, username):
        user = get_object_or_404(User, username=username)
        return user

    def get(self, request, username, format=None):
        user = self.get_object(username)
        
        if request.user.username != user.username:
            return Response({"error": "접근 권한이 없습니다"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserInfoSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)