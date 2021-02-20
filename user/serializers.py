from django.contrib.auth.models import Group
from .models import User, Scope
from rest_framework import serializers


class ScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope
        exclude = ['groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Fetch Age from model property
    age = serializers.ReadOnlyField()

    class Meta:
        model = User
        exclude = ['groups',
                   'user_permissions',
                   'is_staff',
                   'is_superuser',
                   'password']
