from django.contrib import admin
from .models import Perfiles

class PerfilesAdmin(admin.ModelAdmin):
	list_display = ('usuario','nombre','telefono','domicilio') 
	list_filter = ('nombre',)

admin.site.register(Perfiles,PerfilesAdmin)



