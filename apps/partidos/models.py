from django.db import models


class Partido(models.Model):
	torneo = models.CharField(max_length=45, blank=True)
	visitante = models.CharField(max_length=30, blank=True)
	fecha = models.DateField(blank=True, null=True)
	hora = models.TimeField(blank=True, null=True)
	
	def __unicode__(self):
		return self.visitante

