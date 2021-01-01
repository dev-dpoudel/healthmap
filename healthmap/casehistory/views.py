from rest_framework import viewsets
from rest_framework import permissions
from .models import CaseHistory, Diagnosis, InvestigationHistory, Medication
from .serializers import (CaseSerializer, DiagnosisSerializer,
                          InvestigationSerializer,
                          MedictionSerializer)
from django_filters import rest_framework as filters


# Filters specific to Case Records
class CaseFilters(filters.FilterSet):
    username = filters.CharFilter(field_name="username", lookup_expr="icontiains")  # noqa E501
    fromdate = filters.DateFilter(field_name="entered_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateFilter(field_name="entered_date", lookup_expr="year__lte")  # noqa E501
    referal = filters.NumberFilter(field_name="referral_id", lookup_expr="exact")  # noqa E501

    class Meta:
        model = CaseHistory
        fields = ['case_status', 'case_type', 'patient_type']


class CaseHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Case History to be viewed or edited.
    """
    queryset = CaseHistory.objects.all().order_by('entered_date')
    serializer_class = CaseSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = CaseFilters
    permission_classes = [permissions.IsAuthenticated]


# Filters specific to Diagnosis
class DiagnosisFilters(filters.FilterSet):
    fromdate = filters.DateFilter(field_name="diagnose_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateFilter(field_name="diagnose_date", lookup_expr="year__lte")  # noqa E501
    followdate = filters.DateFilter(field_name="followup_date", lookup_expr="year__eq")  # noqa E501

    class Meta:
        model = Diagnosis
        fields = ['case_id']


class DiagnosisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Diagnosis Details to be viewed or edited.
    """
    queryset = Diagnosis.objects.all().order_by('-diagnose_date')
    serializer_class = DiagnosisSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = DiagnosisFilters
    permission_classes = [permissions.IsAuthenticated]


# Filters specific to Diagnosis
class InvestigationFilters(filters.FilterSet):
    fromdate = filters.DateFilter(field_name="investigation_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateFilter(field_name="investigation_date", lookup_expr="year__lte")  # noqa E501

    class Meta:
        model = InvestigationHistory
        fields = ['investigation_type', 'diagnosis_id']


class InvestigationHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Investigation Details to be viewed or edited.
    """
    queryset = InvestigationHistory.objects.all().order_by('-investigation_date')  # noqa E501 : Line Length
    serializer_class = InvestigationSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = InvestigationFilters
    permission_classes = [permissions.IsAuthenticated]


# Filters specific to Diagnosis
class MedicationFilters(filters.FilterSet):
    fromdate = filters.DateFilter(field_name="start_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateFilter(field_name="start_date", lookup_expr="year__lte")  # noqa E501

    class Meta:
        model = Medication
        fields = ['medicine_type', 'is_active', 'dose', 'dose_measure']


class MedicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Medication Details to be viewed or edited.
    """
    queryset = Medication.objects.all().order_by('-start_date')
    serializer_class = MedictionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = MedicationFilters
    permission_classes = [permissions.IsAuthenticated]
