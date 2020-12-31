from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta


# Model Information for Medical Officers.
class MedicalOfficer(models.Model):
    ''' Class Modal for Medical Officer.'''

    officer_id = models.AutoField(primary_key=True, unique=True)
    username = models.ForeignKey('user.User', on_delete=models.CASCADE)
    staff_id = models.ForeignKey('patients.StaffPersons')
    position = models.CharField(max_length=20)
    department = models.CharField(max_length=10)
    join_date = models.DateTimeField()
    leave_date = models.DateTimeField()
    entered_by = models.ForeignKey('user')
    entered_date = models.DateTimeField(auto_now_add=True)

    @property
    def service_period(self):
        "Returns the person's age."
        if (self.leave_date is None):
            service = relativedelta(date.today(), self.join_date)

        else:
            service = relativedelta(self.leave_date, self.join_date)

        return {"year": service.years, "month": service.months,
                "days": service.days}
