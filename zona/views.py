from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from django.urls import reverse
from django.views.generic import ListView
from django.template.loader import render_to_string
from django.http import JsonResponse
from datetime import datetime, timedelta
import io
import base64
import datetime
from django.views import View
from inmueble.models import *
from investigacion.models import *
from equipo.models import *
from zona.models import *
# Create your views here.


class MapaView(View):
    def get(self, request, *args, **kwargs):
        inmueble = Inmueble.objects.all()
        investigation = Investigation.objects.all()
        metodologic = Metodologic.objects.all()
        zones = Zone.objects.all()

        context = {
            'investigation': investigation,
            'metodologic': metodologic,
            'inmueble': inmueble,
            'zones': zones,
        }

        return render(request, "map.html", context)
   