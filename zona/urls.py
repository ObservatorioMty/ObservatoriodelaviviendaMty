from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('mapa', MapaView.as_view(), name='mapa'),
]