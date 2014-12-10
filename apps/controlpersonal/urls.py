from django.conf.urls import patterns, include, url
from .views  import Personal, Registrarpersonal
 

urlpatterns = patterns('',
   
    url(r'^personal/$', Personal.as_view(), name='personal'),
   
    url(r'^registrarpersonal/$', Registrarpersonal.as_view(), name='registrarpersonal'),

    
)
