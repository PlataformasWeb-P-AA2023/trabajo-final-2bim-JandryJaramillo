from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from locales.models import *

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'cedula', 'correo']

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'siglas']

class LocalComidaForm(forms.ModelForm):
    class Meta:
        model = LocalComida
        fields = ['propietario', 'direccion', 'barrio', 'tipoComida', 'ventas']

class LocalRepuestoForm(forms.ModelForm):
    class Meta:
        model = LocalRepuesto
        fields = ['propietario', 'direccion', 'barrio', 'valor']