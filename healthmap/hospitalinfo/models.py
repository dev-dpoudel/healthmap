from django.db import models
from django.utils import timezone


# Hospital Information Model.
class HospitalInformation(models.Model):
    type = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=15)
    country = models.CharField(max_length=25)
    countrycd = models.CharField(max_length=4)
    emergency_available = models.BooleanField(default=True)
    has_lab = models.BooleanField(default=True)
    provides_ambulance = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=15)
    tollfree_no = models.CharField(max_length=30)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='hospital_idx'),
            models.Index(fields=['city', 'region', 'country'],
                         name='location_idx')
        ]


# Department Information Model.
class DepartmentInformation(models.Model):
    hospital = models.ForeignKey('HospitalInformation', on_delete=models.CASCADE)  # noqa E501
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=10)
    depart_head = models.ForeignKey('user.User', on_delete=models.RESTRICT)
    updated_date = models.DateTimeField(auto_now_add=True)


# Room Information Model.
class RoomInformation(models.Model):
    room_type = models.CharField(max_length=4)
    block = models.CharField(max_length=20)
    sub_block = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey('DepartmentInformation', on_delete=models.CASCADE)  # noqa E501

    class Meta:
        indexes = [
            models.Index(fields=['is_active', 'room_type'], name='roomty_idx')
        ]


# Bed Information Model
class BedInformation(models.Model):
    bed_type = models.CharField(max_length=4)
    room = models.ForeignKey('RoomInformation', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_occupied = models.BooleanField(default=False)
    visitor_allowed = models.BooleanField(default=False)
    planned_service_date = models.DateTimeField(null=True)
    last_service_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['is_active', 'is_occupied'],
                         name='available_idx'),
            models.Index(fields=['planned_service_date'], name='service_idx')
        ]


# Vacancy Related Information
class VacancyInfo(models.Model):
    type = models.CharField(max_length=10)
    position = models.CharField(max_length=15)
    required_experience = models.IntegerField(default=0)
    department = models.ForeignKey('DepartmentInformation', on_delete=models.CASCADE)  # noqa E501
    hospital = models.ForeignKey('HospitalInformation', on_delete=models.CASCADE)  # noqa E501
    description = models.CharField(max_length=1000)
    closure_date = models.DateTimeField(default=timezone.now)  # noqa E501
    total_open = models.IntegerField(default=1)

    class Meta:
        indexes = [
            models.Index(fields=['type', 'position', 'department'],
                         name='vacantpost_idx'),
            models.Index(fields=['closure_date'], name='closedt_idx')
        ]
