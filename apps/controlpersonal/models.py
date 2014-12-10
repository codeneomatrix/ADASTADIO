from django.db import models
from django.contrib.auth.models import User

class perfilesper(models.Model):
    usuario = models.OneToOneField(User)
    nombre = models.CharField(max_length=50, blank=True)
    fechaingreso = models.DateField(blank=True, null=True)
    fechanacimiento = models.DateField(blank=True, null=True)  
    puesto = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
    	return self.usuario.username