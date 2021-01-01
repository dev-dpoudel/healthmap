from rest_framework import viewsets
from rest_framework import permissions
from .models import Referral
from referral.serializers import ReferralSerializer
from django_filters import rest_framework as filters


# Filter Class for Referral
class ReferFilter(filters.FilterSet):
    refby = filters.CharField(field_name="refered_by", lookup_expr="iexact")
    reffrom = filters.CharField(field_name="refered_from", lookup_expr="icontiains")  # noqa E501
    reftype = filters.CharField(field_name="referral_type", lookup_expr="icontiains")  # noqa E501

    class Meta:
        model = Referral
        fields = ['refered_date']


# View Class for Referral Records
class ReferralViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Referral.objects.all().order_by('-refered_date')
    serializer_class = ReferralSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = ReferFilter
    permission_classes = [permissions.IsAuthenticated]
