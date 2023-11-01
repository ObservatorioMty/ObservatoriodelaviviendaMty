from django.views import View
from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView


class VerTodosLosArticulosView(View):
    def get(self, request):
        articulos = Investigation.objects.all()
        return render(request, 'investigaciones.html', {'articulos': articulos})
class VerArticulosPorEtiquetaView(View):
    def get(self, request, etiqueta_id):
        etiqueta = Etiqueta.objects.get(pk=etiqueta_id)
        articulos = Investigation.objects.filter(etiquetas=etiqueta)
        return render(request, 'investigaciones_etiqueta.html', {'etiqueta': etiqueta, 'articulos': articulos})
    
class InvestigationDetailView(DetailView):
    model = Investigation
    template_name = 'articulo.html'
    context_object_name = 'investigation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener el artículo basado en el slug
        articulo = Investigation.objects.filter(slug=self.kwargs.get('slug')).first()

        # Agregar el artículo al contexto
        context['articulo'] = articulo

        return context