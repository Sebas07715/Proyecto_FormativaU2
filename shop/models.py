from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(unique=True, max_length=10)
    email = models.EmailField()
    direccion = models.CharField(max_length=80)
    saldo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"
    
class Producto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    articulo = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return f"{self.articulo} - ${self.precio} ({self.fecha})"