"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        #Personas
        path('listarPersonas', views.listarPersonas, 
             name='listarPersonas'),
        path('crearPersonas', views.crearPersonas, 
             name='crearPersonas'),
        path('editarPersonas/<int:id>', views.editarPersonas, 
             name='editarPersonas'),
        path('eliminarPersonas/<int:id>', views.eliminarPersonas, 
             name='eliminarPersonas'),
        #Barrios
        path('listarBarrios', views.listarBarrios, 
             name='listarBarrios'),
        path('crearBarrios', views.crearBarrios, 
             name='crearBarrios'),
        path('editarBarrios/<int:id>', views.editarBarrios, 
             name='editarBarrios'),
        path('eliminarBarrios/<int:id>', views.eliminarBarrios, 
             name='eliminarBarrios'),
        #Local Comida
        path('listarLocalComida', views.listarLocalComida, 
             name='listarLocalComida'),
        path('crearLocalComida', views.crearLocalComida, 
             name='crearLocalComida'),
        path('editarLocalComida/<int:id>', views.editarLocalComida, 
             name='editarLocalComida'),
        path('eliminarLocalComida/<int:id>', views.eliminarLocalComida, 
             name='eliminarLocalComida'),
        #Local Repuesto
        path('listarLocalRepuesto', views.listarLocalRepuesto, 
             name='listarLocalRepuesto'),
        path('crearLocalRepuesto', views.crearLocalRepuesto, 
             name='crearLocalRepuesto'),
        path('editarLocalRepuesto/<int:id>', views.editarLocalRepuesto, 
             name='editarLocalRepuesto'),
        path('eliminarLocalRepuesto/<int:id>', views.eliminarLocalRepuesto, 
             name='eliminarLocalRepuesto'),  
        #Autenticación
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
 ]
