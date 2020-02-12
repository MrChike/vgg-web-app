from django.shortcuts import render
from projects import models
from projects import permissions
from projects import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


class AuthenticateUserView(ObtainAuthToken):
    # Create Token
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileViewSet(viewsets.ModelViewSet):
    """Create a new users with server-side validation"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class ProjectViewSet(viewsets.ModelViewSet):
    # Perform CRUD Operation of Project Model
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProjectSerializer
    queryset = models.Project.objects.all()
    permission_classes = (permissions.UpdateOwnContent, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'description',)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        # Grant project permission to logged in user
        serializer.save(user_profile=self.request.user)
