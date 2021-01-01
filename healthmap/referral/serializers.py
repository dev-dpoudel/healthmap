from .models import Referral
from rest_framework import serializers


# Serializer for Staff Personnels
class ReferralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Referral
        fields = '__all__'
