from django.contrib import admin
from .models import perfilesafi

class perfilesafiAdmin(admin.ModelAdmin):
	list_display = ('nombre','idcoordinador','telefono','fecharegistro') 
	list_filter = ('idcoordinador',)

admin.site.register(perfilesafi,perfilesafiAdmin)
