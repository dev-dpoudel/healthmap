from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import User
from user.serializers import UserSerializer, GroupSerializer
from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(field_name="username",
                                  lookup_expr="icontains")
    birthdate = filters.DateFilter(field_name="birth_date",
                                   lookup_expr='year__gte')
    firstname = filters.CharFilter(field_name="first_name",
                                   lookup_expr='icontains')
    lastname = filters.CharFilter(field_name="last_name",
                                  lookup_expr='icontains')
    bloodgroup = filters.CharFilter(field_name="blood_group",
                                    lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['is_active']


class UserViewSet(viewsets.ModelViewSet):
    """
    read:
    Return the given user. Search based upon additional Query Parameters

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.

    update:
    Update information for the selected user.

    partial_update:
    Update the sleceted fields for given user.

    delete:
    Delete the given user.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = UserFilter
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    read:
    Return information about the selected group.

    list:
    Return a list of all the existing group.

    create:
    Create a new user group.

    update:
    Update information for the selected user group.

    partial_update:
    Update the sleceted fields for given user group.

    delete:
    Delete the given user group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
