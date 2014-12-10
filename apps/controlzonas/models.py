from django.db import models

# Create your models here.
class Zona(models.Model):
    nombre = models.CharField(max_length=20, blank=True)
    cantidaboletos = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    tratoespecial = models.CharField(max_length=20, blank=True)
    puertasacceso = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
    	return self.nombre

class Areas(models.Model):
    idzona = models.ForeignKey(Zona)  # Field name made lowercase.
    nombre = models.CharField(max_length=20, blank=True)
    precio = models.IntegerField(blank=True, null=True)
    asientosdisponibles = models.IntegerField(blank=True, null=True)  # Field name made lowercase.

    def __unicode__(self):
        return unicode(self.idzona) + ' ' + str(self.nombre)