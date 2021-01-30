from .models import Forums, Discussion
from security.serializers import HiddenOwnerSerializer


# Class for File Serializers
class ForumSerializers(HiddenOwnerSerializer):

    class Meta:
        model = Forums
        fields = '__all__'


# Comment Serializers
class DiscussionSerializer(HiddenOwnerSerializer):

    class Meta:
        model = Discussion
        fields = '__all__'
