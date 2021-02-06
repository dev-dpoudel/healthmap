from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters
# Import Model Related to Blocklist and Incidence
from .models import (XSettings)
# Import information related to Serializers
from .serializers import (XSettingsSerializers)


# Filters specific to Hospital Records
class xSettingFilters(filters.FilterSet):
    type = filters.CharFilter(
        field_name="identity",
        lookup_expr="iexact",
        help_text="Settings Type")
    code = filters.CharFilter(
        field_name="code",
        lookup_expr="iexact",
        help_text="Code Type")
    value = filters.CharFilter(
        field_name="value",
        help_text="Value Referenced")

    class Meta:
        model = XSettings
        fields = ['active']


class XSettingsViewSet(viewsets.ModelViewSet):
    """
    read:
    Return the given user thread. Search based upon additional Query Parameters

    list:
    Return a list of all the existing user threads.

    create:
    Create a new user Forum thread .

    update:
    Update the given user thread.

    partial_update:
    Update the given user thread with minimal required fields.

    delete:
    Delete the given user thread.
    """
    queryset = XSettings.objects.all().order_by('-code')
    serializer_class = XSettingsSerializers
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = xSettingFilters
    permission_classes = [permissions.IsAdminUser]
