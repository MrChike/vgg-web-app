from django.shortcuts import render
from projects import models
from projects import permissions
from projects import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
