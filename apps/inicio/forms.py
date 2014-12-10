from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
	nombre = forms.CharField(label = "NOMBRE COMPLETO")
	tarjeta = forms.CharField(label="NUM TARJETA")
	telefono = forms.CharField(label="TELEFONO")
	domicilio = forms.CharField(label="DOMICILIO")
	
