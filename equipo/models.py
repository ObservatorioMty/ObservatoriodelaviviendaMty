from django.db import models



class Team(models.Model):
    team = models.TextField(blank=True, null=True, verbose_name=('quienes somos'))
    image = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image1 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image2 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))


class IntroViviendaMty(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name=('Titulo'))
    intro = models.TextField(blank=True, null=True, verbose_name=('intro'))


class Metodologic(models.Model):
    metodologic = models.TextField(blank=True, null=True,verbose_name=('Metodo'))