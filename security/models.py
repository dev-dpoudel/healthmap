from django.db import models
from datetime import timedelta
from django.utils import timezone


# Hospital Information Model.
class Blocklist(models.Model):
    ip = models.GenericIPAddressField(
        unique=True,
        help_text="IP address of the user")
    type = models.CharField(
        max_length=4,
        help_text="Type of Block List")
    reason = models.CharField(
        max_length=200,
        help_text="Reason Blocklisted")
    entereddt = models.DateTimeField(
        auto_now_add=True,
        help_text="Block List active Date")
    duration = models.PositiveIntegerField(
        default=1,
        help_text="Duration of blocklist active in days")

    @property
    def is_active(self):
        "Returns if the blocklist is active."

        if self.duration == 0:
            return True

        end_date = self.entereddt + timedelta(days=self.duration)
        # Block is effective within the duration specified
        return timezone.now() <= end_date

    class Meta:
        indexes = [
            models.Index(fields=['ip'], name='ipaddr_idx'),
            models.Index(fields=['entereddt', 'type'],
                         name='activated_idx')
        ]


# Department Information Model.
class Incidence(models.Model):
    type = models.CharField(
        max_length=4,
        help_text="Type of Incidence Reported")
    # User may be anonymous: DDOS/ DoS attacks / Pshising / ARP poision / CSRF
    user = models.ForeignKey(
        'user.User',
        to_field='username',
        on_delete=models.CASCADE,
        help_text='Related User',
        null=True)
    ip = models.GenericIPAddressField(
        help_text="Requesting IP Address")
    entereddt = models.DateTimeField(
        auto_now_add=True,
        help_text="Incidence Report Date Time")
