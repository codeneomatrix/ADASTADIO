from django.contrib import admin
from .models import Descuento,Venta
# Register your models here.
class DescuentoAdmin(admin.ModelAdmin):
	list_display = ('descuento','grupo') 
	list_filter = ('grupo',)
	list_editable = ('descuento','grupo')  

admin.site.register(Descuento,DescuentoAdmin)

class VentaAdmin(admin.ModelAdmin):
	list_display = ('id','nickuser','partido','area','cantidad','tipoventa','monto') 
	list_filter = ('tipoventa',)

admin.site.register(Venta,VentaAdmin)