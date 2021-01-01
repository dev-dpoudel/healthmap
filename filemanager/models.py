from django.db import models


# Return full file_path for given files
def file_path(table, field, type, id, name, ext):
    return '{0}/{1}/{2}/{3}/{4}.{5}'.format(table, field, type, id, name, ext)


# Definition of File Manager
class Files(models.Model):
    ''' Class Modal for File manager. '''

    file_id = models.AutoField(primary_key=True, unique=True)
    ref_id = models.IntegerField()
    ref_field = models.CharField()
    ref_table = models.CharField()
    file_type = models.CharField(max_length=10)
    file_name = models.CharField(max_length=50)
    file_ext = models.CharField(max_length=5)
    file = models.FileField(upload_to=file_path)
    user = models.ForeignField('user.User')
    entered_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        index = [
            models.Index(fields=['ref_id', 'ref_field', 'ref_table'],
                         name='ref_idx')
        ]
