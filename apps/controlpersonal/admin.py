from django.contrib import admin
from .models import perfilesper

class perfilesperAdmin(admin.ModelAdmin):
	list_display = ('usuario','nombre','fechaingreso','fechanacimiento','puesto') 
	list_filter = ('nombre',)

admin.site.register(perfilesper,perfilesperAdmin)
