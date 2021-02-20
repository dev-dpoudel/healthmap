from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import User, Scope
from rest_framework.decorators import action
from rest_framework.response import Response
from user.serializers import UserSerializer, GroupSerializer, ScopeSerializer
from django_filters import rest_framework as filters
from security.filters import CurrentUserorStaffFilter
from security.permissions import IsSuperUserOrReadOnly, IsSuperUser


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
    filter_backends = [filters.DjangoFilterBackend, CurrentUserorStaffFilter]
    filter_class = UserFilter
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrReadOnly]


# Creation of Group is Blocked as an security issue. Use of Django Admin
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


# Filter Calss for Menu
class MenuFilter(filters.FilterSet):
    group = filters.CharFilter(
        help_text="Search in reference to group",
        field_name="groups")
    menuset = filters.CharFilter(
        help_text="Search in reference to menu sets",
        field_name="menu_set")

    class Meta:
        model = Scope
        fields = ['action', 'menu']


# Creation of Menu is Blocked for Non Super Users as an security issue.
# Admin Interface is advised for such actions
class MenuViewSet(viewsets.ModelViewSet):
    """
    read:
    Return information about the selected group menus.

    list:
    Return a list of all the existing group menus.

    create:
    Create a new user menu.

    update:
    Update information for the selected user menu.

    partial_update:
    Update the selected fields for given user menu.

    delete:
    Delete the given user menu.
    """
    queryset = Scope.objects.all().order_by('menu')
    serializer_class = ScopeSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = MenuFilter
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]

    @action(detail=False,
            methods=['get'],
            permission_classes=[permissions.IsAuthenticated]
            )
    def getScope(self, request):
        ''' Get Current user Menu List '''
        groupid = request.user.groups.first()
        if groupid:
            userMenu = self.queryset.filter(groups=groupid.id)
            serializer = self.get_serializer(userMenu, many=True)
            return Response(serializer.data)

        return Response(status="404", data="User Not Authorized for action")
