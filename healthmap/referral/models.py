from django.db import models

# Definition related to medication


class Referral(models.Model):
    referral_id = models.AutoField(unique=True, primary_key=True)
    referral_type = models.CharField(max_length=3)
    refered_by = models.ForeignKey('medicalofficer.MedicalOfficer')
    refered_from = models.CharField(max_length=50)
    refered_to = models.CharField(max_length=50)
    refered_date = models.DateTimeField()
    refered_remarks = models.CharField(max_length=100)
