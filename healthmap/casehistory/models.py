from django.db import models


# Definition of Case History Models
class CaseHistory(models.Model):
    ''' Class Modal for Case History. Assuming worst case scenario, One Case
    may have multiple diagnosis. Each Case history is bound to patient '''

    case_id = models.AutoField(primary_key=True, unique=True)
    # Case type may be Emergency | Walkin Checkup | Hospitalized Case
    case_type = models.CharField(max_length=10)
    referral_id = models.ForeignKey('Referral', on_delete=models.CASCADE)
    observer_id = models.ForeignKey('MedicalOfficer')
    # General observation from MO
    observation = models.CharField(max_length=500)
    # General Tags : specific to disese type i.e. Cancer etc.
    patient_type = models.CharField(max_length=10)
    # Corresponding user identity
    patient_id = models.IntField(default=0)
    # Current condition and ward information
    case_status = models.CharField(max_length=3)
    # Department currently handling the case
    case_department = models.CharField(max_length=3)
    # Patient admit date
    entered_date = models.DateTimeField(auto_now_add=True)
    # Last updated record on
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
                models.Index(fields=['case_type'], name="type_idx"),  # noqa E501
                models.Index(fields=['case_status', 'department'], name="status_idx"),  # noqa E501
                models.Index(fields=['entered_date'], name="admitdate_idx"),
                models.Index(fields=['patient_type'], name="patient_idx"),
                ]

# Definition of Case History Models


class Diagnosis(models.Model):
    ''' Class Modal for Diagnosis History. Assuming worst case scenario,
    may have multiple medication. Each Diagnosis history is bound to
    Case History '''

    diagnosis_id = models.AutoField(unique=True, primary_key=True)
    case_id = models.ForeignKey('CaseHistory')
    # general observation reported by MO
    observation = models.CharField(max_length=2500)
    # known symptoms from patient
    symptoms = models.CharField(max_length=2500)
    # allergies specific to diagnosis periods i.e. related to medicine
    allergies = models.CharField(max_length=10)
    # is lab work required i.e. blood test / Scans etc.
    is_investigation_req = models.BooleanFiled(default=False)
    # Date of the diagnosis
    diagnose_date = models.DateTimeField(auto_now_add=True)
    # Follow up Check up Date
    followup_date = models.DateTimeField()

    class Meta:
        indexes = [
                    models.Index(fields=['diagnose_date'], name="diagnosedt_idx"),  # noqa E501
                    models.Index(fields=['followup_date'], name="follow_idx"),
                    ]

# Definition for Investigation and Lab Test


class InvestigationHistory(models.Model):
    ''' Class Modal for Investigation History. Assuming worst case scenario,
    may have multiple Investiagtion Records. Each Investigation history is
    bound to a specifiv Diagnosis '''
    investigation_id = models.AutoField(unique=True, primary_key=True)
    diagnosis_id = models.ForeignKey('Diagnosis')
    # Originally planned investigation appointment date
    planned_date = models.DateTimeField()
    # Type of Investigation
    investigation_type = models.CharField(max_length=5)
    # Investigation Performed date
    investigation_date = models.DateTimeField()
    permofrmed_by = models.ForeignKey('medicalofficer.MedicalOfficer')
    # is results available in system
    is_complete = models.BooleanFiled(default=True)
    # Direction to pre investigation. eg. Fasting required
    pre_remarks = models.CharField(max_length=500)
    remarks = models.CharField(max_length=500)

    class Meta:
        indexes = [
                    models.Index(fields=['investigation_date'], name="invdt_idx"),  # noqa E501
                    models.Index(fields=['investigation_type'], name="invty_idx"),  # noqa E501
                        ]

# Definition related to medication


class Medication(models.Model):
    ''' Class Modal for Medication History. Hold related information in order
    to view any conflicting medication options/ help patient consume right
    doseage of medicine '''

    diagnosis_id = models.ForeignKey('Diagnosis')
    # Code representing type : Oral / Ointment / General / Antibioitc or Other
    medicine_type = models.CharField(max_length=4)
    # Days in int to continue
    duration_use = models.IntField()
    # Usage amount per day
    usage = models.CharField()
    # Usage directions if any
    usage_remarks = models.CharField(max_length=500)
    # name of medicine : composition, may be sustituted with alternate
    medicine = models.CharField(max_length=30)
    # general name for medicine
    general_name = models.CharFiled(max_length=10)
    # doseage amount in integer
    dose = models.IntField()
    # measure of dosage may be gm , ml , cc or viable options
    dose_measure = models.CharFiled(max_length=5)
    # any pre known side effects
    side_effects = models.CharField(max_length=200)
    # start date of consumption
    start_date = models.DateTimeField(auto_now_add=True)
    # is patient still using or supposed to use the medicine
    is_active = models.BooleanFiled(default=True)

    class Meta:
        indexes = [
                    models.Index(fields=['is_active'], name="active_idx"),
                    models.Index(fields=['medicine_type'], name="type_idx"),
                    models.Index(fields=['dose', 'dose_measure'], name="doseage_idx"),  # noqa E501
                        ]
