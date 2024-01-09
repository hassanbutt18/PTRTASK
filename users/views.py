from rest_framework.response import Response
from rest_framework import viewsets, status
from socialnetwork.social_network_pagination import SocialNetworkPagination
from users.models import User
from users.serializer import UserResponseSerializer, SignupSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate, login
import json
from users.utils import get_address_info


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserResponseSerializer
    pagination_class = SocialNetworkPagination

    def create(self, request):
        ip_address=request.query_params.get('ip_address',None)
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            refresh_token = RefreshToken.for_user(instance)
            print("in here refresh token",refresh_token)
            refresh = str(refresh_token)
            access = str(refresh_token.access_token)
            user_detail = UserResponseSerializer(instance,many=False).data
            geo_ip = get_address_info(ip_address)
            return Response({"msg": "User Signup successfully", "access_token": access,
                             "refresh": refresh , "user_detail":user_detail,"geo_ip":geo_ip},
                            status=status.HTTP_200_OK)

