from django.conf.urls import patterns, include, url
from .views  import taquilla, ventas,regdescuento,mostdescuento
 

urlpatterns = patterns('',
   
   url(r'^taquilla/$', taquilla.as_view(), name='taquilla'),

   #vista a donde se envia una vez que se completa el formulario

   url(r'^registros/$', ventas.as_view(), name='registros'),

    url(r'^registrardescuento/$', regdescuento.as_view(), name='registardescuento'),

    url(r'^mostardescuentos/$', mostdescuento.as_view(), name='mostrardescuentos'),
)
