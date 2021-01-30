# Generated by Django 3.1.4 on 2021-01-29 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blocklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(help_text='IP address of the user', unique=True)),
                ('type', models.CharField(help_text='Type of Block List', max_length=4)),
                ('reason', models.CharField(help_text='Reason Blocklisted', max_length=200)),
                ('entereddt', models.DateTimeField(auto_now_add=True, help_text='Block List active Date')),
                ('duration', models.PositiveIntegerField(default=1, help_text='Duration of blocklist active in days')),
            ],
        ),
        migrations.CreateModel(
            name='Incidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Type of Incidence Reported', max_length=4)),
                ('ip', models.GenericIPAddressField(help_text='Requesting IP Address')),
                ('entereddt', models.DateTimeField(auto_now_add=True, help_text='Incidence Report Date Time')),
                ('user', models.ForeignKey(help_text='Related User', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.AddIndex(
            model_name='blocklist',
            index=models.Index(fields=['ip'], name='ipaddr_idx'),
        ),
        migrations.AddIndex(
            model_name='blocklist',
            index=models.Index(fields=['entereddt', 'type'], name='activated_idx'),
        ),
    ]
