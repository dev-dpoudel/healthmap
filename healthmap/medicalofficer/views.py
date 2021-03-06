from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from security import permissions
from .models import MedicalOfficer
from .serializers import MOSerializer
from django_filters import rest_framework as filters
from security.permissions import IsAdminOrReadOnly


# Filters specific to staff Records
class MOFilters(filters.FilterSet):
    user = filters.CharFilter(
        field_name="username",
        lookup_expr="icontiains",
        help_text="Username of the Medical Officer")
    fromdate = filters.DateFilter(
        field_name="join_date",
        lookup_expr="year__gte",
        help_text="Join date gte selected")
    tilldate = filters.DateFilter(
        field_name="join_date",
        lookup_expr="year__lte",
        help_text="Join Date lte")
    position = filters.CharFilter(
        field_name="position",
        lookup_expr="icontiains",
        help_text="Position of Medical Personnel")
    department = filters.CharFilter(
        field_name="department",
        lookup_expr="iexact",
        help_text="Related Department")

    class Meta:
        model = MedicalOfficer
        fields = ['officer_id']


class MOViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Staff Details to be viewed or edited.
    """
    queryset = MedicalOfficer.objects.all().order_by('-created_date')
    serializer_class = MOSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_class = MOFilters
    ordering_fields = ['created_date', 'department', 'user']
    ordering = ['-created_date']
    permission_classes = [permissions.IsAdminOrReadOnly, IsAdminOrReadOnly]
