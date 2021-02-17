from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import User
from user.serializers import UserSerializer, GroupSerializer
from django_filters import rest_framework as filters
from security.filters import IsCurrentUserorStaff
from security.permissions import IsAdminOrReadOnly


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(
        help_text="Search in reference to username",
        field_name="username",
        lookup_expr="icontains")
    birthdate = filters.DateFilter(
        help_text="Search with Birthdate GTE given date",
        field_name="birth_date",
        lookup_expr='year__gte')
    firstname = filters.CharFilter(
        help_text="Search matching the first name : Case insensitive",
        field_name="first_name",
        lookup_expr='icontains')
    lastname = filters.CharFilter(
        help_text="Search matching the lastname : Case insensitive",
        field_name="last_name",
        lookup_expr='icontains')
    bloodgroup = filters.CharFilter(
        help_text="Search with blood group or containing string",
        field_name="blood_group",
        lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['is_active', 'country']


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
    filter_backends = [filters.DjangoFilterBackend, IsCurrentUserorStaff]
    filter_class = UserFilter
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]


# Creation of Group is Bloacked as an security issue. Use of Django Admin
# Interface is advised for such actions
class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    read:
    Return information about the selected group.

    list:
    Return a list of all the existing group.

    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
