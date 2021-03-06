# Generated by Django 3.1.4 on 2021-02-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casehistory', '0005_auto_20210203_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casehistory',
            name='case_type',
            field=models.CharField(help_text='Case Type', max_length=4),
        ),
        migrations.AlterField(
            model_name='casehistory',
            name='patient_type',
            field=models.CharField(help_text='Patient Type', max_length=4),
        ),
        migrations.AlterField(
            model_name='investigationhistory',
            name='investigation_type',
            field=models.CharField(help_text='Type of Investigtaion', max_length=4),
        ),
    ]
