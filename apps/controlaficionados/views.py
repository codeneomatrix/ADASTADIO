from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView,FormView,ListView,CreateView
from django.core.urlresolvers import reverse_lazy


from .models import perfilesafi
from django.shortcuts import redirect


class Aficionado(ListView):
	template_name = 'controlaficionados/aficionado.html'
	model= perfilesafi
	context_object_name = 'aficionados'


class Registraraficionado(CreateView):
	template_name = 'controlaficionados/registro de aficionados.html'
	model = perfilesafi
	success_url= reverse_lazy('aficionados')



