from django.db import models
from helper.models.owner import HiddenOwnerMixin
# Receive the pre_delete signal and delete associated files
from django.db.models.signals import (pre_delete)
from django.dispatch.dispatcher import receiver


# Definition of File Manager
class Files(HiddenOwnerMixin):
    ''' Class Modal for File manager. '''

    file_id = models.AutoField(primary_key=True, unique=True)
    ref_id = models.IntegerField(help_text="Related Record id")
    ref_field = models.CharField(
        max_length=20,
        help_text="Related Field Name")
    ref_table = models.CharField(
        max_length=20,
        help_text="Records related to Table")
    file_type = models.CharField(
        max_length=10,
        help_text="Type of File eg. XRAY, CT-SCAN")
    file = models.FileField(
        upload_to="attachment/",
        help_text="attachment files")
    created_by = models.ForeignKey(
        'user.User',
        to_field='username',
        on_delete=models.CASCADE,
        help_text='Created By User')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x / 1000, 2)
            ext = ' kb'
        elif x < y * 1000:
            value = round(x / 1000000, 2)
            ext = ' Mb'
        else:
            value = round(x / 1000000000, 2)
            ext = ' Gb'
        return str(value) + ext

    @property
    def filename(self):
        return self.file.name

    class Meta:
        indexes = [
            models.Index(fields=['ref_id', 'ref_field', 'ref_table'],
                         name='ref_idx')
        ]


@receiver(pre_delete, sender=Files)
def files_delete(sender, instance, **kwargs):
    # Delete the attached files.
    instance.file.delete(save=False)
