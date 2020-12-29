from django.db import models


# Definition of Case History Models
class CaseHistory(models.Model):
    ''' Class Modal for Case History. Assuming worst case scenario, One Case
    may have multiple diagnosis. Each Case history is bound to patient '''

    case_id = models.AutoField(primary_key=True, unique=True)
    case_type = models.CharField(max_length=10)
    referral_id = models.ForeignKey('Referral', on_delete=models.CASCADE)
    observer_id = models.ForeignKey('MedicalOfficer')
    observation = models.CharField(max_length=500)
    patient_type = models.CharField(max_length=10)
    patient_id = models.IntField(default=0)
    case_status = models.CharField(max_length=3)
    case_department = models.CharField(max_length=3)
    entered_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


# Definition of Case History Models
class Diagnosis(models.Model):
    ''' Class Modal for Diagnosis History. Assuming worst case scenario,
    may have multiple medication. Each Diagnosis history is bound to
    Case History '''

    diagnosis_id = models.AutoField(unique=True, primary_key=True)
    case_id = models.ForeignKey('CaseHistory')
    observation = models.CharField(max_length=2500)
    symptoms = models.CharField(max_length=2500)
    allergies = models.CharField(max_length=10)
    is_investigation_req = models.BooleanFiled(default=False)
    diagnose_date = models.DateTimeField(auto_now_add=True)
    followup_date = models.DateTimeField()


# Definition for Investigation and Lab Test
class InvestigationHistory(models.Model):
    investigation_id = models.AutoField(unique=True, primary_key=True)
    diagnosis_id = models.ForeignKey('Diagnosis')
    investigation_type = models.CharField(max_length=5)
    investigation_date = models.DateTimeField()
    permofrmed_by = models.ForeignKey('medicalofficer.MedicalOfficer')
    is_complete = models.BooleanFiled(default=True)
    remarks = models.CharField(max_length=500)


# Definition related to medication
class Medication(models.Model):
    diagnosis_id = models.ForeignKey('Diagnosis')
    medicine_type = models.CharField(max_length=4)
    duration_use = models.IntField()
    usage = models.CharField()
    usage_remarks = models.CharField(max_length=500)
    medicine = models.CharField(max_length=30)
    general_name = models.CharFiled(max_length=10)
    dose = models.IntField()
    dose_measure = models.CharFiled(max_length=5)
    side_effects = models.CharField(max_length=200)
