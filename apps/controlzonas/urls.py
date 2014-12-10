from django.conf.urls import patterns, include, url
from .views  import Zonas,Registrarzona,Registrararea
 

urlpatterns = patterns('',
   
    url(r'^zonas/$', Zonas.as_view(), name='zonas'),
   
    url(r'^registrarzonas/$', Registrarzona.as_view(), name='registrarzona'),

    url(r'^registrarareas/$', Registrararea.as_view(), name='registararea'),

)
