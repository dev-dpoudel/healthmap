from rest_framework import serializers
from .models import Files
from helper.serializers.default import HiddenOwnerSerializer


# Class for File Serializers
class FileSerializers(HiddenOwnerSerializer):
    modified_date = serializers.ReadOnlyField()
    filename = serializers.ReadOnlyField()
    filesize = serializers.ReadOnlyField()
    # filedata = serializers.ReadOnlyField()

    class Meta:
        model = Files
        exclude = ['created_date']
        extra_kwargs = {'file': {'write_only': True}}
