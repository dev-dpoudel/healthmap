# Provides Serializers for Default Field Value on global scope
from rest_framework import serializers


# Class for File Serializers
class HiddenOwnerSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    created_by = serializers.HiddenField(
        default=serializers.CreateOnlyDefault(serializers.CurrentUserDefault())
    )

    class Meta:
        abstract = True
