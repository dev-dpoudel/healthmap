from rest_framework import viewsets
from rest_framework import permissions
from .models import Files
from filemanager.serializers import FileSerializers
from django_filters import rest_framework as filters


# Filters specific to Case Records
class CaseFilters(filters.FilterSet):
    user = filters.CharField(field_name="entered_by", lookup_expr="icontains")
    fromdate = filters.DateField(field_name="entered_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateField(field_name="entered_date", lookup_expr="year__lte")  # noqa E501
    referal = filters.IntField(field_name="referral_id", lookup_expr="exact")

    class Meta:
        model = Files
        fields = ['file_type', 'file_ext', 'ref_id', 'ref_table', 'ref_field']


class FilesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User Files to be viewed or edited.
    """
    queryset = Files.objects.all().order_by('-update_date')
    serializer_class = FileSerializers
    permission_classes = [permissions.IsAuthenticated]
