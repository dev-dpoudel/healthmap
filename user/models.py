from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import date
from dateutil.relativedelta import relativedelta
# User Class for Custom AuthenticationMiddleware.


class User (AbstractUser):
    ''' Inherits all base attributes and fields from Abstract User from Auth
        Extending the base nodel with additional informations.
    '''
    birth_date = models.DateField(
        default=timezone.now,
        help_text='Date of Birth')
    country = models.CharField(
        max_length=20,
        null=True,
        help_text='Country Name')
    current_city = models.CharField(
        max_length=25,
        null=True,
        help_text='Current City')
    current_address = models.CharField(
        max_length=100,
        null=True,
        help_text='Current Address')
    permanent_address = models.CharField(
        max_length=100,
        null=True,
        help_text='Permanent Address')
    # In Reference to E16.4 max_length(phone_number) eq 15
    phone_number = models.CharField(
        max_length=15,
        null=True,
        help_text='Default Contact Number')
    blood_group = models.CharField(
        max_length=7,
        null=True,
        help_text='Blood Group and Type')
    allergies = models.CharField(
        max_length=500,
        null=True,
        help_text='Known Allergies')
    emergency_contact = models.CharField(
        max_length=50,
        null=True,
        help_text='Contact Number inCase of Emergency')
    contact_relation = models.CharField(
        max_length=20,
        null=True,
        help_text='Relation to User')
    modified_date = models.DateField(
        default=timezone.now,
        help_text='Modified Date')
    entered_by = models.CharField(
        max_length=20,
        null=True,
        help_text='Username performing data Audit')

    @property
    def age(self):
        "Returns the person's age."
        age = relativedelta(date.today(), self.birth_date)
        return {"year": age.years, "month": age.months, "days": age.days}

    class Meta:
        indexes = [
            models.Index(fields=['username'], name='username_idx'),
            models.Index(fields=['first_name', 'last_name'], name='name_idx'),
            models.Index(fields=['blood_group'], name='bloodgroup_idx')
        ]

        unique_together = [('username')]


class Scope (models.Model):
    ''' Menu Set and Menu Related to the User Group
        User Group is used for ease of management.
    '''
    menu_set = models.CharField(
        max_length=15,
        unique=True,
        primary_key=True,
        help_text='Menu Sets')
    menu = models.CharField(
        max_length=15,
        null=True,
        help_text='Menu')
    action = models.CharField(
        max_length=15,
        null=True,
        help_text='Action Supported')
    groups = models.ManyToManyField('auth.Group')

    @property
    def menu_type(self):
        "Returns the menu's action."
        return "%s_%s" % (self.menu, self.action)

    class Meta:
        unique_together = [('menu', 'action')]
