# Generated by Django 3.1.4 on 2021-01-31 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blocklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(help_text='IP address of the user', unique=True)),
                ('type', models.CharField(help_text='Type of Block List', max_length=4)),
                ('reason', models.CharField(help_text='Reason Blocklisted', max_length=200)),
                ('entered_date', models.DateTimeField(auto_now_add=True, help_text='Block List active Date')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Block List active Date')),
                ('duration', models.PositiveIntegerField(default=1, help_text='Duration Blocklisted')),
            ],
        ),
        migrations.CreateModel(
            name='Incidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Type of Incidence Reported', max_length=4)),
                ('ip', models.GenericIPAddressField(help_text='Requesting IP Address')),
                ('entered_date', models.DateTimeField(auto_now_add=True, help_text='Incidence Report Date Time')),
            ],
        ),
    ]
