from django.contrib import admin
from .models import Partido

class PartidoAdmin(admin.ModelAdmin):
	list_display = ('visitante','torneo','fecha','hora') 
	list_filter = ('torneo',)
	list_editable = ('visitante','torneo','fecha','hora') 

admin.site.register(Partido,PartidoAdmin)
