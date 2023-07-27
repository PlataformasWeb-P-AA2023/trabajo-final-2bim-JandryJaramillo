# Guia para levantar el proyecto Django en Ngix

* Se necesita un sistema operativo GNU/Linux (UBUNTU)
* Lenguaje de programación Python
* Librerías de pyhton: django, corsheaders, rest_framework, gunicorn
* Servidor Web - nginx
	
## Proceso 

1. Instalar la librería gunicorn (pip install gunicorn) en el entorno de trabajo.
2. Modificar la variable **ALLOWED_HOSTS**  con direcciones en el archivo **settings.py** del proyecto de django;
```
ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"] 	 
```
2.1 Agregar en el **settings.py** la variable:
```
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
3. En el archivo **urls.py** del proyecto de django agregar lo siguiente:
```
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# agregar el siguiente valor a la variable urlpatterns:

staticfiles_urlpatterns()
```
4. Recopilar el contenido estático en al carpeta static:
```
python manage.py collectstatic
```
5. Levantar o iniciar el proyecto con **gunicorn**, desde la carpeta raíz:
```
gunicorn --bind 0.0.0.0:8000 Final.wsgi
```

### Parte 2

Enlazar el servidor nginx mediante gunicorn con el proyecto de django.

1. Abrir un terminal y usar **cd ..** hasta no poder más y luego.

2. Ubicarse en el directorio **/etc/systemd/system/** agregar el siguiente archivo. Se debe usar **sudo**.

3. **sudo nano proyecto01.service** .

4. En el archivo agregar:
```
[Unit]
# metadatos necesarios
Description=gunicorn daemon
After=network.target

[Service]
# usuario del sistema operativo que ejecutará el proceso
User=jandry
# el grupo del sistema operativo que permite la comunicación a desde el servidor web-nginx con gunicorn. No se debe cambiar el valor
Group=www-data

# a través de la variable WorkingDirectory se indica la dirección absoluta del proyecto de Django
WorkingDirectory=/home/jandry/Escritorio/Final/trabajo-final-2bim-JandryJaramillo/proyecto-django/Final

# En Environment se indica el path de python
# Ejemplo 1: /usr/bin/python3.9
# Ejemplo 2: (Opcional, con el uso de entornos virtuales) /home/usuario/entornos/entorno01/bin
Environment="PATH=/home/jandry/entornos/entorno_django/bin"

# Detallar el comando para iniciar el servicio
ExecStart=/home/jandry/entornos/entorno_django/bin/gunicorn --workers 3 --bind unix:application.sock -m 007 Final.wsgi:application

# Donde: aplicacion.sock es el nombre del archivo que se debe crear en el directorio del proyecto; proyectoDjango el nombre del proyecto que se intenta vincular con nginx.
# La expresión /bin/gunicorn no se debe modificar.

[Install]
# esta sección será usada para indicar que el servicio puede empezar cuando se inicie el sistema operativo. Se sugiere no cambiar el valor dado.
WantedBy=multi-user.target

```
5. Iniciar y habilitar el proceso a través de los siguiente comandos:
```
sudo systemctl start proyecto01
sudo systemctl enable proyecto01
```

6. Verificar que todo esté en orden con el servicio, usar el comando:
```
sudo systemctl status proyecto01
```
