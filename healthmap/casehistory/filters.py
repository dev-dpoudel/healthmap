from rest_framework import filters


# Class Extending Baseic FIlter Function to filter Owner
class IsPatientFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to edit or see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(created_by=request.user)
