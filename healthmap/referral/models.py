from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Definition related to Referral : Departmental or Inter Hospital
class Referral(models.Model):

    class ReferralType(models.TextChoices):
        INTRADEPT = 'IDEP', _('Internal Department')
        OUTDEPT = 'IHSP', _('Inter Hospital Specialist')
        OUTHOSPITAL = 'IHGE', _('Inter Hospital General')

    referral_id = models.AutoField(
        unique=True,
        primary_key=True,
        help_text="Referral Identification Number")
    # Referral Type Code
    referral_type = models.CharField(
        max_length=4,
        choices=ReferralType.choices,
        default=ReferralType.INTRADEPT,
        help_text="Referral Type")
    # Referring Personal Information
    refered_by = models.ForeignKey(
        'medicalofficer.MedicalOfficer',
        on_delete=models.CASCADE,
        help_text="Referred By")
    # Information of Referral Source : Hospital and Department
    refered_from = models.CharField(
        max_length=50,
        help_text="Refered From ")
    # Information to be picked by : Hospital and Department
    refered_to = models.CharField(
        max_length=50,
        help_text="Refered To")
    # Date of Referral Requested
    refered_date = models.DateTimeField(default=timezone.now)
    # Additional/ Supporting  Information
    refered_remarks = models.CharField(
        max_length=100,
        help_text="Refered Remarks")

    class Meta:
        indexes = [
            models.Index(fields=['refered_by'],
                         name="referby_idx"),
            models.Index(fields=['referral_type', 'refered_from'],
                         name="from_idx"),
        ]
