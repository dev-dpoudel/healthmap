# Generated by Django 3.1.4 on 2021-01-31 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpersons',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stafffamily',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.staffpersons'),
        ),
        migrations.AddField(
            model_name='stafffamily',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='staffpersons',
            index=models.Index(fields=['is_hospital_staff'], name='staff_idx'),
        ),
        migrations.AddIndex(
            model_name='stafffamily',
            index=models.Index(fields=['is_billable'], name='billable_idx'),
        ),
    ]
