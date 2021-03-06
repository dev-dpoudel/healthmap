# Generated by Django 3.1.4 on 2021-02-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0002_auto_20210202_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='referral_type',
            field=models.CharField(choices=[('IDEP', 'Internal Department'), ('IHSP', 'Inter Hospital Specialist'), ('IHGE', 'Inter Hospital General')], default='IDEP', help_text='Referral Type', max_length=4),
        ),
    ]
