from rest_framework import viewsets
from rest_framework import permissions
from .models import MedicalOfficer
from medicalofficer.serializers import MOSerializer


class StaffPersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Staff Details to be viewed or edited.
    """
    queryset = MedicalOfficer.objects.all().order_by('-created_date')
    serializer_class = MOSerializer
    permission_classes = [permissions.IsAuthenticated]
