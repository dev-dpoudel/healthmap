from rest_framework import viewsets
from rest_framework import permissions
from .models import Referral
from referral.serializers import ReferralSerializer


class ReferralViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Referral.objects.all().order_by('-refered_date')
    serializer_class = ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]
