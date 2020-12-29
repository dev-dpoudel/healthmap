# File contains custom Validation for Patients
from django.core.validators import RegexValidator


# Function to validate phone numbers
# Using annotations
def validate_phone(phone_number: str) -> type:
    ''' Function to validate phone number of a user '''
    return RegexValidator(regex='[^+\\w\\s]', inverse_match=True)
