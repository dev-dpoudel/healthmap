from .models import CaseHistory, Diagnosis, InvestigationHistory, Medication
from rest_framework import serializers


# Serializers for Case History and Related Information
class CaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaseHistory
        exclude = ['update_date']


# Serializers for Diagnosis History and Related Information
class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diagnosis
        exclude = ['is_investigation_req']


# Serializers for Investigation History and Related Information
class InvestigationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvestigationHistory
        fields = '__all__'


# Serializers for Medication Information
class MedictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'
