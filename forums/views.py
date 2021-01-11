from rest_framework import viewsets
from rest_framework import permissions
from .models import Forums, Discussion
from .serializers import ForumSerializers, DiscussionSerializer
from django_filters import rest_framework as filters
# from helper.filters.access_filters import IsOwnerFilterBackend
from helper.permissions.post_permit import IsOwerOrReadOnly


# Filters specific to Forum Thread Records
class ForumFilters(filters.FilterSet):
    user = filters.CharFilter(
        field_name="created_by",
        lookup_expr="exact",
        help_text="Search based upon username")
    fromdate = filters.DateFilter(
        field_name="created_date",
        lookup_expr="year__gte",
        help_text="Date Created gt specified date")
    tilldate = filters.DateFilter(
        field_name="created_date",
        lookup_expr="year__lte",
        help_text="Date Created lte specified date")

    class Meta:
        model = Forums
        fields = ['is_closed']


class ForumViewSet(viewsets.ModelViewSet):
    """
    read:
    Return the given user thread. Search based upon additional Query Parameters

    list:
    Return a list of all the existing user threads.

    create:
    Create a new user Forum thread .

    update:
    Update the given user thread.

    partial_update:
    Update the given user thread with minimal required fields.

    delete:
    Delete the given user thread.
    """
    queryset = Forums.objects.all().order_by('-created_date')
    serializer_class = ForumSerializers
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = ForumFilters
    permission_classes = [permissions.IsAuthenticated, IsOwerOrReadOnly]


# Filters specific to Discussion Thread Records
class DiscussionFilters(filters.FilterSet):
    user = filters.CharFilter(
        field_name="created_by",
        lookup_expr="exact",
        help_text="Search based on owner of the thread")
    thread = filters.CharFilter(
        field_name="thread_id",
        lookup_expr="exact",
        help_text="Based upon the header thread")
    fromdate = filters.DateFilter(
        field_name="created_date",
        lookup_expr="year__gte",
        help_text="Created Date gte specified date")
    tilldate = filters.DateFilter(
        field_name="created_date",
        lookup_expr="year__lte",
        help_text="Created Date lte specified date")

    class Meta:
        model = Discussion
        fields = ['created_date']


class DiscussionViewSet(viewsets.ModelViewSet):
    """
    read:
    Return the given user. Search based upon additional Query Parameters

    list:
    Return a list of all the discussion for a Forum thread.

    create:
    Create a new user comment.

    update:
    Update the user comment. Needs to be the owner of the comment`

    partial_update:
    Update the sleceted fields for given user.

    delete:
    Delete the selected user comment.
    """
    queryset = Discussion.objects.all().order_by('-created_date')
    serializer_class = DiscussionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = DiscussionFilters
    permission_classes = [permissions.IsAuthenticated, IsOwerOrReadOnly]
