from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from .models import MedicalOfficer


# Check if request user is admin or readonly
class IsMOOrReadOnly(permissions.BasePermission):

    message = "User right violation. This incidence will be reported"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        try:
            user = request.user.username
            medical_officer = MedicalOfficer.objects.get(username=user)
            if medical_officer:
                return True

        except ObjectDoesNotExist:
            return False
