from .models import MedicalOfficer
from rest_framework import serializers


class MOSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicalOfficer
        fields = ['url', 'username', 'staff_id', 'position', 'department',
                  'join_date', 'service_period']
