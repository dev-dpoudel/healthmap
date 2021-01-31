# Generated by Django 3.1.4 on 2021-01-31 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('casehistory', '0001_initial'),
        ('hospitalinfo', '0001_initial'),
        ('medicalofficer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigationhistory',
            name='permfomed_by',
            field=models.ForeignKey(help_text='Investigating Officer', null=True, on_delete=django.db.models.deletion.CASCADE, to='medicalofficer.medicalofficer'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='case_id',
            field=models.ForeignKey(help_text='Related Case Id', on_delete=django.db.models.deletion.CASCADE, to='casehistory.casehistory'),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='department',
            field=models.ForeignKey(help_text='Related Department', on_delete=django.db.models.deletion.CASCADE, to='hospitalinfo.departmentinformation'),
        ),
        migrations.AddField(
            model_name='casehistory',
            name='observer_id',
            field=models.ForeignKey(help_text='Assigned Investigation Officer', on_delete=django.db.models.deletion.RESTRICT, to='medicalofficer.medicalofficer'),
        ),
    ]
