from django.db import models

# Create your models here.

class Receta(models.Model):
	nombre = models.CharField(max_length=30)
	instructiones = models.TextField()
	fecha = models.DateTimeField()
