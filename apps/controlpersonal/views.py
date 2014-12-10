from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView,FormView,ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import perfilesper
from .forms import UserForm 
from django.shortcuts import redirect


class Personal(ListView):
	template_name = 'controlpersonal/personal.html'
	model= perfilesper
	context_object_name = 'personas'


class Registrarpersonal(FormView):
	template_name = 'controlpersonal/registro de personal.html'
	form_class = UserForm 
	success_url= reverse_lazy('personal')

	def form_valid(self, form):
		perfil = perfilesper()
		perfil.nombre = form.cleaned_data['nombre']
		perfil.fechaingreso = form.cleaned_data['fechaingreso']
		perfil.fechanacimiento = form.cleaned_data['fechanacimiento']
		perfil.puesto = form.cleaned_data['puesto']
		user = form.save()
		perfil.usuario  = user
  		perfil.save()
		return super(Registrarpersonal, self).form_valid(form)


