from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# Return full file_path for given files
def file_path(table, field, type, id, name, ext):
    return '{0}/{1}/{2}/{3}/{4}.{5}'.format(table, field, type, id, name, ext)


# Get Default User
def get_defaultUser():
    return get_user_model().objects.get(username='alfaaz')[0]


# Definition of File Manager
class Files(models.Model):
    ''' Class Modal for File manager. '''

    file_id = models.AutoField(primary_key=True, unique=True)
    ref_id = models.IntegerField()
    ref_field = models.CharField(max_length=20)
    ref_table = models.CharField(max_length=20)
    file_type = models.CharField(max_length=10)
    file_name = models.CharField(max_length=50)
    file_ext = models.CharField(max_length=5)
    file = models.FileField(upload_to=file_path)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET(get_defaultUser)) # noqa E501
    entered_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['ref_id', 'ref_field', 'ref_table'],
                         name='ref_idx')
        ]
