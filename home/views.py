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


class HomeView(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, "home.html", locals())
   