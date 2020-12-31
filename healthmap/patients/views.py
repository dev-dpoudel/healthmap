from rest_framework import viewsets
from rest_framework import permissions
from .models import StaffPersons, StaffFamily
from patients.serializers import StaffSerializer, FamilySerializer


class StaffPersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Staff Details to be viewed or edited.
    """
    queryset = StaffPersons.objects.all().order_by('-created_date')
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated]


class StaffFamilyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Family Details to be viewed or edited.
    """
    queryset = StaffFamily.objects.all().order_by('-created_date')
    serializer_class = FamilySerializer
    permission_classes = [permissions.IsAuthenticated]
