from rest_framework import permissions


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
