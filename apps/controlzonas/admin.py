from django.contrib import admin
from .models import Zona, Areas

class AreaAdmin(admin.ModelAdmin):
	list_display = ('idzona','nombre','precio','asientosdisponibles') 
	list_filter = ('idzona',)
	list_editable = ('idzona','nombre','precio','asientosdisponibles') 

class ZonaAdmin(admin.ModelAdmin):
	list_display = ('nombre','cantidaboletos','tratoespecial') 
	list_filter = ('nombre',)
	list_editable = ('nombre','cantidaboletos')

admin.site.register(Zona,ZonaAdmin)
admin.site.register(Areas,AreaAdmin)