from .models import StaffFamily, StaffPersons
from rest_framework import serializers


# Meta Class for Exclude Field Definitions
class ExcludeFields:
    class Meta:
        abstract = True
        exclude_fields = ['created_date', 'modified_date', 'entered_by']


# Serializer for Staff Personnels
class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(ExcludeFields.Meta):
        model = StaffPersons


# Serializer for Staff Families
class FamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta(ExcludeFields.Meta):
        model = StaffFamily
