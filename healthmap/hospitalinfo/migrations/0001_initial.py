# Generated by Django 3.1.4 on 2021-01-31 13:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BedInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_type', models.CharField(help_text='Bed Type', max_length=4)),
                ('is_active', models.BooleanField(default=True, help_text='Active/Inactive')),
                ('is_occupied', models.BooleanField(default=False, help_text='Occupied/Vacant')),
                ('visitor_allowed', models.BooleanField(default=False, help_text='Visitor Allowed')),
                ('planned_service_date', models.DateTimeField(help_text='Regular Planned Service Date', null=True)),
                ('last_service_date', models.DateTimeField(auto_now_add=True, help_text='Last service Date')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Closed/Serving')),
                ('name', models.CharField(help_text='Department Name', max_length=10)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Type of hospital facility i.e. special /general', max_length=4)),
                ('name', models.CharField(help_text='Name of Institution', max_length=50)),
                ('address', models.CharField(help_text='Location', max_length=50)),
                ('city', models.CharField(help_text='City', max_length=20)),
                ('region', models.CharField(help_text='Region i.e. Province or State', max_length=15)),
                ('country', models.CharField(help_text='Country', max_length=25)),
                ('emergency_available', models.BooleanField(default=True, help_text='Emergency Service')),
                ('has_lab', models.BooleanField(default=True, help_text='Lab/ Investigation')),
                ('provides_ambulance', models.BooleanField(default=True, help_text='Ambulance service')),
                ('is_active', models.BooleanField(default=True, help_text='Closed/ Operating')),
                ('phone', models.CharField(help_text='Contact Number', max_length=15)),
                ('tollfree_no', models.CharField(help_text='Toll Free Number', max_length=30)),
                ('website', models.CharField(help_text='Website Link', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Type of Vacancy', max_length=10)),
                ('position', models.CharField(help_text='Position of vacancy', max_length=15)),
                ('required_experience', models.IntegerField(default=0, help_text='Experience Required Years')),
                ('description', models.CharField(help_text='Vacancy Description', max_length=1000)),
                ('closure_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Apply up till')),
                ('total_open', models.IntegerField(default=1, help_text='Total Vacant Position')),
                ('link', models.CharField(help_text='Application Link', max_length=100, null=True)),
                ('department', models.ForeignKey(help_text='Department Related To', on_delete=django.db.models.deletion.CASCADE, to='hospitalinfo.departmentinformation')),
                ('hospital', models.ForeignKey(help_text='Hospital Related To', on_delete=django.db.models.deletion.CASCADE, to='hospitalinfo.hospitalinformation')),
            ],
        ),
        migrations.CreateModel(
            name='RoomInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(help_text='Type i.e. ICU / CCU / General', max_length=4)),
                ('block', models.CharField(help_text='Building Block Code', max_length=20)),
                ('sub_block', models.CharField(help_text='Sub Block Code', max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Active/Inactive')),
                ('department', models.ForeignKey(help_text='Department Related to', on_delete=django.db.models.deletion.CASCADE, to='hospitalinfo.departmentinformation')),
            ],
        ),
        migrations.AddIndex(
            model_name='hospitalinformation',
            index=models.Index(fields=['name'], name='hospital_idx'),
        ),
        migrations.AddIndex(
            model_name='hospitalinformation',
            index=models.Index(fields=['city', 'region', 'country'], name='location_idx'),
        ),
    ]
