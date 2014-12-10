from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from .models import Venta,Descuento
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
class taquilla(CreateView):
	template_name = 'taquilla/taquilla.html'
	model= Venta
	success_url= reverse_lazy('registros') #una vez que se ha registrado el 
								#formulario en la bd decide a donde 
								#te mandara

class ventas(ListView):
	template_name = 'taquilla/registro ventas.html'
	model= Venta
	context_object_name = 'ventas'
####aqui mismose pueden crear la cantida de vistas que uno quiera

class regdescuento(CreateView):
	template_name = 'taquilla/registrar descuentos.html'
	model= Descuento
	success_url= reverse_lazy('mostrardescuentos') #una vez que se ha registrado el 
								#formulario en la bd decide a donde 
								#te mandara

class mostdescuento(ListView):
	template_name = 'taquilla/mostrar descuentos.html'
	model= Descuento
	context_object_name = 'descuentos'