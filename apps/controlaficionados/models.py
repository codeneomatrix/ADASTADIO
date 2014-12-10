from django.db import models
from django.contrib.auth.models import User
from apps.controlpersonal.models import perfilesper

class perfilesafi(models.Model):
    idcoordinador = models.ForeignKey(perfilesper)
    nombre = models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    fecharegistro = models.DateField(blank=True, null=True)  


    def __unicode__(self):
    	return self.nombre