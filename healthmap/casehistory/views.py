from rest_framework import viewsets
from rest_framework import permissions
from .models import CaseHistory, Diagnosis, InvestigationHistory, Medication
from casehistory.serializers import (CaseSerializer, DiagnosisSerializer,
                                     InvestigationSerializer,
                                     MedictionSerializer)


class CaseHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Case History to be viewed or edited.
    """
    queryset = CaseHistory.objects.all().order_by('+entered_date')
    serializer_class = CaseSerializer
    permission_classes = [permissions.IsAuthenticated]


class DiagnosisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Diagnosis Details to be viewed or edited.
    """
    queryset = Diagnosis.objects.all().order_by('-diagnose_date')
    serializer_class = DiagnosisSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvestigationHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Investigation Details to be viewed or edited.
    """
    queryset = InvestigationHistory.objects.all().order_by('-investigation_date') # noqa E501 : Line Length
    serializer_class = InvestigationSerializer
    permission_classes = [permissions.IsAuthenticated]


class MedicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Medication Details to be viewed or edited.
    """
    queryset = Medication.objects.all().order_by('-start_date')
    serializer_class = MedictionSerializer
    permission_classes = [permissions.IsAuthenticated]
