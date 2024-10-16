from django.db import models

class PrecioHistoricoVehiculos(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    modelo = models.TextField(max_length=120)
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    color = models.CharField(default="Desconocido")
