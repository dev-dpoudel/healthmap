from rest_framework import viewsets
from rest_framework import permissions
from .models import Forums, Discussion
from user.serializers import ForumsSerializers, DiscussionSerializer
from django_filters import rest_framework as filters


# Filters specific to Forum Thread Records
class ForumFilters(filters.FilterSet):
    username = filters.CharField(field_name="username", lookup_expr="icontiains")  # noqa E501
    fromdate = filters.DateField(field_name="entered_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateField(field_name="entered_date", lookup_expr="year__lte")  # noqa E501
    referal = filters.IntField(field_name="referral_id", lookup_expr="exact")

    class Meta:
        model = Forums
        fields = ['case_status', 'case_type', 'patient_type']


class ForumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Forum Thread to be viewed or edited.
    """
    queryset = Forums.objects.all().order_by('-created_date')
    serializer_class = ForumsSerializers
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = ForumFilters
    permission_classes = [permissions.IsAuthenticated]


# Filters specific to Discussion Thread Records
class DiscussionFilters(filters.FilterSet):
    username = filters.CharField(field_name="username", lookup_expr="icontiains")  # noqa E501
    fromdate = filters.DateField(field_name="entered_date", lookup_expr="year__gte")  # noqa E501
    tilldate = filters.DateField(field_name="entered_date", lookup_expr="year__lte")  # noqa E501
    referal = filters.IntField(field_name="referral_id", lookup_expr="exact")

    class Meta:
        model = Forums
        fields = ['case_status', 'case_type', 'patient_type']


class DiscussionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Discussion Thread to be viewed or edited.
    """
    queryset = Discussion.objects.all().order_by('-created_date')
    serializer_class = DiscussionSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = DiscussionFilters
    permission_classes = [permissions.IsAuthenticated]
