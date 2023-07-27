from django.contrib.auth.models import User, Group
from locales.models import *

from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__'

class LocalComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalComida
        fields = '__all__'

class LocalRepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalRepuesto
        fields = '__all__'