from django.db import models
from datetime import timedelta
from django.utils import timezone


# Definition of Case History Models
class CaseHistory(models.Model):
    ''' Class Modal for Case History. Assuming worst case scenario, One Case
    may have multiple diagnosis. Each Case history is bound to patient '''

    case_id = models.AutoField(
        primary_key=True,
        unique=True,
        help_text="Case Identification Number")
    # Case type may be Emergency | Walkin Checkup | Hospitalized Case
    case_type = models.CharField(
        max_length=10,
        help_text="Case Type")
    referral_id = models.ForeignKey(
        'referral.Referral',
        on_delete=models.CASCADE,
        help_text="Referral Identification Number",
        null=True)
    observer_id = models.ForeignKey(
        'medicalofficer.MedicalOfficer',
        on_delete=models.RESTRICT,
        help_text="Assigned Investigation Officer")
    # General observation from MO
    observation = models.CharField(
        max_length=500,
        help_text="Obvervation Summary")
    # General Tags : specific to disese type i.e. Cancer etc.
    patient_type = models.CharField(
        max_length=10,
        help_text="Patient Type")
    # Corresponding user identity
    patient = models.ForeignKey(
        'user.User',
        on_delete=models.RESTRICT,
        help_text="Patient Username")
    # Current condition and ward information
    case_status = models.CharField(
        max_length=3,
        help_text="Case Status")
    # Department currently handling the case
    department = models.ForeignKey(
        'hospitalinfo.DepartmentInformation',
        on_delete=models.CASCADE,
        help_text="Related Department")
    # Patient admit date
    entered_date = models.DateTimeField(auto_now_add=True)
    # Last updated record on
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['case_type'],
                         name="casety_idx"),
            models.Index(fields=['case_status', 'department'],
                         name="status_idx"),
            models.Index(fields=['entered_date'],
                         name="admitdate_idx"),
            models.Index(fields=['patient_type'],
                         name="patient_idx"),
        ]

# Definition of Case History Models


class Diagnosis(models.Model):
    ''' Class Modal for Diagnosis History. Assuming worst case scenario,
    may have multiple medication. Each Diagnosis history is bound to
    Case History '''

    diagnosis_id = models.AutoField(
        unique=True,
        primary_key=True,
        help_text="Diagnoisis Id")
    case_id = models.ForeignKey(
        'CaseHistory',
        on_delete=models.CASCADE,
        help_text="Related Case Id")
    # general observation reported by MO
    observation = models.CharField(
        max_length=2500,
        help_text="Observation Summary")
    # known symptoms from patient
    symptoms = models.CharField(
        max_length=2500,
        help_text="Symptoms")
    # allergies specific to diagnosis periods i.e. related to medicine
    allergies = models.CharField(
        max_length=10,
        help_text="Recorded allergies")
    # is lab work required i.e. blood test / Scans etc.
    is_investigation_req = models.BooleanField(
        default=False,
        help_text="Require additioanl Investiagtion")
    # Date of the diagnosis
    diagnose_date = models.DateTimeField(
        auto_now_add=True,
        help_text="Diagnosis Date")
    # Follow up Check up Date
    followup_date = models.DateTimeField(help_text="Follow up date")

    class Meta:
        indexes = [
            models.Index(fields=['diagnose_date'],
                         name="diagnosedt_idx"),
            models.Index(fields=['followup_date'],
                         name="follow_idx"),
        ]

# Definition for Investigation and Lab Test


class InvestigationHistory(models.Model):
    ''' Class Modal for Investigation History. Assuming worst case scenario,
    may have multiple Investiagtion Records. Each Investigation history is
    bound to a specific Diagnosis '''
    investigation_id = models.AutoField(
        unique=True,
        primary_key=True,
        help_text="Investigation Id")
    diagnosis_id = models.ForeignKey(
        'Diagnosis',
        on_delete=models.CASCADE,
        help_text="Related Diagnosis")
    # Originally planned investigation appointment date
    planned_date = models.DateTimeField(help_text="Planned investigation date")
    # Type of Investigation
    investigation_type = models.CharField(
        max_length=5,
        help_text="Type of Investigtaion")
    # Investigation Performed date
    investigation_date = models.DateTimeField(help_text="Investigated Date")
    permfomed_by = models.ForeignKey(
        'medicalofficer.MedicalOfficer',
        on_delete=models.CASCADE,
        null=True,
        help_text="Investigating Officer")
    # is results available in system
    is_complete = models.BooleanField(
        default=True,
        help_text="Is investigation Complete")
    # Direction to pre investigation. eg. Fasting required
    pre_remarks = models.CharField(
        max_length=500,
        help_text="Specific remarks prior to investigation")
    remarks = models.CharField(
        max_length=500,
        help_text="Remarks after Investigation")

    class Meta:
        indexes = [
            models.Index(fields=['investigation_date'],
                         name="invdt_idx"),
            models.Index(fields=['investigation_type'],
                         name="invty_idx"),
        ]

# Definition related to medication


class Medication(models.Model):
    ''' Class Modal for Medication History. Hold related information in order
    to view any conflicting medication options/ help patient consume right
    doseage of medicine '''

    diagnosis_id = models.ForeignKey(
        'Diagnosis',
        on_delete=models.CASCADE,
        help_text="Related Diagnosis Id")
    # Code representing type : Oral / Ointment / General / Antibioitc or Other
    medicine_type = models.CharField(
        max_length=4,
        help_text="Medicine Type")
    # Days in int to continue
    duration = models.IntegerField(help_text="Duration Use")
    # Usage directions if any
    usage_remarks = models.CharField(
        max_length=500,
        help_text="Usage Remarks")
    # name of medicine : composition, may be sustituted with alternate
    medicine = models.CharField(
        max_length=30,
        help_text="Name of Medicine")
    # general name for medicine
    general_name = models.CharField(
        max_length=50,
        help_text="Alternative/General Name")
    # doseage amount in integer
    dose = models.IntegerField(help_text="Dose")
    # measure of dosage may be gm , ml , cc or viable options
    dose_measure = models.CharField(
        max_length=5,
        help_text="Dose measure")
    # any pre known side effects
    side_effects = models.CharField(
        max_length=200,
        help_text="Known Side Effects")
    # start date of consumption
    start_date = models.DateTimeField(
        auto_now_add=True,
        help_text="Start Date")

    # is patient still using or supposed to use the medicine
    @property
    def is_active(self):
        '''Returns if the blocklist is active.'''

        end_date = self.start_date + timedelta(days=self.duration)
        # Block is effective within the duration specified
        return timezone.now() <= end_date

    class Meta:
        indexes = [
            models.Index(fields=['duration', 'medicine_type'],
                         name="medtype_idx"),
            models.Index(fields=['dose', 'dose_measure'],
                         name="doseage_idx"),
        ]
