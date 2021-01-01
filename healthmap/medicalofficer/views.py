from rest_framework import viewsets
from rest_framework import permissions
from .models import MedicalOfficer
from medicalofficer.serializers import MOSerializer
from django_filters import rest_framework as filters


# Filters specific to staff Records
class MOFilters(filters.FilterSet):
    username = filters.CharField(field_name="username", lookup_expr="icontiains")  # noqa E501
    fromdate = filters.DateField(field_name="join_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateField(field_name="join_date", lookup_expr="year__lte")  # noqa E501
    position = filters.CharField(field_name="position", lookup_expr="icontiains")  # noqa E501
    department = filters.CharField(field_name="department", lookup_expr="icontiains")  # noqa E501

    class Meta:
        model = MedicalOfficer


class MOViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Staff Details to be viewed or edited.
    """
    queryset = MedicalOfficer.objects.all().order_by('-created_date')
    serializer_class = MOSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = MOFilters
    permission_classes = [permissions.IsAuthenticated]
