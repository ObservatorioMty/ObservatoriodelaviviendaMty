from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'inmueble'

urlpatterns = [
    path('desarrolladoras/', InmueblesView.as_view(), name='desarrolladoras'),
    path('inmueble/<str:slug>/', InmuebleView.as_view(), name='inmueble'),
]