# Generated by Django 3.1.4 on 2021-01-31 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('referral', '0001_initial'),
        ('casehistory', '0002_auto_20210131_1309'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='casehistory',
            name='patient_id',
            field=models.ForeignKey(help_text='Patient Id', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='referral_id',
            field=models.ForeignKey(help_text='Referral Identification Number', null=True, on_delete=django.db.models.deletion.CASCADE, to='referral.referral'),
        ),
        migrations.AddIndex(
            model_name='medication',
            index=models.Index(fields=['duration', 'medicine_type'], name='medtype_idx'),
        ),
        migrations.AddIndex(
            model_name='medication',
            index=models.Index(fields=['dose', 'dose_measure'], name='doseage_idx'),
        ),
        migrations.AddIndex(
            model_name='investigationhistory',
            index=models.Index(fields=['investigation_date'], name='invdt_idx'),
        ),
        migrations.AddIndex(
            model_name='investigationhistory',
            index=models.Index(fields=['investigation_type'], name='invty_idx'),
        ),
        migrations.AddIndex(
            model_name='diagnosis',
            index=models.Index(fields=['diagnose_date'], name='diagnosedt_idx'),
        ),
        migrations.AddIndex(
            model_name='diagnosis',
            index=models.Index(fields=['followup_date'], name='follow_idx'),
        ),
        migrations.AddIndex(
            model_name='casehistory',
            index=models.Index(fields=['case_type'], name='casety_idx'),
        ),
        migrations.AddIndex(
            model_name='casehistory',
            index=models.Index(fields=['case_status', 'department'], name='status_idx'),
        ),
        migrations.AddIndex(
            model_name='casehistory',
            index=models.Index(fields=['entered_date'], name='admitdate_idx'),
        ),
        migrations.AddIndex(
            model_name='casehistory',
            index=models.Index(fields=['patient_type'], name='patient_idx'),
        ),
    ]
