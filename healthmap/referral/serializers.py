from .models import Referral
from rest_framework import serializers


# Serializer for Staff Personnels
class ReferralSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.ReadOnlyField()
    
    class Meta:
        model = Referral
        fields = '__all__'
