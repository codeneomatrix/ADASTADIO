from django.db import models
from apps.controlzonas.models import Areas
from apps.partidos.models import Partido
from apps.inicio.models import Perfiles
# Create your models here.

class Descuento(models.Model):
	grupo=models.CharField(max_length=30, blank=True)
	descuento=models.FloatField()
	
	def __unicode__(self):
		return self.grupo


class Venta(models.Model):
	partido=models.ForeignKey(Partido)
	area = models.ForeignKey(Areas)
	cantidad = models.IntegerField(blank=True, null=True)
	tarjeta = models.CharField(max_length=16, default=000000000000000)
	tipoventa = models.CharField(max_length=30, blank=True)  # general o vip
	numeroasiento = models.IntegerField(default=0) 
	nickuser = models.ForeignKey(Perfiles)  
	descuentoa = models.ForeignKey(Descuento)
	monto = models.IntegerField(blank=True, null=True)
	
	def __unicode__(self):
		return self.tipoventa

