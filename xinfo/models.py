from django.db import models
from django.utils import timezone


# Create your models here.
class XSettings(models.Model):
    ''' Additional settings for systems
    '''
    tablespace = models.CharField(
        max_length=15,
        null=True,
        help_text='Table Code')
    identity = models.CharField(
        max_length=20,
        null=True,
        help_text='Additioanl Settings Identity Code')
    code = models.CharField(
        max_length=10,
        null=True,
        help_text='Additioanl Settings Unique Code')
    value = models.CharField(
        max_length=150,
        help_text='')
    active = models.BooleanField(
        default=True,
        help_text='Enable on Selection')
    modified_date = models.DateField(
        default=timezone.now,
        help_text='Modified Date')

    class Meta:
        unique_together = [['tablespace', 'identity', 'code']]
        indexes = [
            models.Index(fields=['identity', 'code'], name='xinfo_idx'),
        ]
