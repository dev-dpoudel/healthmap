from rest_framework import viewsets
from rest_framework import permissions
# Import Model Related to Hospital and Department
from .models import (HospitalInformation, DepartmentInformation,
                     RoomInformation, BedInformation, VacancyInfo)
# Import information related to Serializers
from .serializers import (HospitalSerializer, DepartSerializer,
                          RoomInfoSerializer, BedInfoSerializer,
                          VacancySerializer)

from django_filters import rest_framework as filters

# Import Permission permission classes
from security.permissions import IsAdminOrReadOnly


# Filters specific to Hospital Records
class HospitalFilters(filters.FilterSet):
    name = filters.CharFilter(field_name="name",
                              lookup_expr="icontiains",
                              help_text="Filter by Name")
    city = filters.CharFilter(field_name="city", lookup_expr="iexact")
    region = filters.CharFilter(field_name="region", lookup_expr="iexact")
    country = filters.CharFilter(field_name="country", lookup_expr="iexact")

    class Meta:
        model = HospitalInformation
        fields = ['provides_ambulance', 'has_lab', 'emergency_available']


class HospitalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Case History to be viewed or edited.
    """
    queryset = HospitalInformation.objects.all()
    serializer_class = HospitalSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = HospitalFilters
    permission_classes = [IsAdminOrReadOnly]


# Filters specific to Department
class DepartmentFilters(filters.FilterSet):

    class Meta:
        model = DepartmentInformation
        fields = ['name']


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Diagnosis Details to be viewed or edited.
    """
    queryset = DepartmentInformation.objects.all()
    serializer_class = DepartSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = DepartmentFilters
    permission_classes = [IsAdminOrReadOnly]


# Filters specific to Room Information
class RoomInfoFilters(filters.FilterSet):
    active = filters.BooleanFilter(field_name="is_active")
    type = filters.CharFilter(field_name="room_type", lookup_expr="iexact")

    class Meta:
        model = RoomInformation
        fields = ['department']


class RoomInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Investigation Details to be viewed or edited.
    """
    queryset = RoomInformation.objects.all().order_by('is_active')
    serializer_class = RoomInfoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = RoomInfoFilters
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]


# Filters specific to Diagnosis
class BedInfoFilters(filters.FilterSet):
    active = filters.BooleanFilter(
        field_name="is_active",
        help_text="Operational or Under Maintaince")
    occupied = filters.BooleanFilter(
        field_name="is_occupied",
        help_text="Occupied/Vacant")
    fromdate = filters.DateFilter(
        field_name="planned_service_date",
        lookup_expr="year__gte",
        help_text="Service Date GTE given date")
    tilldate = filters.DateFilter(
        field_name="planned_service_date",
        lookup_expr="year__lte",
        help_text="Service Date LTE given date")

    class Meta:
        model = BedInformation
        fields = ['room']


class BedInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Medication Details to be viewed or edited.
    """
    queryset = BedInformation.objects.all().order_by('-last_service_date')
    serializer_class = BedInfoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = BedInfoFilters
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]


# Filters specific to Diagnosis
class VacancyFilters(filters.FilterSet):
    fromdate = filters.DateFilter(field_name="closure_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateFilter(field_name="closure_date", lookup_expr="year__lte")  # noqa E501

    class Meta:
        model = VacancyInfo
        fields = ['type', 'position', 'department', 'hospital']


class VacancyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Medication Details to be viewed or edited.
    """
    queryset = VacancyInfo.objects.all().order_by('closure_date')
    serializer_class = VacancySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = VacancyFilters
    permission_classes = [IsAdminOrReadOnly]
