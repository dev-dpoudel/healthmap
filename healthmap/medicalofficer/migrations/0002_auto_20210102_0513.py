# Generated by Django 3.1.4 on 2021-01-02 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalinfo', '0001_initial'),
        ('medicalofficer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalofficer',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitalinfo.departmentinformation'),
        ),
    ]