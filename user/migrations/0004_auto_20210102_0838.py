# Generated by Django 3.1.4 on 2021-01-02 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201231_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(help_text='Country Name', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='current_city',
            field=models.CharField(help_text='Current City', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='allergies',
            field=models.CharField(help_text='Known Allergies', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='blood_group',
            field=models.CharField(help_text='Blood Group and Type', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_relation',
            field=models.CharField(help_text='Relation to User', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='current_address',
            field=models.CharField(help_text='Current Address', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='emergency_contact',
            field=models.CharField(help_text='Contact Number inCase of Emergency', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='entered_by',
            field=models.CharField(help_text='Username performing data Audit', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Modified Date'),
        ),
        migrations.AlterField(
            model_name='user',
            name='permanent_address',
            field=models.CharField(help_text='Permanent Address', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(help_text='Default Contact Number', max_length=15, null=True),
        ),
    ]
