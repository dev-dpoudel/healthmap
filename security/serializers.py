# Provides Serializers for Default Field Value on global scope
from rest_framework import serializers
from .models import Blocklist, Incidence


# Class for File Serializers
class HiddenOwnerSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    created_by = serializers.HiddenField(
        default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault())
    )

    class Meta:
        abstract = True


# Class for Blocklist Serializers
class BlocklistSerializer(serializers.HyperlinkedModelSerializer):
    is_active = serializers.ReadOnlyField()

    class Meta:
        model = Blocklist
        fields = '__all__'


# Class for Incidence Serializers
class IncidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incidence
        fields = '__all__'
