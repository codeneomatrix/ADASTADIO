from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from .models import Zona, Areas
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.

class Zonas(ListView):
	template_name = 'controlzonas/control y designacion de areas.html'
	model= Areas
	context_object_name = 'areas'



class Registrarzona(CreateView):
	template_name = 'controlzonas/registro de zonas.html'
	model= Zona
	success_url= reverse_lazy('zonas') #una vez que se ha registrado el 
								#formulario en la bd decide a donde 
								#te mandara

class Registrararea(CreateView):
	template_name = 'controlzonas/registro de areas.html'
	model= Areas
	success_url= reverse_lazy('zonas')
####aqui mismose pueden crear la cantida de vistas que uno quiera
