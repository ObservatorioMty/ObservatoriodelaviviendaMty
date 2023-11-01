from django.db import models
from datetime import datetime
from django.utils.text import slugify
# Create your models here.

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    seleccionada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class   Investigation(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name=('Titulo'))
    slug = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    image = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image1 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    introduccion = models.TextField(max_length=1500, blank=True, null=True, verbose_name='introducción')
    seccion1 = models.TextField(max_length=10500, blank=True, null=True,verbose_name='seccion1')
    by = models.CharField(max_length=500, blank=True, null=True, verbose_name=('Escrito por')  )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    etiquetas = models.ManyToManyField(Etiqueta)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)