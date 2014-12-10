from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from apps.partidos.models import Partido
from .models import Perfiles
from .forms import UserForm 
from django.shortcuts import redirect

# Create your views here.
class index(TemplateView):
	template_name = 'inicio/index.html'
	#model= Partido

class padmin(TemplateView):
	template_name = 'inicio/panel.html'
	#model= Partido

 
class Login(TemplateView):
	template_name = 'inicio/login.html'
	model= Perfiles
	success_url= reverse_lazy('login') 


class cliente(FormView):
	template_name = 'inicio/cliente.html'
	form_class = UserForm 
	success_url= reverse_lazy('login')

	def form_valid(self, form):
		perfil = Perfiles()
		perfil.nombre = form.cleaned_data['nombre']
		perfil.tarjeta = form.cleaned_data['tarjeta']
		perfil.telefono  = form.cleaned_data['telefono']
		perfil.domicilio = form.cleaned_data['domicilio']
		user = form.save()
		perfil.usuario  = user
  		perfil.save()
		return super(cliente, self).form_valid(form)


