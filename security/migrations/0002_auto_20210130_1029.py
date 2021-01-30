# Generated by Django 3.1.4 on 2021-01-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='blocklist',
            name='activated_idx',
        ),
        migrations.RenameField(
            model_name='blocklist',
            old_name='entereddt',
            new_name='entered_date',
        ),
        migrations.RenameField(
            model_name='incidence',
            old_name='entereddt',
            new_name='entered_date',
        ),
        migrations.AlterField(
            model_name='blocklist',
            name='duration',
            field=models.PositiveIntegerField(default=1, help_text='Reason Blocklisted'),
        ),
        migrations.AddIndex(
            model_name='blocklist',
            index=models.Index(fields=['entered_date', 'type'], name='activated_idx'),
        ),
    ]
