# Generated by Django 3.1.4 on 2021-02-03 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casehistory', '0004_auto_20210202_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='allergies',
            field=models.CharField(help_text='Recorded allergies', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='case_id',
            field=models.ForeignKey(help_text='Related Case Id', on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to='casehistory.casehistory'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='followup_date',
            field=models.DateTimeField(help_text='Follow up date', null=True),
        ),
        migrations.AlterField(
            model_name='investigationhistory',
            name='diagnosis_id',
            field=models.ForeignKey(help_text='Related Diagnosis', on_delete=django.db.models.deletion.CASCADE, related_name='investigations', to='casehistory.diagnosis'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='diagnosis_id',
            field=models.ForeignKey(help_text='Related Diagnosis Id', on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='casehistory.diagnosis'),
        ),
    ]
