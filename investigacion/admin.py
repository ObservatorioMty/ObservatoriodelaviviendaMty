from django.contrib import admin
from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.

from django import forms

class InvestigationAdminForm(forms.ModelForm):
    class Meta:
        model = Investigation
        fields = ['title', 'image', 'image1', 'introduccion', 'seccion1', 'by', 'etiquetas']

    etiquetas = forms.ModelMultipleChoiceField(
        queryset=Etiqueta.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class InvestigationAdmin(admin.ModelAdmin):
    form = InvestigationAdminForm

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Investigation, InvestigationAdmin)
admin.site.register(Etiqueta)