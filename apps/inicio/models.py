from django.db import models
from django.contrib.auth.models import User

class Perfiles(models.Model):
    usuario = models.OneToOneField(User)
    nombre = models.CharField(max_length=50, blank=True)
    tarjeta = models.CharField(max_length=16, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    domicilio = models.CharField(max_length=40, blank=True)
    tipou = models.CharField(max_length=16,default='cliente')

    def __unicode__(self):
        return self.usuario.username

