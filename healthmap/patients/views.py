from rest_framework import viewsets
from security import permissions
from .models import StaffPersons, StaffFamily
from .serializers import StaffSerializer, FamilySerializer
from django_filters import rest_framework as filters


# Filters specific to staff Records
class StaffPersonFilters(filters.FilterSet):
    username = filters.CharFilter(
        field_name="username",
        lookup_expr="iexact",
        help_text="Username of the Staff Personnel")

    class Meta:
        model = StaffPersons
        fields = ['is_hospital_staff']


class StaffPersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Staff Details to be viewed or edited.
    """
    queryset = StaffPersons.objects.all().order_by('-created_date')
    serializer_class = StaffSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = StaffPersonFilters
    permission_classes = [permissions.IsAdminOrReadOnly]


# Filters specific to staff family
class StaffFamilyFilters(filters.FilterSet):
    username = filters.CharFilter(
        field_name="username",
        lookup_expr="iexact",
        help_text="Username of Staff Family")
    id = filters.NumberFilter(
        field_name="Related Staff Id",
        help_text="Related staff Id")

    class Meta:
        model = StaffFamily
        fields = ['is_billable']


class StaffFamilyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Family Details to be viewed or edited.
    """
    queryset = StaffFamily.objects.all().order_by('-created_date')
    serializer_class = FamilySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = StaffFamilyFilters
    permission_classes = [permissions.IsAdminOrReadOnly]
