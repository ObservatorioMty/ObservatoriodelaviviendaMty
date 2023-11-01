from django.urls import path
from .views import *

urlpatterns = [
    # Otras rutas
    path('todos-articulos/', VerTodosLosArticulosView.as_view(), name='ver_todos_los_articulos'),
    path('etiqueta/<int:etiqueta_id>/', VerArticulosPorEtiquetaView.as_view(), name='ver_articulos_por_etiqueta'),
    path('investigation/<str:slug>/', InvestigationDetailView.as_view(), name='investigacion_detalle'),
]