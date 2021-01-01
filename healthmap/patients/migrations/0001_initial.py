# Generated by Django 3.1.4 on 2021-01-01 11:22

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
            name='StaffPersons',
            fields=[
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('entered_by', models.CharField(max_length=20)),
                ('staff_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('is_hospital_staff', models.BooleanField(default=False)),
                ('staff_post', models.CharField(max_length=25)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffFamily',
            fields=[
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('entered_by', models.CharField(max_length=20)),
                ('relation', models.CharField(max_length=20)),
                ('relation_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('is_billable', models.BooleanField(default=False)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.staffpersons')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='staffpersons',
            index=models.Index(fields=['is_hospital_staff'], name='staff_idx'),
        ),
        migrations.AddIndex(
            model_name='stafffamily',
            index=models.Index(fields=['is_billable'], name='billable_idx'),
        ),
    ]
