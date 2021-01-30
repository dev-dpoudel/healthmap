from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters
from .models import Files
from filemanager.serializers import FileSerializers


# Filters specific to Case Records
class FileFilters(filters.FilterSet):
    user = filters.CharFilter(
        field_name="create_by",
        lookup_expr="icontains",
        help_text="Created_by Id")
    fromdate = filters.DateFilter(
        field_name="modified_date",
        lookup_expr="year__gte",
        help_text="Updated Date gte specified date")
    tilldate = filters.DateFilter(
        field_name="modified_date",
        lookup_expr="year__lte",
        help_text="Updated Date lte specified date")
    referal = filters.NumberFilter(
        field_name="ref_id",
        lookup_expr="exact",
        help_text="Reference Id . Use in combination of ref_Table and field")

    class Meta:
        model = Files
        fields = ['file_type', 'ref_table', 'ref_field']


class FilesViewSet(viewsets.ModelViewSet):
    """

    API to Moderate Attachment files. Used for forums / diagnoisis and case

    read:
    Return the given user files. Search based upon additional Query Parameters

    list:
    Return a list of all the existing user files.

    create:
    Create a new user File .

    update:
    Update the given user file.

    partial_update:
    Update the given user file with minimal required fields.

    delete:
    Delete the given file.

    data:
    Get Binary File Data
    """
    queryset = Files.objects.all().order_by('-modified_date')
    serializer_class = FileSerializers
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = FileFilters
    permission_classes = [permissions.IsAuthenticated]


# class FileDataViewSet(RetrieveViewsets):
#     """
#
#     API to get Attachment files. Used for forums / diagnoisis and case
#
#     read:
#     Return the given user files. Search based upon additional Query Parameter
#     """
#     queryset = Files.objects.all()
#     serializer_class = FileDataSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     renderer_classes = [OctetRenderer, PDFRenderer, FileRenderer, ImageRenderer]      # noqa E501
#
#     # def read(self, request, pk, format=None):
#     #     queryset = self.get_queryset()
#     #     serializer = FileDataSerializer(queryset)
#     #     if serializer.data is not None:
#     #         file = open(serializer.data.path, 'rb')
#     #         response = HttpResponse(FileWrapper(file))
#     #         response['Content-Disposition'] = 'attachment;filename="%s"' %(
#     #             serializer.data.name)
#     #     else:
#     #         response = HttpResponse("Not found")
#     #
#     #     return response
