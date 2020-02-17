from projects import models
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = ('id', 'user_profile', 'name',
                  'description', 'completed', 'user_stories')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Action
        fields = ['project_id', 'description', 'note']
