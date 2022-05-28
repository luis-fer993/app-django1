from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField

# Create your models here.
'''
Para cada tabla de la base de datos crearemos 
una clase con sus respectivos campos...
'''

class Clientes(models.Model):
    nombre = models.CharField(max_length=30, blank=False, default="nulo")
    direccion = models.CharField(max_length=40,blank=False, default="nulo")
    email = models.EmailField(max_length=30, unique=True, blank=False, default="nulo")
    telefono = models.CharField(max_length=12, blank=False, default="nulo")
    password = models.CharField(max_length=20, blank=False, default="nulo")

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()
    '''
     def __str__(self):
        return 'Articulo: %s, Precio: %s, Seccion: %s \n' %(self.nombre, self.precio, self.seccion)
        ESTA FUNCION SOLO LA UTILIZAMOS PARA CONVERTIR A STRING EL RESULTADO
        Y VERLO POR LA CONSOLA, PERO HAORA NO ES NECESARIO.. POR ESO SE EXCLUYE..
    '''
   
class Pedidos(models.Model):
    nuemero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()


