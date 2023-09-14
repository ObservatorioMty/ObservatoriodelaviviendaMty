from django.db import models
from datetime import datetime
# Create your models here.



class   Investigation(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name=('Titulo'))
    image = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image1 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image2 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image3 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image4 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    introduccion = models.TextField(max_length=1500, blank=True, null=True, verbose_name='introducción')
    seccion1 = models.TextField(max_length=3500, blank=True, null=True,verbose_name='seccion1')
    seccion2 = models.TextField(max_length=3500,blank=True, null=True,  verbose_name='seccion2')
    seccion3 = models.TextField(max_length=3500,blank=True, null=True, verbose_name='seccion3')
    seccion4 = models.TextField(max_length=3500, blank=True, null=True, verbose_name='seccion4')
    seccion5 = models.TextField(max_length=3500, blank=True, null=True, verbose_name='seccion5')
    seccion6 = models.TextField(max_length=3500, blank=True, null=True, verbose_name='seccion6')
    seccion7 = models.TextField(max_length=3500, blank=True, null=True, verbose_name='seccion7')
    seccion8 = models.TextField(max_length=3500, blank=True, null=True, verbose_name='seccion8')
    by = models.CharField(max_length=500, blank=True, null=True, verbose_name=('Escrito por')  )
    appointment1 = models.TextField(max_length=600, blank=True, null=True, verbose_name=('Cita1'))
    name_appointment1 = models.TextField(max_length=600, blank=True, null=True, verbose_name=('Nombre de la cita1'))
    appointment2 = models.TextField(max_length=600, blank=True, null=True, verbose_name=('Cita2'))
    name_appointment2 = models.TextField(max_length=600, blank=True, null=True, verbose_name=('Nombre de la cita2'))
    appointment3 = models.TextField(max_length=600, blank=True, null=True, verbose_name=('Cita3'))
    name_appointment3 = models.TextField(max_length=600, blank=True, null=True, verbose_name=('Nombre de la cita3'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)