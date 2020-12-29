from django.db import models
from validators import validate_phone


# Base Model for Patient Information
class Patients(models.Model):
    first_name = models.CharFiled(max_length=25)
    last_name = models.CharField(max_length=25)
    current_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    email_address = models.EmaiField()
    # In Reference to E16.4 max_length(phone_number) eq 15
    phone_number = models.CharField(max_length=15, validators=[validate_phone])
    allergies = models.CharField(max_length=500)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    entered_by = models.CharField(max_length=20)

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    def __repr__(self):
        return 'Patient Name: %s %s' % (self.first_name, self.last_name)

    # define as a abstract base class
    class Meta:
        abstract = True
        index = [
            models.Index(fields=['first_name', 'last_name'], name='name_idx')
        ]


# Model for Staff Information.
class StaffPersons(Patients):
    staff_id = models.AutoField(unique=True, primary_key=True)
    is_hospital_staff = models.BooleanFiled(default=False)
    staff_post = models.CharField(max_length=25)

    class Meta(Patients.Meta):
        pass


# Model for Staff Family
class StaffFamily(Patients):
    staff_id = models.ForeignKey('StaffPersons', on_delete=models.CASCADE)
    relation = models.CharField(max_length=20)
    patient_id = models.AutoField(unique=True, primary_key=True)

    class Meta(Patients.Meta):
        pass
