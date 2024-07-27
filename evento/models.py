from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    presio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='Eventos/', null=True, blank=True)
    fecha = models.DateTimeField()

    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    nombre_evento = models.CharField(max_length=100)
    a_nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.a_nombre
    