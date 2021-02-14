from .models import (HospitalInformation, DepartmentInformation,
                     RoomInformation, BedInformation, VacancyInfo)
from rest_framework import serializers


# Serializer for Hospital+ Information
class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    hospital_type = serializers.ReadOnlyField()

    class Meta:
        model = HospitalInformation
        fields = '__all__'
        extra_kwargs = {
            # 'type': {'write_only': True},
        }


# Serializer for Department Information
class DepartSerializer(serializers.HyperlinkedModelSerializer):
    updated_date = serializers.ReadOnlyField()

    class Meta:
        model = DepartmentInformation
        fields = '__all__'


# Serializer for Room Information
class RoomInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoomInformation
        fields = '__all__'


# Serializer for Bed Information
class BedInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BedInformation
        fields = '__all__'


# Serializer for Bed Information
class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VacancyInfo
        fields = '__all__'
