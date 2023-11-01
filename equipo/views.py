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
from equipo.models import *

# Create your views here.
class TeamView(View):
    def get(self, request, *args, **kwargs):
        team = Team.objects.all()
     
        context = {
            'team': team
        }

        return render(request, 'quienes-somos.html', context)


class MiembroView(DetailView):
    model = Team
    template_name = 'miembro.html'
    context_object_name = 'miembro'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener la obra a través del slug en la URL
        miembro = Team.objects.filter(slug=self.kwargs.get('slug')).first()

       

        context['miembro'] = miembro

        return context