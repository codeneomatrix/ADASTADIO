from django.conf.urls import patterns, include, url
from .views  import Aficionado, Registraraficionado
 

urlpatterns = patterns('',
   
    url(r'^aficionados/$', Aficionado.as_view(), name='aficionados'),
   
    url(r'^registraraficionados/$', Registraraficionado.as_view(), name='registraraficionados'),

    
)
