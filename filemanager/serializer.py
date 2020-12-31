from rest_framework import serializers
from .models import Files


# Class for File Serializers
class FileSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Files
        field = ['file', 'file_type']
