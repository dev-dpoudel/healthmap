from rest_framework import viewsets
from rest_framework import permissions
from .models import MedicalOfficer
from .serializers import MOSerializer
from django_filters import rest_framework as filters


# Filters specific to staff Records
class MOFilters(filters.FilterSet):
    # username = filters.CharFilter(field_name="username", lookup_expr="icontiains")  # noqa E501
    fromdate = filters.DateFilter(field_name="join_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateFilter(field_name="join_date", lookup_expr="year__lte")  # noqa E501
    position = filters.CharFilter(field_name="position", lookup_expr="icontiains")  # noqa E501
    department = filters.CharFilter(field_name="department", lookup_expr="icontiains")  # noqa E501

    class Meta:
        model = MedicalOfficer
        fields = []


class MOViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Staff Details to be viewed or edited.
    """
    queryset = MedicalOfficer.objects.all().order_by('-created_date')
    serializer_class = MOSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = MOFilters
    permission_classes = [permissions.IsAuthenticated]
