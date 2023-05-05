# django_apis
Repositorio para la creacion de API's de prueba
Toda la infor en:
https://www.django-rest-framework.org/
https://www.django-rest-framework.org/tutorial/quickstart/


Tutorial donde se sacó  este manual --->
https://www.youtube.com/watch?v=GE0Q8YNKNgs

*Instalar entorno Virtual y activarlo
python3 -m venv my_env
ubuntu --> source env/bin/activate

*Instalar DJango 
pip install django

*Instalar Django Rest FrameWork
pip install djangorestframework

*Iniciar proyecto
django-admin startproject NombreDelProyecto .  // Con el punto le digo que lo cree en el directorio actual. 

*Probar que funcione.
python manage.py runserver
Ir a la ip que te da en el mensaje ---> http://127.0.0.1:8000/

*Crear API (Ejemplo)
Vamos a crear una API que nos permita poder obtener, crear, eliminar,  proyecto y actualizarlos (CRUD)
python manage.py startapp NOMBRE_API_APP

En settings.py dentro de la carpeta del proyecto. 
Agregar en INSTALLED_APPS la nueva api y el FrameWork de Rest--->

INSTALLED_APPS = [
	.
	.
	.
    'proyectos',
    'rest_framework'
]

*Crear Modelo de Datos **MODELS**
Se crea el modelo para que se pueda crear la tabla.
Se crea la clase Projecto para crear la tabla en la Base de datos que esté conectado a DJango. (Esta clase esta en models.py)
-->
from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=200)
    fue_creado = models.DateTimeField(auto_now_add=True)
---

Hasta el momento el proyecto no tiene creada ninguna base de datos. 
tiene el db.sqlite3 pero no esta inicializada no se hizo ninguna migración. 
Para esto -->

python manage.py makemigrations
Migrations for 'proyectos':
  proyectos\migrations\0001_initial.py
    - Create model Proyecto
Aqui crea los comandos por mi para crear la tabla en la base de datos. 

Para crear la tabla y la BD -->
python manage.py migrate


*Para poder usar el modelo tenemos que crear los SERIALIZER y los VIEWSETS.
*API
Aqui creamos la Rest API
Arthivos-->

    Serializer:
	El serializer es quien va a hacer posible transformar nuestras tablas en formato JSon o XML. En este caso Json
    proyectos/serializers.py -->
        from rest_framework import serializers
        from .models import Proyecto

        class ProyectoSerializer(serializers.ModelSerializer):
            class Meta:
                model = Proyecto
                fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'fue_creado')
                read_only_fields = ('fue_creado') #Este campo solo puede leerse no cambiarse.
    
    Viewsets:
    proyectos/api.py -->
        from .models import Proyecto
        from rest_framework import viewsets, permissions
        from .serializers import ProyectoSerializer  #--->> s no se pone el  "." en el principio da error 

        #Aqui vamos a decir que consultas vamos a poder hacer
        class ViewSetProyecto(viewsets.ModelViewSet):
            queryset = Proyecto.objects.all() #Utilizando el modelo Proyecto le decimos que consulte todos los objetos 
            permission_classes = [permissions.AllowAny]
            serializer_class = ProyectoSerializer   #Aqui llamamos el Serializer para decirle a partir de que Serializer va a estar utilizando estos datos. 
                                                    #Le decimos como los va a convertir

*TEnemos que crear las rutas URL
Archivos -->
    URLS:
    proyectos/urls.py
        from rest_framework import routers
        from .api import ViewSetProyecto

        router = routers.DefaultRouter
        router.register('api/proyects', ViewSetProyecto, 'proyectos')#Aqui genera como 4 urls, parar get, post, delete y put.
        #router.register('ruta', viewset(va a estar basando en el conjunto de datos de viewset), 'nombre de la ruta')


        #Hay que exportar el urlPatterns
        urlpatterns = router.urls

    Ya estan creadas las rutas, pero la plicacione principal no las conoce, 
    entonces hay que modificar el archivo urls.py -->


*Tenemos que añadir las rutas a la aplicaciones principal. 

        from django.urls import path, include
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('proyectos.urls')),
            path('', include('usuarios.urls'))
        ]