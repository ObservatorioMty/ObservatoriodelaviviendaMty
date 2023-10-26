from django.db import models
from django.utils.text import slugify
from datetime import datetime
# Create your models here



class Inmueble(models.Model):
    no_licencia =  models.CharField(max_length=500,blank=True, null=True, verbose_name=('Numero de la licencia'))
    development = models.CharField(max_length=500, blank=True, null=True,verbose_name=('Nombre del inmueble'))
    slug = models.CharField(max_length=100, blank=True, null=True, unique=True, db_index=True)
    address = models.CharField(max_length=500, blank=True, null=True, verbose_name=('Dirección del inmueble'))
    descripcion = models.CharField(max_length=800, blank=True, null=True, verbose_name=('Descripción del inmueble'))
    characteristics = models.CharField(max_length=800, blank=True, null=True, verbose_name=('Características del inmueble'))
    characteristics = models.CharField(max_length=800, blank=True, null=True, verbose_name=('Características del inmueble'))
    owner = models.CharField(max_length=800, blank=True, null=True, verbose_name=('Propietario'))
    agreement_date = models.DateTimeField(blank=True, null=True, verbose_name=('Fecha de acuerdo'))
    surface = models.FloatField(blank=True, null=True, verbose_name=('Superficie'))
    levels = models.IntegerField(blank=True, null=True, verbose_name=('Niveles'))
    departments = models.IntegerField(blank=True, null=True, verbose_name=('Departamentos'))
    local = models.IntegerField(blank=True, null=True, verbose_name=('Locales'))
    offices = models.IntegerField(blank=True, null=True, verbose_name=('Oficinas'))
    parking = models.IntegerField(blank=True, null=True, verbose_name=('Estacionamiento'))
    required_parking = models.IntegerField(blank=True, null=True, verbose_name=('Estacionamientos requeridos'))
    price = models.FloatField(blank=True, null=True, verbose_name=('precio'))
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    image = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image1 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image2 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image3 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image4 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image5 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image6 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image7 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image8 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image9 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image10 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image11 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image12 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image13 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image14 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image15 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image16 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image17 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image18 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image19 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image20 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    credits_image = models.CharField(max_length=300,null=True, blank=True, verbose_name=('Creditos de las imagenes'))
    link_image = models.URLField(null=True, blank=True,verbose_name="Link de los creditos")
    pdf = models.FileField(blank=True, null=True, upload_to='pdf', verbose_name='pdf')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.development

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.development)
        return super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.development)
        if self.pk is not None and self.completate != self.__class__.objects.get(pk=self.pk).completate and self.completate:
            # si completate ha cambiado de False a True, actualiza la fecha de término
            self.term2 = datetime.now().date()
        elif self.pk is not None and self.completate != self.__class__.objects.get(pk=self.pk).completate and not self.completate:
            # si completate ha cambiado de True a False, reinicia la fecha de término
            self.term2 = None
        super().save(*args, **kwargs) 