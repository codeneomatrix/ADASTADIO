from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from .models import Partido
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
class RegistrarPartido(CreateView):
	template_name = 'partidos/registro de partidos.html'
	model= Partido
	success_url= reverse_lazy('mostrarpartidos') #una vez que se ha registrado el 
								#formulario en la bd decide a donde 
								#te mandara

class MostrarPartido(ListView):
	template_name = 'partidos/cancelacion y reprogramacion de los partidos.html'
	model= Partido
	context_object_name = 'partidos'
####aqui mismose pueden crear la cantida de vistas que uno quiera

