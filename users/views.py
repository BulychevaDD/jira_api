from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CustomTokenObtainPairSerializer, RegisterSerializer, UserInfoSerializer
from rest_framework import generics, views


class CustomObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer


class UserInfoView(views.APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user = self.get_object(request.user.username)
        user_info_serializer = UserInfoSerializer(user)
        user_info_data = user_info_serializer.data

        return Response(user_info_data)
