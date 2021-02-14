from .viewMixins import GetListMixins
from rest_framework import permissions
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
# Import Model Related to Blocklist and Incidence
from .models import (Blocklist, Incidence)
# Import information related to Serializers
from .serializers import (BlocklistSerializer, IncidenceSerializer)


# Filters specific to Hospital Records
class BlocklistFilters(filters.FilterSet):
    fromdate = filters.DateFilter(
        field_name="entered_date",
        lookup_expr="year__gte",
        help_text="Blocked from")
    todate = filters.DateFilter(
        field_name="entered_date",
        lookup_expr="year__lte",
        help_text="Blocked To")
    ipaddr = filters.CharFilter(
        field_name="ip",
        help_text="IP address")
    duration = filters.NumberFilter(
        field_name="duration",
        help_text="Duration of Block")

    class Meta:
        model = Blocklist
        fields = ['type']


class BlocklistViewSet(GetListMixins):
    """
    API endpoint that allows Blocklist History to be viewed.
    """
    queryset = Blocklist.objects.all().order_by('start_date')
    serializer_class = BlocklistSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_class = BlocklistFilters
    ordering_fields = '__all__'
    ordering = ['start_date']
    permission_classes = [permissions.IsAdminUser]


# Filters specific to Department
class IncidenceFilters(filters.FilterSet):
    fromdate = filters.DateFilter(
        field_name="entered_date",
        lookup_expr="year__gte",
        help_text="Blocked from")
    todate = filters.DateFilter(
        field_name="entered_date",
        lookup_expr="year__lte",
        help_text="Blocked To")
    ipaddr = filters.CharFilter(
        field_name="ip",
        help_text="IP address")
    user = filters.CharFilter(
        field_name="user",
        help_text="User Related to")

    class Meta:
        model = Incidence
        fields = ['type']


class IncidenceViewSet(GetListMixins):
    """
    API endpoint that allows Incidence Details to be viewed.
    """
    queryset = Incidence.objects.all().order_by('entered_date')
    serializer_class = IncidenceSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filter_class = IncidenceFilters
    ordering_fields = ['entered_date', 'user', 'ip']
    ordering = ['entered_date']
    permission_classes = [permissions.IsAdminUser]
