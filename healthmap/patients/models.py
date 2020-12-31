from django.db import models


# Base Model for Patient Information
class Patients(models.Model):
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    entered_by = models.CharField(max_length=20)

    # define as a abstract base class
    class Meta:
        abstract = True


# Model for Staff Information.
class StaffPersons(Patients):
    staff_id = models.AutoField(unique=True, primary_key=True)
    username = models.ForeignKey('user.User', on_delete=models.CASCADE)
    is_hospital_staff = models.BooleanFiled(default=False)
    staff_post = models.CharField(max_length=25)

    class Meta(Patients.Meta):
        pass


# Model for Staff Family
class StaffFamily(Patients):
    staff_id = models.ForeignKey('StaffPersons', on_delete=models.CASCADE)
    username = models.ForeignKey('user.User', on_delete=models.CASCADE)
    relation = models.CharField(max_length=20)
    relation_id = models.AutoField(unique=True, primary_key=True)
    is_billable = models.BooleanFiled(default=False)

    class Meta(Patients.Meta):
        pass
