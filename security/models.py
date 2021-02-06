from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Blocklist Information Model.
class Blocklist(models.Model):

    class BlocklistType(models.TextChoices):
        GENERAL = 'GEN', _('General')  # Added in response to collected data
        PREDEF = 'PDEF', _('Pre Defined')  # List of IP added pre production
        NIDS = 'NDS', _('Network Intrusuion')  # Possible Threat Cause

    ip = models.GenericIPAddressField(
        unique=True,
        help_text="IP address of the user")
    type = models.CharField(
        max_length=4,
        choices=BlocklistType.choices,
        default=BlocklistType.GENERAL,
        help_text="Type of Block List")
    reason = models.CharField(
        max_length=200,
        help_text="Reason Blocklisted")
    entered_date = models.DateTimeField(
        auto_now_add=True,
        help_text="Block List active Date")
    start_date = models.DateTimeField(
        default=timezone.now,
        help_text="Block List active Date")
    duration = models.PositiveIntegerField(
        default=1,
        help_text="Duration Blocklisted")

    @property
    def is_active(self):
        "Returns if the blocklist is active."

        # Duration 365 requires admin intervention
        if self.duration == 365:
            return True

        # Per Current Standard 0 is used for in-active block list
        if self.duration == 0:
            return False

        end_date = self.start_date + timedelta(days=self.duration)
        # Block is effective within the duration specified
        return timezone.now() <= end_date

    class Meta:
        indexes = [
            models.Index(fields=['ip'], name='ipaddr_idx'),
            models.Index(fields=['entered_date', 'type'],
                         name='activated_idx')
        ]


# Department Information Model.
class Incidence(models.Model):

    class IncidenceSource(models.TextChoices):
        GENERAL = 'GEN', _('General')
        CYBERSEC = 'CS', _('Cyber Security')
        NIDS = 'NDS', _('Network Intrusuion')

    class IncidenceType(models.TextChoices):
        VIOLATE = 'AV', _('Access Violation')
        ARPPOISION = 'ARP', _('ARP Poisioning')
        MALWARE = 'MAL', _('Malicious Code')
        EVEDROP = 'EDP', _('Eves Dropping')

    # User may be anonymous: DDOS/ DoS attacks / Pshising / ARP poision / CSRF
    source = models.CharField(
        max_length=4,
        choices=IncidenceSource.choices,
        default=IncidenceSource.GENERAL,
        help_text="Type of Incidence Source")

    type = models.CharField(
        max_length=4,
        choices=IncidenceType.choices,
        default=IncidenceType.VIOLATE,
        help_text="Type of Incidence Reported")

    user = models.ForeignKey(
        'user.User',
        to_field='username',
        on_delete=models.CASCADE,
        help_text='Related User',
        null=True)
    ip = models.GenericIPAddressField(
        help_text="Requesting IP Address")
    entered_date = models.DateTimeField(
        auto_now_add=True,
        help_text="Incidence Report Date Time")
