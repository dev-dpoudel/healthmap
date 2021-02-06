from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Hospital Information Model.
class HospitalInformation(models.Model):

    class HospitalType(models.TextChoices):
        GENERAL = 'GEN', _('General')
        PHYSIO = 'PSY', _('Physiotherapy')
        OUTHOSPITAL = 'IHGE', _('Inter Hospital General')

    type = models.CharField(
        max_length=4,
        help_text="Type of hospital facility i.e. special /general")
    name = models.CharField(
        max_length=50,
        help_text="Name of Institution")
    address = models.CharField(
        max_length=50,
        help_text="Location")
    city = models.CharField(
        max_length=20,
        help_text="City")
    region = models.CharField(
        max_length=15,
        help_text="Region i.e. Province or State")
    country = models.CharField(
        max_length=25,
        help_text="Country")
    emergency_available = models.BooleanField(
        default=True,
        help_text="Emergency Service")
    has_lab = models.BooleanField(
        default=True,
        help_text="Lab/ Investigation")
    provides_ambulance = models.BooleanField(
        default=True,
        help_text="Ambulance service")
    is_active = models.BooleanField(
        default=True,
        help_text="Closed/ Operating")
    phone = models.CharField(
        max_length=15,
        help_text="Contact Number")
    tollfree_no = models.CharField(
        max_length=30,
        help_text="Toll Free Number")
    website = models.CharField(
        max_length=100,
        help_text="Website Link",
        null=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='hospital_idx'),
            models.Index(fields=['city', 'region', 'country'],
                         name='location_idx')
        ]


# Department Information Model.
class DepartmentInformation(models.Model):

    class DepartmentType(models.TextChoices):
        EMERGENCY = 'EMR', _('Emergency')
        ANASTHECIA = 'ATC', _('Anasthetics')
        ONCOLOGY = 'ONC', _('Oncology')
        CARDIOLOGY = 'CRD', _('Cardiology')
        STERILE = 'SPD', _('Sterile Processing Department')
        DIMAGING = 'DIMG', _('Diagnostic Imaging')
        GASTRO = 'GAST', _('Gastroenterology')
        GYNO = 'GYNO', _('Gynocology')
        HEMATO = 'HEMT', _('Hematology')
        INFECTION = 'ICO', _('Infection Control')
        OPTHALMO = 'OPTH', _('Opthalmology')
        UROLOGY = 'Uro', _('Urology')
        ENT = 'ENT', _('Ear Nose Throat')
        NEURO = 'NEU', _('Neuro')
        PEDIA = 'PED', _('Pediatrics')

    hospital = models.ForeignKey(
        'HospitalInformation',
        on_delete=models.CASCADE,
        help_text="Related Hospital")
    is_active = models.BooleanField(
        default=True,
        help_text="Closed/Serving")
    name = models.CharField(
        max_length=10,
        help_text="Department Name")
    depart_head = models.ForeignKey(
        'user.User',
        on_delete=models.RESTRICT,
        help_text="Department Name")
    updated_date = models.DateTimeField(auto_now_add=True)


# Room Information Model.
class RoomInformation(models.Model):

    class RoomType(models.TextChoices):
        GENERAL = 'GEN', _('General')
        GCABIN = 'GCAB', _('General Private Cabin')
        INTENSIVE = 'ICU', _('Intensive Care Unit')
        CRITICAL = 'CCU', _('Critical Care Unit')

    room_type = models.CharField(
        max_length=4,
        help_text="Type i.e. ICU / CCU / General")
    block = models.CharField(
        max_length=20,
        help_text="Building Block Code")
    sub_block = models.CharField(
        max_length=20,
        null=True,
        help_text="Sub Block Code")
    is_active = models.BooleanField(
        default=True,
        help_text="Active/Inactive")
    department = models.ForeignKey(
        'DepartmentInformation',
        on_delete=models.CASCADE,
        help_text="Department Related to")

    class Meta:
        indexes = [
            models.Index(fields=['is_active', 'room_type'], name='roomty_idx')
        ]


# Bed Information Model
class BedInformation(models.Model):

    class BedType(models.TextChoices):
        GENERAL = 'GEN', _('General')
        VENTILATED = 'VENT', _('Ventilated Bed')
        CONSTMONIT = 'CMON', _('Constant Monitoring Bed')
        RECLINED = 'RECL', _('Recline Bed')

    bed_type = models.CharField(
        max_length=4,
        help_text="Bed Type")
    room = models.ForeignKey(
        'RoomInformation',
        on_delete=models.CASCADE,
        help_text="Room Related To")
    is_active = models.BooleanField(
        default=True,
        help_text="Active/Inactive")
    is_occupied = models.BooleanField(
        default=False,
        help_text="Occupied/Vacant")
    visitor_allowed = models.BooleanField(
        default=False,
        help_text="Visitor Allowed")
    planned_service_date = models.DateTimeField(
        null=True,
        help_text="Regular Planned Service Date")
    last_service_date = models.DateTimeField(
        auto_now_add=True,
        help_text="Last service Date")

    class Meta:
        indexes = [
            models.Index(fields=['is_active', 'is_occupied'],
                         name='available_idx'),
            models.Index(fields=['planned_service_date'], name='service_idx')
        ]


# Vacancy Related Information
class VacancyInfo(models.Model):

    class VacancyType(models.TextChoices):
        CONTRACT = 'CONT', _('Contract Full Time')
        PERMANENT = 'PERM', _('Permanent Full Time')
        PARTTIME = 'PART', _('Part Time')

    type = models.CharField(
        max_length=10,
        help_text="Type of Vacancy")
    position = models.CharField(
        max_length=15,
        help_text="Position of vacancy")
    required_experience = models.IntegerField(
        default=0,
        help_text="Experience Required Years")
    department = models.ForeignKey(
        'DepartmentInformation',
        on_delete=models.CASCADE,
        help_text="Department Related To")
    hospital = models.ForeignKey(
        'HospitalInformation',
        on_delete=models.CASCADE,
        help_text="Hospital Related To")
    description = models.CharField(
        max_length=1000,
        help_text="Vacancy Description")
    closure_date = models.DateTimeField(
        default=timezone.now,
        help_text="Apply up till")
    total_open = models.IntegerField(
        default=1,
        help_text="Total Vacant Position")
    link = models.CharField(
        max_length=100,
        help_text="Application Link",
        null=True)

    class Meta:
        indexes = [
            models.Index(fields=['type', 'position', 'department'],
                         name='vacantpost_idx'),
            models.Index(fields=['closure_date'], name='closedt_idx')
        ]
