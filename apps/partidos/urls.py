from django.conf.urls import patterns, include, url
from .views  import RegistrarPartido, MostrarPartido
 

urlpatterns = patterns('',
   
    url(r'^registrarpartidos/$', RegistrarPartido.as_view(), name='registrar_partidos'),

    #vista a donde se envia una vez que se completa el formulario

    url(r'^mostrarpartidos/$', MostrarPartido.as_view(), name='mostrarpartidos'),
)
