from rest_framework import permissions
from .models import Blocklist


# Defines permission for Owner for Update property
class IsOwerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow creator of object to update/delete.
     Assumes the model instance has an `created_by` attribute.
    """

    message = "Access violation. This incident will be reported"

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `created_by`.
        return obj.created_by == request.user


# Check if request user is admin or readonly
class IsAdminOrReadOnly(permissions.BasePermission):

    message = "Access violation. No user right."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


# Check if request user is admin or readonly
class IsBlockListed(permissions.BasePermission):

    message = 'You have been block listed.'

    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blocked = Blocklist.objects.filter(ip=ip_addr)
        if not blocked.exists:
            return True

        return not blocked.is_active
