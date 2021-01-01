from django.db import models


# Model for Staff Information.
class Forums(models.Model):
    thread_id = models.AutoField(unique=True, primary_key=True)
    thread_title = models.CharField(max_length=1000)
    tags = models.SlugField(max_length=200)
    is_closed = models.BooleanField(default=False)
    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE) # noqa E501
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['tags'], name='tags_idx'),
            models.Index(fields=['is_closed', 'created_by'], name="user_idx"),
            models.Index(fields=['is_closed', 'created_date'], name="created_idx")  # noqa E501
        ]

# Model for thread discussion


class Discussion(models.Model):
    discussion_id = models.AutoField(unique=True, primary_key=True)
    thread_id = models.ForeignKey('Forums', on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    created_by = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = ['created_date']
