from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from xinfo.getXInfo import get_xSettings


# Model Information for Medical Officers.
class MedicalOfficer(models.Model):
    ''' Class Modal for Medical Officer.'''

    officer_id = models.AutoField(
        primary_key=True,
        unique=True,
        help_text="Officer Id")
    username = models.ForeignKey(
        'user.User',
        to_field='username',
        on_delete=models.RESTRICT,
        help_text="Username")
    position = models.CharField(
        max_length=4,
        help_text="MO Position")  # May be Consultant, Dentist
    department = models.ForeignKey(
        'hospitalinfo.DepartmentInformation',
        on_delete=models.CASCADE,
        help_text="Related Department")
    join_date = models.DateTimeField(default=timezone.now)
    leave_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def service_period(self):
        "Returns the person's age."
        if (self.leave_date is None):
            service = relativedelta(timezone.now(), self.join_date)

        else:
            service = relativedelta(self.leave_date, self.join_date)

        return {"year": service.years, "month": service.months,
                "days": service.days}

    @property
    def post(self):

        return get_xSettings(tablespace="medicalofficer",
                             identity="post",
                             code=self.position)

        class Meta:
            indexes = [
                models.Index(fields=['position', 'department'],
                             name="post_idx"),
                models.Index(fields=['join_date'],
                             name="joindate_idx")
            ]

            permissions = ['patient_case',
                           'patients_diagnoisis',
                           'patients_medication',
                           'patients_investigation',
                           ]
