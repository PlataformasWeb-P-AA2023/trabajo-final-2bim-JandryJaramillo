from django.contrib import admin
from .models import *

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'correo')
    search_fields = ('nombres', 'apellidos')
admin.site.register(Persona, PersonaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas')
    search_fields = ('nombre', 'siglas')
admin.site.register(Barrio, BarrioAdmin)

class LocalComidaAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion', 'barrio', 'tipoComida', 'ventas')
    search_fields = ('direccion', 'tipoComida')    
admin.site.register(LocalComida, LocalComidaAdmin)

class LocalRepuestoAdmin(admin.ModelAdmin):
    list_display = ('propietario', 'direccion', 'barrio', 'valor')
    search_fields = ('direccion', 'barrio')
admin.site.register(LocalRepuesto, LocalRepuestoAdmin)