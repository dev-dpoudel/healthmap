from rest_framework import serializers
from .models import Files
from security.serializers import HiddenOwnerSerializer


# Class for File Serializers
class FileSerializers(HiddenOwnerSerializer):
    modified_date = serializers.ReadOnlyField()
    filename = serializers.ReadOnlyField()
    filesize = serializers.ReadOnlyField()

    class Meta:
        model = Files
        exclude = ['created_date']
        extra_kwargs = {'file': {'write_only': True}}


# Class for File Data Serializers
class FileDataSerializer(serializers.Serializer):

    fileData = serializers.ReadOnlyField()

    class Meta:
        model = Files
        fields = ['fileData']
