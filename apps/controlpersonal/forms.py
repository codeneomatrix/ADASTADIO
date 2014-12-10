from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
	nombre = forms.CharField(label = "NOMBRE COMPLETO")
	fechaingreso = forms.DateField(label="FECHA DE INGRESO ")
	fechanacimiento = forms.DateField(label="FECHA DE NACIMIENTO")
	puesto = forms.CharField(label="PUESTO")

	
