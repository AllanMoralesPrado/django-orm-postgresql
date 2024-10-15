from django.db import models

class Automotriz(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class TipoCombustible(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
class DirectorEjecutivo(models.Model):
    automotriz = models.OneToOneField(Automotriz, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.nombre

class ModeloCarro(models.Model):
    nombre = models.CharField(max_length=255)
    automotriz = models.ForeignKey(Automotriz, on_delete=models.SET_NULL, blank=True, null=True)
    tipo_combustible = models.ManyToManyField(TipoCombustible)

    def __str__(self):
        return self.nombre