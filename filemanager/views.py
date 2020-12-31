from rest_framework import viewsets
from rest_framework import permissions
from .models import Files
from filemanager.serializers import FileSerializers


class FilesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows User Files to be viewed or edited.
    """
    queryset = Files.objects.all().order_by('-date_joined')
    serializer_class = FileSerializers
    permission_classes = [permissions.IsAuthenticated]
