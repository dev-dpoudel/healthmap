from django.contrib.auth.models import Group
from .models import User
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Fetch related group information
    groups = GroupSerializer(many=True, required=False)
    # Fetch Age from model property
    age = serializers.ReadOnlyField()

    class Meta:
        model = User
        exclude = ['user_permissions', 'is_staff', 'is_superuser', 'password']
