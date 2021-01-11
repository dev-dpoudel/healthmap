from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model


# Get Default User
def get_defaultUser():
    return get_user_model().objects.get(username='alfaaz')[0]


# Model Information for Medical Officers.
class MedicalOfficer(models.Model):
    ''' Class Modal for Medical Officer.'''

    officer_id = models.AutoField(primary_key=True, unique=True)
    staff_id = models.ForeignKey('patients.StaffPersons',
                                 on_delete=models.RESTRICT)
    position = models.CharField(max_length=20)
    department = models.ForeignKey('hospitalinfo.DepartmentInformation',
                                   on_delete=models.CASCADE)
    join_date = models.DateTimeField()
    leave_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def service_period(self):
        "Returns the person's age."
        if (self.leave_date is None):
            service = relativedelta(date.today(), self.join_date)

        else:
            service = relativedelta(self.leave_date, self.join_date)

        return {"year": service.years, "month": service.months,
                "days": service.days}

        class Meta:
            indexes = [
                models.Index(fields=['position', 'department'], name="post_idx"),  # noqa E501
                models.Index(fields=['join_date'], name="joindate_idx")
                ]

            permissions = ['patient_case',
                           'patients_diagnoisis',
                           'patients_medication',
                           'patients_investigation',
                           ]
