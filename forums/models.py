from django.db import models

# Model for Staff Information.


class Forums(models.Model):
    thread_id = models.AutoField(unique=True, primary_key=True)
    thread_title = models.CharField(
        max_length=1000,
        help_text='Title of Discussion')
    tags = models.SlugField(
        max_length=200,
        help_text='Tags for Search')
    is_closed = models.BooleanField(
        default=False,
        help_text='Marked as closed')
    created_by = models.ForeignKey(
        'user.User',
        to_field='username',
        on_delete=models.CASCADE,
        help_text='Created By User')
    created_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Date of Creation')
    updated_date = models.DateTimeField(
        auto_now=True,
        help_text='Last Update Date')

    @property
    def user(self):
        """ Returns the user of the thread comment """
        return self.created_by

    class Meta:
        indexes = [
            models.Index(fields=['tags'], name='tags_idx'),
            models.Index(fields=['is_closed', 'created_by'], name="user_idx"),
            models.Index(fields=['is_closed', 'created_date'], name="created_idx")  # noqa E501
        ]

# Model for thread discussion


class Discussion(models.Model):
    discussion_id = models.AutoField(unique=True, primary_key=True)
    thread_id = models.ForeignKey(
        'Forums',
        on_delete=models.RESTRICT,
        help_text='Main Conversation Thread')
    message = models.CharField(
        max_length=5000,
        help_text='User Comment')
    created_by = models.ForeignKey(
        'user.User',
        to_field='username',
        on_delete=models.CASCADE,
        help_text='Created By User')
    created_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Date of Comment')

    @property
    def user(self):
        """ Returns the instance of the user for the thread comment """
        return self.created_by

    class Meta:
        get_latest_by = ['created_date']
