from rest_framework import viewsets
from rest_framework import permissions
from .models import Forums, Discussion
from .serializers import ForumSerializers, DiscussionSerializer
from django_filters import rest_framework as filters


# Filters specific to Forum Thread Records
class ForumFilters(filters.FilterSet):
    username = filters.CharFilter(field_name="created_by", lookup_expr="icontiains")  # noqa E501
    fromdate = filters.DateFilter(field_name="created_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateFilter(field_name="created_date", lookup_expr="year__lte")  # noqa E501

    class Meta:
        model = Forums
        fields = ['is_closed']


class ForumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Forum Thread to be viewed or edited.
    """
    queryset = Forums.objects.all().order_by('-created_date')
    serializer_class = ForumSerializers
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = ForumFilters
    permission_classes = [permissions.IsAuthenticated]


# Filters specific to Discussion Thread Records
class DiscussionFilters(filters.FilterSet):
    username = filters.CharFilter(field_name="created_by", lookup_expr="icontiains")  # noqa E501
    fromdate = filters.DateFilter(field_name="created_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateFilter(field_name="created_date", lookup_expr="year__lte")  # noqa E501

    class Meta:
        model = Discussion
        fields = ['created_date']


class DiscussionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Discussion Thread to be viewed or edited.
    """
    queryset = Discussion.objects.all().order_by('-created_date')
    serializer_class = DiscussionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = DiscussionFilters
    permission_classes = [permissions.IsAuthenticated]
