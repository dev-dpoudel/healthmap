# Generated by Django 3.1.4 on 2021-01-31 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filemanager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='created_by',
            field=models.ForeignKey(help_text='Created By User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AddIndex(
            model_name='files',
            index=models.Index(fields=['ref_id', 'ref_field', 'ref_table'], name='ref_idx'),
        ),
    ]
