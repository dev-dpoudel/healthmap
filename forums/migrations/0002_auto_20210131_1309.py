# Generated by Django 3.1.4 on 2021-01-31 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forums', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='forums',
            name='created_by',
            field=models.ForeignKey(help_text='Created By User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='created_by',
            field=models.ForeignKey(help_text='Created By User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='thread_id',
            field=models.ForeignKey(help_text='Main Conversation Thread', on_delete=django.db.models.deletion.RESTRICT, to='forums.forums'),
        ),
        migrations.AddIndex(
            model_name='forums',
            index=models.Index(fields=['tags'], name='tags_idx'),
        ),
        migrations.AddIndex(
            model_name='forums',
            index=models.Index(fields=['is_closed', 'created_by'], name='user_idx'),
        ),
        migrations.AddIndex(
            model_name='forums',
            index=models.Index(fields=['is_closed', 'created_date'], name='created_idx'),
        ),
    ]
