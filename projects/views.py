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


# class CreateUserView(APIView):
#     """Test API View"""
#     serializer_class = serializers.UserProfileSerializer

#     def get(self, request, format=None):
#         """Returns a list of APIView features"""

#         an_apiview = [
#             'Uses HTTP methods as functions (get, post, patch, put, delete)',
#             'Is similar to a traditional Django View',
#             'Gives you the most control over your logic',
#             'Is mapped manually to URLs',
#         ]

#         return Response({'message': 'Hello!', 'an_apiview': an_apiview})

#     def post(self, request):
#         """Create a hello message with our name"""
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             email = serializer.validated_data.get('email')
#             # message = f'Hello {name}!'
#             message = f'Hello {name}, your emailhas been received. Head over to the auth endpoint /api/users/auth for you token!'
#             return Response({
#                 'message': message,
#             })
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#     def put(self, request, pk=None):
#         return Response({'method': 'PUT'})

#     def patch(self, request, pk=None):
#         """Handle partial update of object"""

#         return Response({'method': 'PATCH'})

#     def delete(self, request, pk=None):
#         """Delete an object"""

#         return Response({'method': 'DELETE'})


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

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
