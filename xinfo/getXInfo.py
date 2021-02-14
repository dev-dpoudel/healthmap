from .models import XSettings
from django.core.exceptions import ObjectDoesNotExist


# Defines the get method for XSetting Information
def get_xSettings(**Kwargs) -> str:
    '''
    Get XSettings related to input query filters
    '''
    try:

        # Get Type from extra Settings
        type = XSettings.objects.get(**Kwargs).value

    # In Case Type Doesn't exist: Object Doesn't exist is thrown
    except ObjectDoesNotExist:
        type = "No Records"

    return type


# Defines the list method for XSetting Information
def list_xSettings(**Kwargs) -> list:
    '''
        List XSettings related to input query parameters
    '''
    # Get Type from extra Settings
    type_list = XSettings.objects.filter(**Kwargs)

    return type_list
