# Generated by Django 3.1.4 on 2021-02-02 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicalofficer', '0002_medicalofficer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalofficer',
            name='username',
            field=models.ForeignKey(help_text='Username', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
