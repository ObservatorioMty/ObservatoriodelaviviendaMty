from django.db import models
from django.utils.text import slugify


class Team(models.Model):
    name = models.CharField(max_length=300,blank=True, null=True, verbose_name='Nombre')
    slug = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    team = models.TextField(blank=True, null=True, verbose_name=('Info'))
    image = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class IntroViviendaMty(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name=('Titulo'))
    intro = models.TextField(blank=True, null=True, verbose_name=('intro'))


class Metodologic(models.Model):
    metodologic = models.TextField(blank=True, null=True,verbose_name=('Metodo'))