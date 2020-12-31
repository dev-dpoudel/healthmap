from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from dateutil.relativedelta import relativedelta
# User Class for Custom AuthenticationMiddleware.


class User (AbstractUser):
    ''' Inherits all base attributes and fields from Abstract User from Auth
        Extending the base nodel with additional informations.
    '''
    birth_date = models.DateField(null=True)
    current_address = models.CharField(max_length=100, null=True)
    permanent_address = models.CharField(max_length=100, null=True)
    # In Reference to E16.4 max_length(phone_number) eq 15
    phone_number = models.CharField(max_length=15, null=True)
    blood_group = models.CharField(max_length=7, null=True)
    allergies = models.CharField(max_length=500, null=True)
    emergency_contact = models.CharField(max_length=50, null=True)
    contact_relation = models.CharField(max_length=20, null=True)
    modified_date = models.DateField(auto_now=True, null=True)
    entered_by = models.CharField(max_length=20, null=True)

    @property
    def age(self):
        "Returns the person's age."
        age = relativedelta(date.today(), self.birth_date)
        return {"year": age.years, "month": age.months, "days": age.days}
