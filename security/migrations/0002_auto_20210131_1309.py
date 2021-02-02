# Generated by Django 3.1.4 on 2021-01-31 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidence',
            name='user',
            field=models.ForeignKey(help_text='Related User', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
        migrations.AddIndex(
            model_name='blocklist',
            index=models.Index(fields=['ip'], name='ipaddr_idx'),
        ),
        migrations.AddIndex(
            model_name='blocklist',
            index=models.Index(fields=['entered_date', 'type'], name='activated_idx'),
        ),
    ]