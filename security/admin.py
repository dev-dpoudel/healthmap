from django.contrib import admin
from .models import Blocklist, Incidence
# Register your models here.
admin.site.register(Blocklist)
admin.site.register(Incidence)
