from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework import permissions
from healthmap.medicalofficer.permissions import IsMOOrReadOnly
from .models import CaseHistory, Diagnosis, InvestigationHistory, Medication
from .serializers import (CaseSerializer,
                          DiagnosisSerializer,
                          InvestigationSerializer,
                          MedictionSerializer)


# Filters specific to Case Records
class CaseFilters(filters.FilterSet):
    username = filters.CharFilter(
        field_name="username",
        lookup_expr="iexact",
        help_text="Patient name")
    fromdate = filters.DateFilter(
        field_name="entered_date",
        lookup_expr="year__gte",
        help_text="Case registered date gte fromdate")
    tilldate = filters.DateFilter(
        field_name="entered_date",
        lookup_expr="year__lte",
        help_text="Case registered lte date")
    referal = filters.NumberFilter(
        field_name="referral_id",
        lookup_expr="exact",
        help_text="Referral Identification")

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
    permission_classes = [permissions.IsAuthenticated, IsMOOrReadOnly]


# Filters specific to Diagnosis
class DiagnosisFilters(filters.FilterSet):
    fromdate = filters.DateFilter(
        field_name="diagnose_date",
        lookup_expr="year__gte",
        help_text="Case registered gte date")
    tilldate = filters.DateFilter(
        field_name="diagnose_date",
        lookup_expr="year__lte",
        help_text="Case registered lte date")
    followdate = filters.DateFilter(
        field_name="followup_date",
        lookup_expr="year__eq",
        help_text="Follow up date")

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
    permission_classes = [permissions.IsAuthenticated, IsMOOrReadOnly]


# Filters specific to Diagnosis
class InvestigationFilters(filters.FilterSet):
    fromdate = filters.DateFilter(
        field_name="investigation_date",
        lookup_expr="year__gte",
        help_text="Investigation registered gte date")
    tilldate = filters.DateFilter(
        field_name="investigation_date",
        lookup_expr="year__lte",
        help_text="Investigation registered lte date")

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
    permission_classes = [permissions.IsAuthenticated, IsMOOrReadOnly]


# Filters specific to Diagnosis
class MedicationFilters(filters.FilterSet):
    fromdate = filters.DateFilter(
        field_name="start_date",
        lookup_expr="year__gte",
        help_text="Medicine start gte date")
    tilldate = filters.DateFilter(
        field_name="start_date",
        lookup_expr="year__lte",
        help_text="Medication start lte date")

    class Meta:
        model = Medication
        fields = ['medicine_type', 'dose', 'dose_measure', 'duration']


class MedicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Medication Details to be viewed or edited.
    """
    queryset = Medication.objects.all().order_by('-start_date')
    serializer_class = MedictionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = MedicationFilters
    permission_classes = [permissions.IsAuthenticated, IsMOOrReadOnly]
