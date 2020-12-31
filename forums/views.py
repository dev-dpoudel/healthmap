from rest_framework import viewsets
from rest_framework import permissions
from .models import Forums, Discussion
from user.serializers import ForumsSerializers, DiscussionSerializer


class ForumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Forum Thread to be viewed or edited.
    """
    queryset = Forums.objects.all().order_by('-date_joined')
    serializer_class = ForumsSerializers
    permission_classes = [permissions.IsAuthenticated]


class DiscussionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Discussion Thread to be viewed or edited.
    """
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticated]
