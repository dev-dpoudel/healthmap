# Generated by Django 3.1.4 on 2021-01-31 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseHistory',
            fields=[
                ('case_id', models.AutoField(help_text='Case Identification Number', primary_key=True, serialize=False, unique=True)),
                ('case_type', models.CharField(help_text='Case Type', max_length=10)),
                ('observation', models.CharField(help_text='Obvervation Summary', max_length=500)),
                ('patient_type', models.CharField(help_text='Patient Type', max_length=10)),
                ('case_status', models.CharField(help_text='Case Status', max_length=3)),
                ('entered_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosis_id', models.AutoField(help_text='Diagnoisis Id', primary_key=True, serialize=False, unique=True)),
                ('observation', models.CharField(help_text='Observation Summary', max_length=2500)),
                ('symptoms', models.CharField(help_text='Symptoms', max_length=2500)),
                ('allergies', models.CharField(help_text='Recorded allergies', max_length=10)),
                ('is_investigation_req', models.BooleanField(default=False, help_text='Require additioanl Investiagtion')),
                ('diagnose_date', models.DateTimeField(auto_now_add=True, help_text='Diagnosis Date')),
                ('followup_date', models.DateTimeField(help_text='Follow up date')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_type', models.CharField(help_text='Medicine Type', max_length=4)),
                ('duration', models.IntegerField(help_text='Duration Use')),
                ('usage_remarks', models.CharField(help_text='Usage Remarks', max_length=500)),
                ('medicine', models.CharField(help_text='Name of Medicine', max_length=30)),
                ('general_name', models.CharField(help_text='Alternative/General Name', max_length=50)),
                ('dose', models.IntegerField(help_text='Dose')),
                ('dose_measure', models.CharField(help_text='Dose measure', max_length=5)),
                ('side_effects', models.CharField(help_text='Known Side Effects', max_length=200)),
                ('start_date', models.DateTimeField(auto_now_add=True, help_text='Start Date')),
                ('diagnosis_id', models.ForeignKey(help_text='Related Diagnosis Id', on_delete=django.db.models.deletion.CASCADE, to='casehistory.diagnosis')),
            ],
        ),
        migrations.CreateModel(
            name='InvestigationHistory',
            fields=[
                ('investigation_id', models.AutoField(help_text='Investigation Id', primary_key=True, serialize=False, unique=True)),
                ('planned_date', models.DateTimeField(help_text='Planned investigation date')),
                ('investigation_type', models.CharField(help_text='Type of Investigtaion', max_length=5)),
                ('investigation_date', models.DateTimeField(help_text='Investigated Date')),
                ('is_complete', models.BooleanField(default=True, help_text='Is investigation Complete')),
                ('pre_remarks', models.CharField(help_text='Specific remarks prior to investigation', max_length=500)),
                ('remarks', models.CharField(help_text='Remarks after Investigation', max_length=500)),
                ('diagnosis_id', models.ForeignKey(help_text='Related Diagnosis', on_delete=django.db.models.deletion.CASCADE, to='casehistory.diagnosis')),
            ],
        ),
    ]
