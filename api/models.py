from django.db import models

# Create your models here.
class Agentes(models.Models):
    nombre=models.CharField(max_length=50)
    rol=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    habilidad_q=models.CharField(max_length=50)
    habilidad_e=models.CharField(max_length=50)
    habilidad_c=models.CharField(max_length=50)
    definitiva=models.CharField(max_length=50)

    class Meta:
        ordering=['nombre']
