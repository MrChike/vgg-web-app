from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.decorators import action
from .serializers import ProjectSerializer, ActionSerializer
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
from.models import Action


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
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    def perform_create(self, serializer):
        # Grant project permission to logged in user
        serializer.save(user_profile=self.request.user)

    @action(detail=True, methods=['put'])
    def actions(self, request, pk=None):
        user = self.get_object()
        user_stories = user.user_stories
        serializer = ProjectSerializer(user_stories, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)


class ActionViewset(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
