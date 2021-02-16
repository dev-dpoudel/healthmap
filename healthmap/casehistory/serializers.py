from .models import CaseHistory, Diagnosis, InvestigationHistory, Medication
from rest_framework import serializers


# Serializers for Investigation History and Related Information
class InvestigationSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.ReadOnlyField()

    class Meta:
        model = InvestigationHistory
        fields = '__all__'


# Serializers for Medication Information
class MedictionSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.ReadOnlyField()

    class Meta:
        model = Medication
        fields = '__all__'


# Serializers for Diagnosis History and Related Information
class DiagnosisSerializer(serializers.HyperlinkedModelSerializer):
    investigations = InvestigationSerializer(many=True, read_only=True)
    medicines = MedictionSerializer(many=True, read_only=True)

    class Meta:
        model = Diagnosis
        exclude = ['is_investigation_req']


# Serializers for Case History and Related Information
class CaseSerializer(serializers.HyperlinkedModelSerializer):
    diagnosis = DiagnosisSerializer(many=True, read_only=True)
    case_typeds = serializers.ReadOnlyField()
    patient_typeds = serializers.ReadOnlyField()
    status = serializers.ReadOnlyField()

    class Meta:
        model = CaseHistory
        exclude = ['update_date']
