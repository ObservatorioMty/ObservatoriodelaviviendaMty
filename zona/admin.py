from django.contrib import admin

# Register your models here.
from .models import *


class ZoneAdmin(admin.ModelAdmin):
    list_display = ( 'street',)


admin.site.register(Zone, ZoneAdmin)