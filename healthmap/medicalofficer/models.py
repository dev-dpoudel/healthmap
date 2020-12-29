from django.db import models

# Create your models here.


class MedicalOfficer(models.Model):
    ''' Class Modal for Medical Officer.'''

    officer_id = models.AutoField(primary_key=True, unique=True)
    position = models.CharField(max_length=20)
    department = models.CharField(max_length=10)
    is_active = models.BooleanFiled(deafult=True)
    join_date = models.DateTimeField()
