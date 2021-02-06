from .models import XSettings
from rest_framework import serializers


# Class for File Serializers
class XSettingsSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = XSettings
        exclude = ['modified_date']
