from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.settings import api_settings
from profiles_api import views
from django.urls import path
from rest_framework import viewsets, filters
from profiles_api.models import UserProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from profiles_api import serializers
from profiles_api import permissions


def home(request):
    path('', views.home, name='home'),
    return render(request, 'home.html', {})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (permissions.UpdateOwnPrfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication toekn"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data,
    #                                        context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data['user']
    #     token, created = Token.objects.get_or_create(user=user)
    #     return Response({
    #         'token': token.key,
    #         'id': user.pk,
    #         'email': user.email,
    #     })
