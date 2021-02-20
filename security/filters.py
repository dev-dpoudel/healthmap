from rest_framework import filters


# Class Extending Baseic FIlter Function to filter Owner
class CurrentUserFilter(filters.BaseFilterBackend):
    """
    Filter that only allows users to edit or see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(created_by=request.user)


# Filter Viewsets based on the type of user
class CurrentUserorStaffFilter(filters.BaseFilterBackend):
    """
    Filter that only allows users to edit or see their own objects.
    """

    def filter_queryset(self, request, queryset, view):

        # When User is normal user, the user can on;y see his/her details
        if request.user.is_staff:
            return queryset

        # If user is staff : can view details of other user
        return queryset.filter(username=request.user)
