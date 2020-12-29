from django.db import models


# Model for Staff Information.
class Forums(models.Model):
    thread_id = models.AutoField(unique=True, primary_key=True)
    thread_title = models.CharFiled(max_length=1000)
    tags = models.SlugField(max_length=50)
    is_closed = models.BooleanFiled(default=False)
    created_by = models.BooleanFiled(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


# Model for thread discussion
class Discussion(models.Model):
    discussion_id = models.AutoField(unique=True, primary_key=True)
    thread_id = models.ForeignKey('Forums', on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    created_by = models.BooleanFiled(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = ['created_date']
