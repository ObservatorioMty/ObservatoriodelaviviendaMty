from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'team'

urlpatterns = [
    path('equipo/', TeamView.as_view(), name='team'),
    path('equipo/<str:slug>/', MiembroView.as_view(), name='miembro'),
]