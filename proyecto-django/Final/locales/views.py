from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

# importaer serializers
from locales.serializers import *

# importar las clases de models.py
from locales.models import *

# importar los formularios de forms.py
from locales.forms import *

# Create your views here.


def index(request):
    return render(request, "master.html")


# Personas
def listarPersonas(request):
    personas = Persona.objects.all()

    informacion_template = {"personas": personas}
    return render(request, "listarPersonas.html", informacion_template)


@login_required(login_url="/entrando/login/")
def crearPersonas(request):
    if request.method == "POST":
        formulario = PersonaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()  # se guarda en la base de datos
            return redirect(listarPersonas)
    else:
        formulario = PersonaForm()
    diccionario = {"formulario": formulario}

    return render(request, "crearPersonas.html", diccionario)


@login_required(login_url="/entrando/login/")
def editarPersonas(request, id):
    estudiante = Persona.objects.get(pk=id)
    if request.method == "POST":
        formulario = PersonaForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listarPersonas)
    else:
        formulario = PersonaForm(instance=estudiante)
    diccionario = {"formulario": formulario}

    return render(request, "editarPersonas.html", diccionario)


@login_required(login_url="/entrando/login/")
def eliminarPersonas(request, id):
    estudiante = Persona.objects.get(pk=id)
    estudiante.delete()
    return redirect(listarPersonas)


# Barrios
def listarBarrios(request):
    personas = Barrio.objects.all()

    informacion_template = {"personas": personas}
    return render(request, "listarBarrios.html", informacion_template)


@login_required(login_url="/entrando/login/")
def crearBarrios(request):
    if request.method == "POST":
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()  # se guarda en la base de datos
            return redirect(listarBarrios)
    else:
        formulario = BarrioForm()
    diccionario = {"formulario": formulario}

    return render(request, "crearBarrios.html", diccionario)


@login_required(login_url="/entrando/login/")
def editarBarrios(request, id):
    estudiante = Barrio.objects.get(pk=id)
    if request.method == "POST":
        formulario = BarrioForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listarBarrios)
    else:
        formulario = BarrioForm(instance=estudiante)
    diccionario = {"formulario": formulario}

    return render(request, "editarBarrios.html", diccionario)


@login_required(login_url="/entrando/login/")
def eliminarBarrios(request, id):
    estudiante = Barrio.objects.get(pk=id)
    estudiante.delete()
    return redirect(listarBarrios)


# Local de Comida
def listarLocalComida(request):
    personas = LocalComida.objects.all()

    informacion_template = {"personas": personas}
    return render(request, "listarLocalComida.html", informacion_template)


@login_required(login_url="/entrando/login/")
def crearLocalComida(request):
    if request.method == "POST":
        formulario = LocalComidaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()  # se guarda en la base de datos
            return redirect(listarLocalComida)
    else:
        formulario = LocalComidaForm()
    diccionario = {"formulario": formulario}

    return render(request, "crearLocalComida.html", diccionario)


@login_required(login_url="/entrando/login/")
def editarLocalComida(request, id):
    estudiante = LocalComida.objects.get(pk=id)
    if request.method == "POST":
        formulario = LocalComidaForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listarLocalComida)
    else:
        formulario = LocalComidaForm(instance=estudiante)
    diccionario = {"formulario": formulario}

    return render(request, "editarLocalComida.html", diccionario)


@login_required(login_url="/entrando/login/")
def eliminarLocalComida(request, id):
    estudiante = LocalComida.objects.get(pk=id)
    estudiante.delete()
    return redirect(listarLocalComida)


# Local de Repuesto
def listarLocalRepuesto(request):
    personas = LocalRepuesto.objects.all()

    informacion_template = {"personas": personas}
    return render(request, "listarLocalRepuesto.html", informacion_template)


@login_required(login_url="/entrando/login/")
def crearLocalRepuesto(request):
    if request.method == "POST":
        formulario = LocalRepuestoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()  # se guarda en la base de datos
            return redirect(listarLocalRepuesto)
    else:
        formulario = LocalRepuestoForm()
    diccionario = {"formulario": formulario}

    return render(request, "crearLocalRepuesto.html", diccionario)


@login_required(login_url="/entrando/login/")
def editarLocalRepuesto(request, id):
    estudiante = LocalRepuesto.objects.get(pk=id)
    if request.method == "POST":
        formulario = LocalRepuestoForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listarLocalRepuesto)
    else:
        formulario = LocalRepuestoForm(instance=estudiante)
    diccionario = {"formulario": formulario}

    return render(request, "editarLocalRepuesto.html", diccionario)


@login_required(login_url="/entrando/login/")
def eliminarLocalRepuesto(request, id):
    estudiante = LocalRepuesto.objects.get(pk=id)
    estudiante.delete()
    return redirect(listarLocalRepuesto)


# LogIn
def ingreso(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(index)
    else:
        form = AuthenticationForm()

    informacion_template = {"form": form}
    return render(request, "registration/login.html", informacion_template)


def logout_view(request):
    logout(request)
    messages.info(request, "Has salido del sistema")
    return redirect(index)


# ViewSets
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]


class BarrioViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalComidaViewSet(viewsets.ModelViewSet):
    queryset = LocalComida.objects.all()
    serializer_class = LocalComidaSerializer
    permission_classes = [permissions.IsAuthenticated]

class LocalRepuestoViewSet(viewsets.ModelViewSet):
    queryset = LocalRepuesto.objects.all()
    serializer_class = LocalRepuestoSerializer
    permission_classes = [permissions.IsAuthenticated]