from .models import MedicalOfficer
from rest_framework import serializers


class MOSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.ReadOnlyField()

    class Meta:
        model = MedicalOfficer
        fields = '__all__'
