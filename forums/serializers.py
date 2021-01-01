from rest_framework import serializers
from .models import Forums, Discussion


# Class for File Serializers
class ForumSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forums
        fields = '__all__'


class DiscussionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discussion
        fields = '__all__'
