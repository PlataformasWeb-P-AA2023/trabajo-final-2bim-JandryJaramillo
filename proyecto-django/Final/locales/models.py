from django.db import models
from decimal import Decimal

class Persona(models.Model):

    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    cedula = models.CharField(max_length=10)
    correo = models.EmailField()

    def __str__(self):
        return "Nombre: %s %s - Cédula: %s - Correo: %s" % (self.nombres,
                                self.apellidos,
                                self.cedula,
                                self.correo)

class Barrio(models.Model):

    nombre = models.CharField(max_length=80)
    siglas = models.CharField(max_length=30)

    def __str__(self):
        return "Nombre: %s - Siglas: %s" % (self.nombre,
                          self.siglas)

class LocalComida(models.Model):

    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="personaComida")
    
    direccion = models.CharField(max_length=80)

    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="barrioComida")
    
    tipoComida = models.CharField(max_length=80)
    ventas = models.DecimalField(max_digits=12, decimal_places=2)

    def pagoPermiso(self):
        return self.ventas * Decimal('0.8')

    def __str__(self):
        return "%s %s %s %s %s" % (self.propietario,
                                self.direccion,
                                self.barrio,
                                self.tipoComida,
                                self.ventas)

class LocalRepuesto(models.Model):

    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="personaRepuesto")
    
    direccion = models.CharField(max_length=80)

    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="barrioRepuesto")

    valor = models.DecimalField(max_digits=12, decimal_places=2)
    
    def pagoPermiso(self):
        return self.valor * Decimal('0.001')
    
    def __str__(self):
        return "%s %s %s %s %s" % (self.propietario,
                                self.direccion,
                                self.barrio,
                                self.valor)