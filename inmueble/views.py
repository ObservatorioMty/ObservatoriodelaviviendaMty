from django.shortcuts import render,redirect,reverse
import locale
from django.views import View
from django.views import generic
from django.views.generic.detail import DetailView
import os
import zipfile
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import DetailView
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
import locale
from inmueble.models import *

# Create your views here.
class InmueblesView(View):
    def get(self, request, *args, **kwargs):
        inmuebles = Inmueble.objects.all()
     
        context = {
            'inmuebles': inmuebles
        }

        return render(request, 'desarrolladoras.html', context)


class InmuebleView(DetailView):
    model = Inmueble
    template_name = 'desarrolladora.html'
    context_object_name = 'inmueble'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener la obra a través del slug en la URL
        inmueble = Inmueble.objects.filter(slug=self.kwargs.get('slug')).first()

       

        context['inmueble'] = inmueble

        return context