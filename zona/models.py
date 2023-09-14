from django.db import models
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext as _
from django.db.models import Count, Q, Avg,JSONField
from datetime import datetime, timedelta
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.


class Zone(models.Model):
    street =  models.CharField(max_length=400,default='test', verbose_name=('Calle'))
    colony =  models.CharField(max_length=600, default='test', verbose_name=('Colonia'))
    municipality = models.CharField(max_length=300, verbose_name=('Municipio'))
    since =  models.CharField(max_length=400,default='test', verbose_name=('Desde'))
    latitude_since = models.FloatField(null=True, verbose_name=('Desde latitude'))
    longitude_since = models.FloatField(null=True, verbose_name=('Desde longitud'))
    until =  models.CharField(max_length=400,default='test', verbose_name=('Hasta'))
    latitude_until = models.FloatField(null=True, verbose_name=('Hasta latitude'))
    longitude_until = models.FloatField(null=True, verbose_name=('Hasta longitud'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
